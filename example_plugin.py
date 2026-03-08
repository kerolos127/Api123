from tool_registry import register_tool

register_tool("list_processes", "show running processes", "ps aux")
register_tool("disk_usage", "show disk usage", "df -h")
register_tool("check_python", "show python version", "python --version")