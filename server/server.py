import hashlib, requests

def check_key(key):
    data = requests.get("https://raw.githubusercontent.com/Idlekahbo/Fileforge/iss#3/server/server.json").json()
    return hashlib.sha256(key.encode()).hexdigest() in data["Productkeys"]
