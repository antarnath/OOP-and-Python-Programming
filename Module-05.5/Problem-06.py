sample_dict = {
    "name": "kelly",
    "age": 25,
    "salary": 80000,
    "city": "New York"
}

keys = ["name","salary"]
output = {}
for key in keys:
    # print(key, sample_dict[key])
    output[key] = sample_dict[key]

print(output)