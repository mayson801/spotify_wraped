import json
test = [1,2,3,4,5]
def convert_to_json(danceablity):
    json_string = json.dumps(danceablity)
    return json_string
plz = convert_to_json(test)
print(plz)