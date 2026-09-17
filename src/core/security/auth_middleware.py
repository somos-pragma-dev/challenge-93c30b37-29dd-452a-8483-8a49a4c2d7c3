from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from src.core.security.jwt import jwt_handler, JWTHandler


security = HTTPBearer(auto_error=False)


class AuthMiddleware:
    def __init__(self, jwt_handler: JWTHandler):
        self.jwt_handler = jwt_handler

    async def get_current_user(
        self,
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
    ) -> dict:
        if credentials is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se proporcionó token de autenticación",
                headers={"WWW-Authenticate": "Bearer"}
            )
        token = credentials.credentials
        if not self.jwt_handler.verify_token(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado",
                headers={"WWW-Authenticate": "Bearer"}
            )
        payload = self.jwt_handler.decode_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudo validar el token",
                headers={"WWW-Authenticate": "Bearer"}
            )
        user_id = payload.get("sub")
        username = payload.get("username")
        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token sin información de usuario",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return {"user_id": int(user_id), "username": username}

    async def get_optional_current_user(
        self,
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
    ) -> Optional[dict]:
        if credentials is None:
            return None
        token = credentials.credentials
        if not self.jwt_handler.verify_token(token):
            return None
        payload = self.jwt_handler.decode_token(token)
        if payload is None:
            return None
        user_id = payload.get("sub")
        username = payload.get("username")
        if user_id is None or username is None:
            return None
        return {"user_id": int(user_id), "username": username}

    def require_role(self, allowed_roles: list[str]):
        async def role_checker(current_user: dict = Depends(self.get_current_user)) -> dict:
            user_role = current_user.get("role", "user")
            if user_role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="No tiene permisos suficientes para esta acción"
                )
            return current_user
        return role_checker


auth_middleware = AuthMiddleware(jwt_handler)


def get_auth_middleware() -> AuthMiddleware:
    return auth_middleware


async def get_current_user(current_user: dict = Depends(auth_middleware.get_current_user)) -> dict:
    return current_user


async def get_optional_user(current_user: Optional[dict] = Depends(auth_middleware.get_optional_current_user)) -> Optional[dict]:
    return current_user