import json
import csv
import re

def clean_text(text):
    # Remove extra spaces, newlines, and brackets
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.strip('[]')
    return text

def convert_json_to_csv():
    # Read JSON file
    with open('questions.json', 'r') as json_file:
        data = json.load(json_file)

    # Define headers
    headers = [
        'Question', 'Question Type', 'Answer Option 1', 'Explanation 1',
        'Answer Option 2', 'Explanation 2', 'Answer Option 3', 'Explanation 3',
        'Answer Option 4', 'Explanation 4', 'Correct Answers', 'Overall Explanation',
        'Domain'
    ]

    # Process and write to CSV
    with open('questions.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Write headers

        for question_set in data:
            # Split into individual questions and process each
            questions = question_set.split('\n\n')
            for question in questions:
                if not question.strip():
                    continue
                
                # Clean the question text
                question = clean_text(question)
                
                # Split the question into parts
                parts = [part.strip() for part in question.split(',')]
                
                # Skip header rows or malformed data
                if parts[0] == 'Question' or len(parts) != len(headers):
                    continue
                
                # Write the row to CSV
                writer.writerow(parts)

if __name__ == '__main__':
    convert_json_to_csv()
