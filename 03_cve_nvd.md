# 03 - NVD CVE 数据采集

## 学习目标

通过 NVD API 获取 CVE 漏洞数据，并完成基础的 AI Security 数据处理。

## 实现功能

- 使用 requests 调用 NVD API
- 使用 keywordSearch 搜索 LLM 相关漏洞
- 使用 startIndex 实现分页
- 处理 HTTP 429
- 处理请求超时
- 对请求进行重试
- 保存中间原始数据
- 解析 CVE ID
- 解析漏洞描述
- 解析 CVSS Severity
- 兼容 CVSS V3.1 和 V2
- 统计漏洞严重等级
- 筛选 HIGH / CRITICAL 漏洞
- 保存 JSON 数据

## 数据流程

NVD API
↓
LLM 关键词搜索
↓
分页获取
↓
CVE 数据整理
↓
Severity 判断
↓
HIGH / CRITICAL 筛选
↓
JSON 保存

## 当前测试结果

搜索关键词：

LLM

NVD 返回结果：

299 条

当前程序可以自动分页获取全部结果。

## 本阶段学习内容

### Python

- 函数
- return
- 异常处理
- requests
- JSON
- 字典和列表
- 文件读写

### API

- API 请求
- HTTP 状态码
- 分页
- API 数据结构差异
- 超时和重试

### AI Security

第一次接触真实漏洞数据库，并尝试建立 LLM 相关漏洞数据集。
