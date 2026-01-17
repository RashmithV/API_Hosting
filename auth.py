import os
from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

API_KEYS = set(
    key.strip()
    for key in os.getenv("MYAPP_API_KEYS", "").split(",")
    if key.strip()
)

if not API_KEYS:
    raise RuntimeError("APP_API_KEYS is not set")


def verify_api_key(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme",
        )

    if credentials.credentials not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return credentials.credentials
