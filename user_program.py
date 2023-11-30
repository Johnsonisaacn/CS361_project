#   Stand-in for user program in Python
#   Connects REQ socket to tcp://localhost:5555


import zmq

context = zmq.Context()

#  Socket to talk to server
proceed = True
while proceed is True:

    topic = input("Enter a topic you would like to quiz yourself on (press x to exit): ")
    if topic == "x":
        print("Thank you for using the quiz app, have a nice day!")
        proceed = False
        continue

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_string(topic)
    message = str(socket.recv())[1:]
    print(message)
