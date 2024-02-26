import zmq
import requests
import random

# Function to generate a random plant ID
def generate_random_plant_id():
    # 3000 plants available in the database
    return random.randint(1, 3000)


# Function to fetch plant details for a given plant ID from Perenual API
def fetch_plant_details(plant_id):
    api_key = "sk-g7Ma65dcf66fb13704373"
    url = f"https://perenual.com/api/species/details/{plant_id}?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch plant details"}

# Set up ZeroMQ socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Listen for incoming requests and respond with plant details
while True:
    message = socket.recv_string()
    if message == "get_random_plant_details":
        plant_id = generate_random_plant_id()
        plant_details = fetch_plant_details(plant_id)
        socket.send_json(plant_details)
    else:
        socket.send_string("Invalid request")
