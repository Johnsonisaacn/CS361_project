#   Microservice for quiz app in Python
#   Binds REP socket to tcp://*:5555


import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

quiz_library = ["'GEOGRAPHY'", "'CHEMISTRY'", "'HISTORY'", "'BIOLOGY'", "'LITERATURE'"]

while True:
    #  Wait for next request from client
    message = str(socket.recv())[1:]
    if message.upper() in quiz_library:
        print("Fetching questions on that topic...")
        time.sleep(1)
        socket.send_string("Here are some quiz questions about " + message)
    else:
        socket.send_string("We didn't find" + message + " in the library. Please try again." )


    
