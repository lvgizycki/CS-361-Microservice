import zmq

# Set up ZeroMQ socket to connect to the microservice
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send request to microservice to get random plant details
socket.send_string("get_random_plant_details")
response = socket.recv_json()

# Print received random plant details
print("Received random plant details:", response)
