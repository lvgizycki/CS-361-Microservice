# CS-361-Microservice - Random Plant Generator

 # Communication Contract:
 To request data from the microservice, follow these steps:
 1. Establish a ZeroMQ socket connection with the microservice
 2. Send a string message indicating the type of data you want to request
 3. Wait for the response from the microservice
 4. Receive the response in JSON format

# Example Call:

import zmq


context = zmq.Context()

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")


socket.send_string("get_random_plant_details")

response = socket.recv_json()


print("Received random plant details:", response)


# Receiving Data:
The microservice will respond to requests with plant details in JSON format. You can receive the data by:
1. Listening for incoming responses from the microservice
2. Upon receiving the response, parse the JSON data to extract the plant details


# UML Sequence Diagram:
![UMLseq](https://github.com/lvgizycki/CS-361-Microservice/assets/100311267/6a4cfa06-d30d-42ef-9d29-2b9837c7c0c1)
