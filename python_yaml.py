import yaml

CONFIG_FILE = "./params.yaml"

def read_config_file(config_file: str) -> dict:
    with open(config_file, "r") as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded

print(read_config_file(CONFIG_FILE))