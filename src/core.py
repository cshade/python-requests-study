import requests
import json
from poem import Poem
from response_inspector import ResponseInspector

def inspect_response(response_obj):
    seconds = str(round(response_obj.elapsed.total_seconds(),2))
    print(f"Time elapsed: {seconds} seconds")
    print(f"Status code: {response_obj.status_code}") # expect 200
    print(f"Encoding: {response_obj.encoding}") # expect 'UTF-8'
    print(f"History (i.e. 301s): {response_obj.history}") # expect no 301 redirection
    print(f"Response headers: {response_obj.headers['Content-Type']}") # expect JSON

def main():
    response = requests.get('https://cagibilit.com/wp-json/wp/v2/posts/10555')
    print(f"\nmain() GET request to: {response.url}")
    ri = ResponseInspector(response)
    ri.run()

    # could simply use "if response", but really we need a 200
    if response.status_code == 200:
        # pretty print the JSON response object
        # json_formatted_str = json.dumps(response.json(), indent=2)
        # print(json_formatted_str)

        poem = Poem(response.text)
        print(poem)
    else:
        print(f'main() ERROR // HTTP status code: {response.status_code}')

if __name__ == '__main__':
    main()