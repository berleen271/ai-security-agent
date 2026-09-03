import requests
import json
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
params={
    "resultsPerPage" :"5"
}
print("开始请求")

response = requests.get(url, timeout=10,params=params)

print("请求完成")
print(response.status_code)
data = response.json()

print(type(data))
print(data.keys())
vulnerabilities = data["vulnerabilities"]

print(type(vulnerabilities))

first = vulnerabilities[0]

print(type(first))

print(first.keys())
cve = first["cve"]

print(type(cve))
print(cve.keys())
print(cve["id"])
descriptions = cve["descriptions"]

print(type(descriptions))
first_description = descriptions[0]

print(type(first_description))
print(first_description.keys())
print(first_description["lang"])
print(first_description["value"])
print(cve["metrics"].keys())
cvss = cve["metrics"]["cvssMetricV2"]

print(type(cvss))
print(cvss[0])
print(type(cvss[0]))
cvss_data=cvss[0]
print(cvss_data.keys())
print(cvss_data["baseSeverity"])
cve_list = []
for item in vulnerabilities:
    cvss = item["cve"]["metrics"]["cvssMetricV2"][0]
    cve_info = {
    "id":item["cve"]["id"] ,
    "severity":cvss["baseSeverity"] ,
    "description": item["cve"]["descriptions"][0]["value"]
}
    cve_list.append(cve_info)
for item in cve_list:
    if item["severity"]=="HIGH" or item["severity"]=="CRITICAL":
        print(item)
high_risk_cves = []
for item in cve_list:
    if item["severity"] == "HIGH" or item["severity"] == "CRITICAL":
        high_risk_cves.append(item)
print(high_risk_cves)
with open("high_risk_cves.json", "w") as f:
    f.write(json.dumps(high_risk_cves, indent=2))

with open("high_risk_cves.json", "r") as f:
    content=f.read()
    cve_data=json.loads(content)
    print(type(cve_data))
    print(len(cve_data))
    print(cve_data[0])
keywords = ["AI", "LLM", "machine learning"]
ai_related_cves = []  
for item in cve_data:
    for keyword in keywords:
        if keyword in item["description"]:
            ai_related_cves.append(item)
            break
print(len(ai_related_cves))
for item in vulnerabilities:
    cvss = item["cve"]["metrics"]["cvssMetricV2"]
    print(item["cve"]["id"], len(cvss))
