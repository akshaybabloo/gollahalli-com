import json


def is_json(my_json):
    try:
        json_object = json.loads(my_json)
        del json_object
    except ValueError as e:
        return False
    return True

# if __name__ == '__main__':
#     convert_to_json()