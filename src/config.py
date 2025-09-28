try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings

class Settings(BaseSettings):
    """Configuration settings for Playbook MCP Server"""
    
    server_name: str = "Playbook MCP Server"
    port: int = 8080
    environment: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()