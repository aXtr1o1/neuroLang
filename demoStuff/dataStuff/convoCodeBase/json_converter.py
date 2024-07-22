import json

with open("Angular_textFile.txt","r") as file:
    dictionary_string = file.read()

dictionary = eval(dictionary_string)
# print(dictionary)

json_data = json.dumps(dictionary, indent=4)

with open("Angular_Questions.json",'w') as json_file:
    json_file.write(json_data)

print("Dictionary successfully converted to json file")
