# Python Requests Module Study

A repo for studying Python's Requests module and for reference, and for continually improving and expanding. Using Python 3.

## Design Notes

Requests are made to public domain poetry & prose found in Cagibi journal, at cagibilit.com. Cagibi is an online journal on WordPress, and so this uses the WordPress REST API.

Consists of a core.py main program, and two classes:  Poem and ResponseInspector.

### Run

Running src/core.py within VSCode
```bash
/usr/local/bin/python3 /Users/.../requests-study/src/core.py
```

If requests ModuleNotFoundError, run below pip3 command (Python 3) to install, or see Requests link under Built With section for installation guide:
```bash
pip3 install requests
```

## Built With

- Python 3.7.4
- [Requests](https://requests.readthedocs.io/en/latest/): an HTTP library for Python
- [json](https://docs.python.org/3/library/json.html): JSON encoder and decoder for Python
- [WordPress REST API](https://developer.wordpress.org/rest-api/)