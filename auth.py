from fastapi import Header, HTTPException
from api_keys import validate_api_key, record_request

async def verify_api_key(x_api_key: str = Header(...)):
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    record_request(x_api_key)
    return x_api_key