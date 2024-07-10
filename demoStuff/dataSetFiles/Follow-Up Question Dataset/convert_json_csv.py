import json
import csv

with open("Angular_Questions_Follow-up_Questions.txt","r") as file:
    data = json.load(file)
    

with open('AngularQuestions.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['prompt','response','follow_up_question'])
    writer.writeheader()


    for entry in data:
        writer.writerow(entry)
    

print("Dictionary has been successfully converted to CSV format.")