import json
from pprint import pprint
from nested_lookup import nested_lookup
from nested_lookup import nested_delete

# in children delete filename, type
child_filename = 'filename'
child_type = 'type'

with open('QAE_json.txt') as js:
    print('JSON BEFORE EDITING: -------------------------------------------------------------')
    data = json.load(js)
    #   post_artifactId = data['artifactId']
    #    post_children = data['children']
    pprint(data)

    # print('HERE------------------------------')
    # for child in data['children']:
    #     print(child)

print('JSON AFTER EDITING: -------------------------------------------------------------')
with open('QAE_json.txt') as js:
    json_object = json.load(js)
    result_arr = []


def get_sub_child_obj(json_arr):
    fixed_arr = []
    for json_obj in json_arr:
        fixed_obj = get_child_objects(json_obj)
        fixed_arr.append(fixed_obj)
    return fixed_arr


def get_child_objects(json_obj):
    child = {}
    
    for attribute, value in json_obj.items():
        if attribute == 'children':
            child['children'] = get_sub_child_obj(value)
        elif (attribute != child_filename) and (attribute != child_type):
            child[attribute] = value
    return child


result_arr = get_sub_child_obj(json_object)
pprint(result_arr)
