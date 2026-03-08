import secrets

api_keys = {}

def generate_api_key(owner: str):

    key = "exos_" + secrets.token_hex(32)
    api_keys[key] = {"owner": owner, "requests": 0}
    return key

def validate_api_key(key: str):
    return key in api_keys

def record_request(key: str):
    if key in api_keys:
        api_keys[key]["requests"] += 1