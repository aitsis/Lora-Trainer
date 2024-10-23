import json
import os

class ConfigHandler:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump({}, file)  # Create an empty JSON file if it doesn't exist

    def load_config(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_config(self, config):
        with open(self.filename, 'w') as file:
            json.dump(config, file, indent=4)

    def get_key(self, key):
        config = self.load_config()
        return config.get(key)

    def set_key(self, key, value):
        config = self.load_config()
        config[key] = value
        self.save_config(config)
