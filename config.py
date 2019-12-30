import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def get_option(self, section, key):
        try:
            val = self.config[section][key]
        except KeyError:
            val = None
        return val
