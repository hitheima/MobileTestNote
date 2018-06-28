import yaml


def analyze_file():
    with open("./data/search_data.yml", 'r') as f:
        return yaml.load(f)
