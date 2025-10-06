import re
from collections import defaultdict

def analyze_logs(log_lines):
    """
    Analyze logs and categorize anomalies by severity.
    Returns a dictionary with:
    - summary
    - anomalies
    - severity_report (High, Medium, Low)
    """
    anomalies = []
    severity_report = defaultdict(list)

    for line in log_lines:
        # High severity: failed logins or critical attacks
        if "401" in line or "403" in line or "failed password" in line.lower():
            anomalies.append(line)
            severity_report["High"].append(line)
        elif re.search(r"(select|union|drop|<script>|alert\()", line, re.IGNORECASE):
            anomalies.append(line)
            severity_report["High"].append(line)

        # Medium severity: server errors
        elif "500" in line or "error" in line.lower():
            anomalies.append(line)
            severity_report["Medium"].append(line)

        # Low severity: timeouts or warnings
        elif "timeout" in line.lower():
            anomalies.append(line)
            severity_report["Low"].append(line)

        # Otherwise, normal log lines
        else:
            continue

    summary = {
        "total_logs": len(log_lines),
        "total_anomalies": len(anomalies),
        "high": len(severity_report["High"]),
        "medium": len(severity_report["Medium"]),
        "low": len(severity_report["Low"])
    }

    return {
        "summary": summary,
        "anomalies": anomalies,
        "severity_report": severity_report
    }
