"""Configuration management for Capsule."""

import os
from pathlib import Path
from typing import Any, Optional

import yaml


class Config:
    """Manages configuration for Capsule CLI."""
    
    DEFAULT_CONFIG_PATH = Path.home() / ".config" / "capsule" / "config.yaml"
    
    DEFAULT_CONFIG = {
        "api": {
            "gemini_key": None,
        },
        "paths": {
            "knowledge_base": str(Path.cwd()),
            "output_dir": "Materials",
        },
        "defaults": {
            "class_id": "TCM_101",
            "max_attempts": 3,
            "template": "TCM_Pattern_Template_Simple.md",
        },
        "preferences": {
            "theme": "dark",
            "verbose": False,
            "save_logs": True,
        }
    }
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize configuration.
        
        Args:
            config_path: Path to config file. Defaults to ~/.config/capsule/config.yaml
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self._config = self._load_config()
    
    def _load_config(self) -> dict:
        """Load configuration from file or create default."""
        if not self.config_path.exists():
            return self.DEFAULT_CONFIG.copy()
        
        try:
            with open(self.config_path, 'r') as f:
                loaded = yaml.safe_load(f) or {}
                # Merge with defaults to ensure all keys exist
                return self._merge_dicts(self.DEFAULT_CONFIG.copy(), loaded)
        except Exception:
            return self.DEFAULT_CONFIG.copy()
    
    def _merge_dicts(self, base: dict, override: dict) -> dict:
        """Recursively merge override into base."""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_dicts(result[key], value)
            else:
                result[key] = value
        return result
    
    def save(self) -> None:
        """Save configuration to file."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            yaml.safe_dump(self._config, f, default_flow_style=False)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'api.gemini_key')
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        # Check environment variable first
        env_key = f"CAPSULE_{key.upper().replace('.', '_')}"
        if env_key in os.environ:
            return os.environ[env_key]
        
        # Special case for GEMINI_API_KEY
        if key == "api.gemini_key" and "GEMINI_API_KEY" in os.environ:
            return os.environ["GEMINI_API_KEY"]
        
        # Navigate config dict
        parts = key.split('.')
        value = self._config
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value using dot notation.
        
        Args:
            key: Configuration key (e.g., 'api.gemini_key')
            value: Value to set
        """
        parts = key.split('.')
        config = self._config
        
        # Navigate to the parent dict
        for part in parts[:-1]:
            if part not in config or not isinstance(config[part], dict):
                config[part] = {}
            config = config[part]
        
        # Set the value
        config[parts[-1]] = value
    
    def get_all(self) -> dict:
        """Get entire configuration dictionary."""
        return self._config.copy()
    
    def init_interactive(self) -> None:
        """Initialize configuration interactively."""
        try:
            import questionary
            
            # API Key
            api_key = questionary.password(
                "Enter your Gemini API key:",
                default=self.get("api.gemini_key", "")
            ).ask()
            if api_key:
                self.set("api.gemini_key", api_key)
            
            # Knowledge Base Path
            kb_path = questionary.path(
                "Path to TCM Knowledge Base:",
                default=self.get("paths.knowledge_base")
            ).ask()
            if kb_path:
                self.set("paths.knowledge_base", kb_path)
            
            # Class ID
            class_id = questionary.text(
                "Default class ID:",
                default=self.get("defaults.class_id")
            ).ask()
            if class_id:
                self.set("defaults.class_id", class_id)
            
            self.save()
            
        except ImportError:
            # Fallback to basic input if questionary not available
            print("Interactive mode requires 'questionary' package.")
            print("Install with: pip install questionary")


def get_config() -> Config:
    """Get global configuration instance."""
    return Config()
