def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def update_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts.update({name: phone}) 
        return "Contact updated."
    else:
        return "Contact not found. Try again."
   
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Tel.: {contacts[name]}"
    else:
        return "Contact not found. Try again."

def get_all(contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"Name: {name}, Tel.: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()