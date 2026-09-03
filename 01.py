cves = [
    {
        "id": "CVE-001",
        "name": "LLM Prompt Injection",
        "severity": "HIGH"
    },
    {
        "id": "CVE-002",
        "name": "Web Server Vulnerability",
        "severity": "MEDIUM"
    },
    {
        "id": "CVE-003",
        "name": "AI Model Vulnerability",
        "severity": "CRITICAL"
    }
]

for j in cves:
    if j["severity"]=="HIGH" or j["severity"]=="CRITICAL" :  
        print(j["id"],j["name"])