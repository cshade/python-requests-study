class ResponseInspector:

    def __init__(self, a):
        self.r = a
    
    def run(self):
        print('\n---------------\nRESPONSE INSPECTOR\n')
        seconds = str(round(self.r.elapsed.total_seconds(),2))
        print(f"Time elapsed: {seconds} seconds")
        print(f"Status code: {self.r.status_code}") # expect 200
        print(f"Encoding: {self.r.encoding}") # expect 'UTF-8'
        print(f"History (i.e. 301s): {self.r.history}") # expect no 301 redirection
        print(f"Response headers: {self.r.headers['Content-Type']}") # expect JSON
        print('\n---------------\n')