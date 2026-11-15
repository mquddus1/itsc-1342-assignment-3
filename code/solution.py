# Mohammed Abdul Quddus - Assignment 3

def format_alert(severity, source_ip, alert_message):
    # Return a formatted string in the pattern: [SEVERITY] - IP: MESSAGE
    return f"[{severity}] - {source_ip}: {alert_message}"
