def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Contact {name} is not found"
    old_phone = contacts[name]
    contacts[name] = phone
    return f"Phone for '{name}' changed from {old_phone} to {phone}." 

    



def main():
    contacts = {}
    print("Hi, I'm bot!")
    while True:
        user_input = input("Please, enter command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            for i in contacts:
                print(i, contacts[i])
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
