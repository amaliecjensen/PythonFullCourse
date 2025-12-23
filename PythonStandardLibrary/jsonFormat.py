import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 1, "title": "Terminator", "year": 1992}
# ]

# data = json.dumps(movies)

data = Path("movies.json").read_text()
movies = json.loads(data)
