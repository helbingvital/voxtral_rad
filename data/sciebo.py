import os
from pysciebo import ScieboClient

url = os.environ["SCIEBO_URL"]
username = os.environ["SCIEBO_USERNAME"]
password = os.environ["SCIEBO_PASSWORD"]

# Login
client = ScieboClient(url, username, password)

# Upload a file to sciebo
client.upload("/sciebo/file/path", "/local/file/path")

# Download a file from sciebo (local path is optional)
client.download("/sciebo/file/path", "/local/file/path")

# Delete a file from sciebo
client.delete("/sciebo/file/path")