import json

# read the json file and display in nice format
with open('sample.txt','r') as file:
    text = file.read()
    data = json.loads(text)
    for user in data['users']:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        
# count words in a file
with open('file.txt','r') as file:
    text = file.read()
    words = text.split()
    print(words)
    print(f"Total Words: {len(words)}")

# Count unique words in a file
with open('file.txt','r') as file:
    text = file.read()
    unique_words = set(text.split())
    # print(type(unique_words))
    print(f"Unique words in the file is: {unique_words}")
    print(f"Length of the words is: {len(unique_words)}")