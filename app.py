import csv
from langchain_community.document_loaders import WebBaseLoader

raw_url_data=[]
def process_url(url):
    print(f"Processing URL: {url}")
    loader = WebBaseLoader(url)
    docs = loader.load()
    print("-----------")
    #print(docs[0].page_content)
    raw_url_data.append(docs[0].page_content)
    print(type(docs))
    print(f"Loaded {len(docs)} documents")
    return docs
    

def read_and_process_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                process_url(row[0])
                print(row)
read_and_process_csv('data.csv')

import answer_gen 
import json

def generate_questions(text):
    response = answer_gen.generate_questions(text)
    return response

def generate_questions_from_raw_data(raw_url_data):
    for data in raw_url_data:
        print("Generating questions for data")
        print(data)
        questions = generate_questions(data)
        print(questions)
        with open('questions.json', 'w') as f:
            json.dump(questions, f)
generate_questions_from_raw_data(raw_url_data)
