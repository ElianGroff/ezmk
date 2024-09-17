import configparser
import os

from .constants import DEFAULT_CONFIG


class ConfigManager:

    def __init__ (self):
        self.config = {}
        self.config_file = "ezmk.cfg"
        self.load_defaults()

    def load_defaults(self):
        self.config = DEFAULT_CONFIG

        if os.path.exists(self.config_file):
            parser = configparser.ConfigParser()
            parser.read(self.config_file)

            for section in parser.sections():
                for option in parser.options(section):
                    self.config[section][option] = parser.get(section, option)

    def get(self, key):
        return self.config.get(key)
    
    def set(self, key, value):
        self.config[key] = value

