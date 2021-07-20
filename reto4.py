import json

def func(dicc,search):
    json_obj = json.loads(dicc)
    sum = 0;
    values = []
    result = ""
    for i in search:
        for key, value in json_obj.items():
            if key == i:
                 sum = value + sum
                 values.append(key)
                 result = " ".join(values)
    print(sum)
    print(result)


func(dicc = input(), search = input())

