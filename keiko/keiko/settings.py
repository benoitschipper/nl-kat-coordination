"""Keiko settings module."""
from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, DirectoryPath, Field, FilePath


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    debug: bool = Field(False, description="Enable global debug mode, which increases logging verbosity", env="DEBUG")
    log_cfg: FilePath = Field("logging.json", description="Path to the logging configuration file")
    templates_folder: DirectoryPath = Field("templates", description="Folder containing the templates")
    glossaries_folder: DirectoryPath = Field("glossaries", description="Folder containing the glossaries")
    assets_folder: DirectoryPath = Field("assets", description="Folder containing the assets")
    reports_folder: DirectoryPath = Field("/reports", description="Output folder containing the reports")

    span_export_grpc_endpoint: Optional[AnyHttpUrl] = Field(
        None, description="OpenTelemetry endpoint", env="SPAN_EXPORT_GRPC_ENDPOINT"
    )

    class Config:
        env_prefix = "KEIKO_"
