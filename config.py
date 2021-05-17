from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_PREFIX: str = '/api/p'

    POSTGRES_HOST: str = '172.20.10.2'
    POSTGRES_USER: str = 'ds'
    POSTGRES_PASSWORD: str = 'dspassword'
    POSTGRES_DB: str = 'ds'
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_HOST'),
            path=f'/{values.get("POSTGRES_DB") or ""}'
        )

    HBASE_HOST: str = '172.20.10.3'
    HBASE_PORT: int = 9090

    KEYCLOAK_SERVER_URL: str = 'http://172.20.10.5:8080/auth/'
    KEYCLOAK_CLIENT_ID: str = 'python'
    KEYCLOAK_REALM_NAME: str = 'ds'
    KEYCLOAK_CLIENT_SECRET_KEY: str = '6eb73628-604f-49dc-adcc-8351a89cad4d'

    class Config:
        case_sensitive = True


settings = Settings()