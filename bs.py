def get_links(url):
    import requests
    from bs4 import BeautifulSoup
    result = requests.get(url)
    page = result.text  
    doc = BeautifulSoup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

def get_class(url):
    import requests
    from bs4 import BeautifulSoup
    result = requests.get(url)
    page = result.text 
    doc = BeautifulSoup(page)
    class_list = [element.get("class") for element in doc.find_all("div")]
    return class_list

if __name__ == "__main__":
    import sys
    for url in sys.argv[1:]:
        print('Links in', url)
        for num, link in enumerate(get_class(url), start = 1):
            print(num, link)
            print()

    
