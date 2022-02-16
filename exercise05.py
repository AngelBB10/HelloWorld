# AngelBB command processor

print("\nAngelBB command processor.")
for i in range(99):
    command_received = input("Type a command [" + str(i) + "]: ")

    if command_received == "exit":
        break
    else:
        print(command_received)
