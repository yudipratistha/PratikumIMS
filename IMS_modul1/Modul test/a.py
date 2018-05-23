# import president as president
#
import json

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
# data = json.load(president)
# print(type(data))
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)

people_string = {
    "people": [
        {
            "name": "John Sminth",
            "phone": "2323231234",
            "emails": "aweasd",

        }
    ]
}


data = json.people_string
print(type(data))
print(data)