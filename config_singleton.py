import json


class ConfigSingleton:
    _instance = None
    _config = None

    def __new__(cls, config_path="config.json"):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            with open(config_path, "r") as file:
                cls._config = json.load(file)
        return cls._instance

    @property
    def config(self):
        return self._config
