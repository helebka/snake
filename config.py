import json

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = 800, 600
FPS = 15


def get_data() -> dict:
    with open("data/data.json", "r") as json_file:
        json_data = json.load(json_file)
    return json_data


def write_data(data: dict) -> None:
    with open("data/data.json", "w") as json_file:
        json.dump(data, json_file)
