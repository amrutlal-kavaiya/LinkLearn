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
print(type(raw_url_data))
print("-----------------")
print("Raw URL Data")
read_and_process_csv('data.csv')
