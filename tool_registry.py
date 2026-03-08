tools = {}

def register_tool(name, description, command):
    tools[name] = {"description": description, "command": command}

def list_tools():
    return tools

def run_tool(name):
    if name not in tools:
        return None
    return tools[name]["command"]