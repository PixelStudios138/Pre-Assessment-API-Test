import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        show_data(pokemon_data)
    else:
        print(f"Failed to retrieve data: Error {response.status_code}")
    
def show_data(data):
    print(f"Name: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print(f"Base Experience: {data['base_experience']}")