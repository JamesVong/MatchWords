JSON_SEARCH = True

if not JSON_SEARCH:
    import requests
    from bs4 import BeautifulSoup
    from ast import literal_eval

import json

def comprehensive_search(limit=1000):
    part = input("Words should contain: ")
    url = f"https://www.thefreedictionary.com/words-containing-{part}"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    scraped = [tag.get_text() for tag in soup.find_all('li', attrs={'data-f': True})]

    words = [text for text in scraped if 'Words ' not in text]

    words.sort(key=len)
    
    for word in words[:limit]:
        print(word)

def quick_search(limit):
    with open('words.txt', 'r') as fp:
        words = fp.read()
    lst = words.replace("{", "[").replace("}", "]")

    word_list = literal_eval(lst)
    part = input("Words should contain: ")

    words = [word for word in word_list if part in word]

    words.sort(key=len)
    for word in words[:limit]:
        print(word)

def json_search(limit):
    with open('words_dictionary.json', 'r') as fp:
        word_dict = json.loads(fp.read())
    
    part = input("Words should contain: ")

    words = [word for word in word_dict.keys() if part in word]

    words.sort(key=len)
    print(len(words))

    with open('output.json', 'w') as fp:
        fp.write(json.dumps(str(words)))

    for word in words[:limit]:
        print(word)

def match_words(limit):
    with open('words_dictionary.json', 'r') as fp:
        word_dict = json.loads(fp.read())
    
    part = input("Hang Man expected input: ")
    search = [letter for letter in part]
    words = []
    
    for word in word_dict.keys():
        match = True
        if len(word) != len(search):
            continue

        for ind in range(len(search)):
            if word[ind].lower() == search[ind].lower() and match != False:
                match = True
            elif search[ind] != '_':
                match = False

        if match:
            words.append(word)

    words.sort(key=len)

    print(f"Found {len(words)} matches.")
    for word in words[:limit]:
        print(word)

# json_search(500)
match_words(10000)
