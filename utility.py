import json


def is_json(my_json):
    try:
        json_object = json.loads(my_json)
        del json_object
    except ValueError as e:
        return False
    return True


def convert_to_json(value):
    value.replace("\u2018", "").encode("utf-8")
    print(value)
    # a = json.loads(value, strict=False)
    # print(a)
    return value

# if __name__ == '__main__':
#     convert_to_json()