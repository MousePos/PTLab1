import yaml
from typing import List, Dict
from DataReader import DataReader

class YamlDataReader(DataReader):
    def read(self, path: str) -> List[Dict[str, Dict[str, int]]]:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data