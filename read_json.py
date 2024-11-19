import json
import csv

def convert_json_to_csv():
    # Read JSON file
    with open('questions.json', 'r') as json_file:
        data = json.load(json_file)

    # Prepare CSV headers
    headers = [
        'Question', 'Question Type', 'Answer Option 1', 'Explanation 1',
        'Answer Option 2', 'Explanation 2', 'Answer Option 3', 'Explanation 3',
        'Answer Option 4', 'Explanation 4', 'Correct Answers', 'Overall Explanation',
        'Domain'
    ]

    # Write to CSV file
    with open('questions.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for question_set in data:
            # Split the question set into individual questions
            questions = question_set.split('\n\n')
            for question in questions:
                if question.strip():
                    # Parse each question and extract values
                    parts = question.strip('[]').split(', ')
                    if len(parts) == len(headers):
                        writer.writerow(parts)

if __name__ == '__main__':
    convert_json_to_csv()
