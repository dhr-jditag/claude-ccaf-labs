from typing import Callable

# ==========================================
# Protected Assets
# ==========================================

PROTECTED_HOSTS = {
    "trading-prod-01",
    "market-data-relay",
    "ceo-laptop",
}

PROTECTED_IPS = {
    "10.0.0.1",
    "192.168.1.10",
}

# ==========================================
# Audit Log
# ==========================================

AUDIT_LOG = []

# ==========================================
# Demo Tools
# ==========================================


def quarantine_host(hostname: str):
    return f"Host '{hostname}' quarantined."


def block_ip(ip: str):
    return f"IP '{ip}' blocked."


DEMO_TOOLS = {
    "quarantine_host": quarantine_host,
    "block_ip": block_ip,
}

# ==========================================
# Hook 1 - Logging
# ==========================================


def logging_hook(tool_name: str, tool_input: dict):

    print(f"[HOOK] Logging -> {tool_name} {tool_input}")

    return True, ""


# ==========================================
# Hook 2 - Validation
# ==========================================


def arg_validation_hook(tool_name: str, tool_input: dict):

    if tool_name == "quarantine_host":

        if "hostname" not in tool_input:
            return False, "Missing required argument: hostname"

    elif tool_name == "block_ip":

        if "ip" not in tool_input:
            return False, "Missing required argument: ip"

    return True, ""


# ==========================================
# Hook 3 - Protected Assets
# ==========================================


def protected_asset_hook(tool_name: str, tool_input: dict):

    if tool_name == "quarantine_host":

        hostname = tool_input.get("hostname")

        if hostname in PROTECTED_HOSTS:
            return False, f"{hostname} is a protected host."

    if tool_name == "block_ip":

        ip = tool_input.get("ip")

        if ip in PROTECTED_IPS:
            return False, f"{ip} is a protected IP."

    return True, ""


# ==========================================
# Hook Engine
# ==========================================


HOOKS = [
    logging_hook,
    arg_validation_hook,
    protected_asset_hook,
]


def run_tool(tool_name: str, tool_input: dict):

    for hook in HOOKS:

        allowed, reason = hook(tool_name, tool_input)

        if not allowed:

            AUDIT_LOG.append(
                {
                    "tool": tool_name,
                    "input": tool_input,
                    "status": "BLOCKED",
                    "reason": reason,
                }
            )

            return f"BLOCKED: {reason}"

    result = DEMO_TOOLS[tool_name](**tool_input)

    AUDIT_LOG.append(
        {
            "tool": tool_name,
            "input": tool_input,
            "status": "SUCCESS",
        }
    )

    return result


# ==========================================
# Audit Viewer
# ==========================================


def print_audit_log():

    print("\n========== AUDIT LOG ==========\n")

    for entry in AUDIT_LOG:
        print(entry)