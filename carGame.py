print("*" * 10)
print('''Car Game
type help for commands''')
print("*" * 10)
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car has already started!")
        else:
            started = True
            print("Car has Started")
    elif command == 'stop':
        if not started:
            print("Car has already stopped!")
        else:
            started = False
            print("Car has Stopped")
    elif command == 'help':
        print('''Available commands:
        (1) start
        (2) stop
        (3) exit
        ''')
    elif command == 'exit':
        print("Thanks for playing")
        break
    else:
        print("Invalid command")