import requests
import json
from poem import Poem
from response_inspector import ResponseInspector

def get_poem(p_path):
    response = requests.get(p_path);
    if response.ok:
        return response
    else:
        print(f'\nERROR main() // HTTP status code: {response.status_code}')
        return None

def main():
    response = get_poem('https://cagibilit.com/wp-json/wp/v2/posts/10555')
    
    if response != None:
        ri = ResponseInspector(response)
        ri.run()

    if response != None:
        # pretty print the JSON response object
        # json_formatted_str = json.dumps(response.json(), indent=2)
        # print(json_formatted_str)

        poem = Poem(response.text)
        print(poem)

if __name__ == '__main__':
    main()