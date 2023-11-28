This microservice uses ZeroMQ as an asynchronous messaging service (https://zguide.zeromq.org/docs/chapter1/). It is written in python and acts as the server that responds to requests made by the user program through tcp://localhost:5555. The user will need to download the required libraries:
pip install pyzmq

The user will need to open split terminals in the IDE of choice (I used Visual Studio Code Git Bash but also verified on Pycharm using two consoles). They then need to run the microservice.py program, followed by their own program. The screenshots detail the process for the example program.

![image](https://github.com/Johnsonisaacn/CS361_project/assets/114550967/9c772d1d-9126-4c1d-b648-33891a385616)

![image](https://github.com/Johnsonisaacn/CS361_project/assets/114550967/d5c330ca-9022-4951-934e-c0323475e5cf)



![microservice_UML](https://github.com/Johnsonisaacn/CS361_project/assets/114550967/f976feb6-ba72-4534-8784-a5c17219b45c)
