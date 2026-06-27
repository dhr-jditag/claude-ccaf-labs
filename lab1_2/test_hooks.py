from lab1_2.tool_hooks import run_tool, print_audit_log

print(run_tool(
    "quarantine_host",
    {
        "hostname": "dev-server"
    }
))

print(run_tool(
    "quarantine_host",
    {
        "hostname": "trading-prod-01"
    }
))

print(run_tool(
    "block_ip",
    {
        "ip": "10.0.0.1"
    }
))

print(run_tool(
    "block_ip",
    {
        "ip": "8.8.8.8"
    }
))

print_audit_log()