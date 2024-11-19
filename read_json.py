import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            print("Invalid JSON data")
            return
    
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            print("Invalid JSON string")
            return
    
    if isinstance(data, list):
        if len(data) == 0:
            print("Empty JSON list")
            return
        keys = data[0].keys()
    else:
        keys = data.keys()
        data = [data]
    
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    json_file_path = 'questions.json'
    csv_file_path = 'output.csv'
    json_to_csv(json_file_path, csv_file_path)