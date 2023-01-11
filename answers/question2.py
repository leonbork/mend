import json
from pprint import pprint


with open('QAE_json.txt') as js:
    json_object = json.load(js)
    result_arr = []
    flat_arr = []


def get_sub_child_obj(json_arr):
    for json_obj in json_arr:
        fixed_obj = get_child_objects(json_obj)
        flat_arr.append(fixed_obj)


def get_child_objects(json_obj):
    child = {}

    for attribute, value in json_obj.items():
        if attribute == 'children':
            get_sub_child_obj(value)
            child['children'] = []
        else:
            child[attribute] = value
    return child


get_sub_child_obj(json_object)
pprint(flat_arr)
