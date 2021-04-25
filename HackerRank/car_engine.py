driver_command = ""
car_started = False
while driver_command != "quit":
    driver_command = input(">").lower()
    if driver_command == "help":
        print("Start - To start the car\nStop - To stop the car\nStatus - To check status\nQuit - To "
              "exit")
    elif driver_command == "start":
        if not car_started:
            print("Car started")
            car_started = True
        else:
            print("Car already started")
    elif driver_command == "stop":
        if car_started:
            print("Car stopped")
            car_started = False
        else:
            print("Car already stopped")
    elif driver_command == "status":
        if car_started:
            print("Car is already running")
        else:
            print("Car is not running")
    elif driver_command == "quit":
        break
    else:
        print("Invalid input")
