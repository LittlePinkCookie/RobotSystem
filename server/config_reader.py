import json
import sys
from json import JSONDecodeError


class ConfigReader:
    def __init__(self, file_path: str):
        try:
            f = open(file_path)
            self.data = json.load(f)
        except OSError:
            print("Unable to open file {}. Aborting.".format(file_path))
            sys.exit(-1)
        except JSONDecodeError:
            print("Error while reading configuration file. Aborting.")
            sys.exit(-1)

    def get_param(self, param_name: str) -> str:
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
