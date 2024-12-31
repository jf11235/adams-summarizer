import wikipediaapi
import os
import yaml

def get_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config


email = get_config()['email']

user_agent = f"Adam\'s Practice Python Scraper ({email})"
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent)

page_title = 'Ball python'
page_py = wiki_wiki.page(page_title)

#check if the texts directory exists if not make it
dir_name = 'texts'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

#check if the file exists if not make it
file_name = os.path.join(dir_name, page_title + '.txt')
if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write(page_py.text)
