import requests
import json
import time


# =========================
# 1. NVD API 配置
# =========================

url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

results_per_page = 20


# =========================
# 2. 获取 NVD CVE 数据
# =========================

def fetch_cves():

    all_vulnerabilities = []

    start_index = 0
    page_count = 0

    # 每一页最多重试 3 次
    max_retries = 3

    while True:

        params = {
            "resultsPerPage": results_per_page,
            "startIndex": start_index,
            "keywordSearch": "LLM"
        }

        retry_count = 0

        while retry_count < max_retries:

            print(f"正在请求：startIndex={start_index}")

            try:

                response = requests.get(
                    url,
                    params=params,
                    timeout=30
                )

                print(f"请求完成：{response.status_code}")

            except requests.exceptions.Timeout:

                retry_count += 1

                print(
                    f"请求超时，第 {retry_count}/{max_retries} 次重试"
                )

                time.sleep(5)
                continue

            except requests.exceptions.RequestException as e:

                retry_count += 1

                print(
                    f"网络请求失败，第 {retry_count}/{max_retries} 次重试"
                )

                print(e)

                time.sleep(5)
                continue


            # =========================
            # 请求成功
            # =========================

            if response.status_code == 200:

                data = response.json()

                total_results = data["totalResults"]
                vulnerabilities = data["vulnerabilities"]

                all_vulnerabilities.extend(vulnerabilities)

                print(f"本页数量：{len(vulnerabilities)}")
                print(f"总结果数：{total_results}")
                print(
                    f"当前已获取：{len(all_vulnerabilities)} 条"
                )

                # =========================
                # 保存当前已经获取的数据
                # =========================

                with open(
                    "llm_cves_raw.json",
                    "w",
                    encoding="utf-8"
                ) as f:

                    json.dump(
                        all_vulnerabilities,
                        f,
                        ensure_ascii=False,
                        indent=2
                    )

                print("中间数据已保存")

                start_index += results_per_page
                page_count += 1

                break


            # =========================
            # 请求过快
            # =========================

            elif response.status_code == 429:

                retry_count += 1

                print(
                    f"请求过快，第 {retry_count}/{max_retries} 次重试"
                )

                time.sleep(5)


            # =========================
            # 其他 HTTP 错误
            # =========================

            else:

                raise Exception(
                    f"请求失败，状态码：{response.status_code}"
                )


        # =========================
        # 当前页面连续失败
        # =========================

        else:

            raise Exception(
                f"连续 {max_retries} 次请求失败，停止程序"
            )
        # =========================
        # 已经获取全部结果
        # =========================

        if start_index >= total_results:

            break


    print()
    print("=========================")
    print("分页测试完成")
    print("=========================")

    print(f"获取页数：{page_count}")
    print(f"获取漏洞数量：{len(all_vulnerabilities)}")

    return all_vulnerabilities


# =========================
# 3. 整理 CVE 数据
# =========================

def normalize_cves(all_vulnerabilities):

    cve_list = []

    for item in all_vulnerabilities:

        cve = item["cve"]
        metrics = cve["metrics"]

        if "cvssMetricV31" in metrics:

            severity = (
                metrics["cvssMetricV31"][0]
                ["cvssData"]["baseSeverity"]
            )

        elif "cvssMetricV2" in metrics:

            severity = (
                metrics["cvssMetricV2"][0]
                ["baseSeverity"]
            )

        else:

            severity = "UNKNOWN"

        cve_info = {
            "id": cve["id"],
            "severity": severity,
            "description": cve["descriptions"][0]["value"]
        }

        cve_list.append(cve_info)

    return cve_list


# =========================
# 4. 筛选高风险 CVE
# =========================

def filter_high_risk(cve_list):

    high_risk_cves = []

    for item in cve_list:

        if (
            item["severity"] == "CRITICAL"
            or item["severity"] == "HIGH"
        ):
            high_risk_cves.append(item)

    return high_risk_cves


# =========================
# 5. 保存 JSON
# =========================

def save_json(data, filename):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(f"JSON 保存完成：{filename}")


# =========================
# 6. 主程序
# =========================

all_vulnerabilities = fetch_cves()


cve_list = normalize_cves(
    all_vulnerabilities
)


print()
print("=========================")
print("CVE 数据整理完成")
print("=========================")

print(f"CVE 数量：{len(cve_list)}")
print(cve_list[0])


# =========================
# 7. 严重等级统计
# =========================

severity_count = {}

for item in cve_list:

    severity = item["severity"]

    if severity not in severity_count:

        severity_count[severity] = 0

    severity_count[severity] += 1


print()
print("=========================")
print("严重等级统计")
print("=========================")

print(severity_count)


# =========================
# 8. 筛选高风险漏洞
# =========================

high_risk_cves = filter_high_risk(
    cve_list
)


print()
print("=========================")
print("高风险 CVE")
print("=========================")

print(
    f"高风险数量：{len(high_risk_cves)}"
)


# =========================
# 9. 保存高风险漏洞
# =========================

save_json(
    high_risk_cves,
    "llm_high_risk_cves.json"
)