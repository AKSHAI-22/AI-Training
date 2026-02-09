reports = [
    {"app_version": "1.0", "device": "Android", "severity": "HIGH"},
    {"app_version": "1.1", "device": "iOS", "severity": "LOW"},
    {"app_version": "1.0", "device": "Android", "severity": "MEDIUM"},
    {"app_version": "1.2", "device": "Android", "severity": "HIGH"},
    {"app_version": "1.1", "device": "iOS", "severity": "HIGH"}
]

high = []
version_count = {}
for r in reports:
    if r["severity"] == "HIGH":
        high.append(r)
    v = r["app_version"]
    if v in version_count:
        version_count[v] += 1
    else:
        version_count[v] = 1
print("High severity reports:", high)
print("Crash count per version:", version_count)
