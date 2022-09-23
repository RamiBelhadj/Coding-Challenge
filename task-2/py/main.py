import json


def get_data_from_db():
    with open('../mock-data.json') as json_file:
        return json.load(json_file)


class Cache:
    def __init__(self):
        pass


if __name__ == '__main__':
    cache = Cache()
