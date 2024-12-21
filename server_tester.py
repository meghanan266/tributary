import requests as requests

data = {
    "engine_temperature": 0.3,
}

response = requests.post("http://127.0.0.1:8000/record", json=data)
print(response.content)


def test_collect():
    response = requests.post("http://127.0.0.1:8000/collect", json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error while fetching data: {response.text}")


test_collect()
