from pprint import pprint



dir_name = 'texts'
file_name = '/Ball python.txt'

with open(dir_name + file_name, 'r') as f:
    text = f.read()
    

print(text)