import os
import yaml

def load_config():
    config_path = os.path.join("config", "config.yaml")  # Use os.path.join for portability
    with open(config_path, "r") as file:
        return yaml.safe_load(file)