import json
import sys
from json import JSONDecodeError


class ConfigReader:
    def __init__(self, file_path: str):
        try:
            f = open(file_path)
            self.data = json.load(f)
        except OSError as e:
            print("Unable to open file {} for reason : {}. Aborting.".format(file_path, e))
            sys.exit(-1)
        except JSONDecodeError:
            print("Error while reading configuration file. Aborting.")
            sys.exit(-1)

    def get_param(self, param_name: str, default_value=None) -> str:
        try:
            params = param_name.split(".")
            if len(params) == 0:
                return self.data[param_name]
            else:
                search_into = self.data[params[0]]
                for param in params:
                    if param == params[0]:
                        continue
                    search_into = search_into[param]
                return search_into
        except KeyError:
            print("Unable to find {}. Using default value : {}".format(param_name, default_value))
            return default_value


config = ConfigReader("config.json")
