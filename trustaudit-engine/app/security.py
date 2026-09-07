from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Placeholder for RBAC & JWT validation per nTrust security baseline
    return {"user": "auditor", "role": "admin"}
