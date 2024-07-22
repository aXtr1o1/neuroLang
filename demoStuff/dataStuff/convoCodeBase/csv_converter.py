import csv
import ast

with open("Angular_textFile.txt","r") as file:
    dictionary_string = file.read()

dictionary = ast.literal_eval(dictionary_string)
# print(dictionary)

with open('Angular_Questions.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    headers = dictionary.keys()
    writer.writerow(headers)

    rows = zip(*dictionary.values())
    writer.writerows(rows)

print("Dictionary has been successfully converted to CSV format.")
