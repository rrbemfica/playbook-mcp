try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings

from pydantic import ConfigDict

class Settings(BaseSettings):
    """Configuration settings for Playbook MCP Server"""
    
    model_config = ConfigDict(env_file=".env")
    
    server_name: str = "Playbook MCP Server"
    port: int = 8000
    environment: str = "development"

settings = Settings()