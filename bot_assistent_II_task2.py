from collections import UserDict

class Field:
 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

class Phone(Field):
    # phone number validation has been implemented (must be 10 digits).
     def __init__(self, value ):
        if not value.isdigit() and len(value) != 10:
            raise ValueError("Invalid number")
        super().__init__(value)

class Record:
    # storage of the Name object in a separate attribute has been implemented.
    # storage of the list of Phone objects in a separate attribute has been implemented.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # implemented method for adding 
    def add_phone(self,phone): 
        self.phones.append(Phone(phone))


    # implemented method for removing 
    def remove_phone(self,phone):
        for phn in self.phones:
            if phn.value == phone:
                self.phones.remove(phn)

    # implemented method for editing
    def edit_phone(self, old_phone, new_phone):
        for phn in self.phones:
            if phn.value == old_phone:
                phn.value = new_phone

    # implemented method for finding Phone objects
    def find_phone(self, phone):
        for phn in self.phones:
            if phn.value == phone:
                return phn

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    # add records to self.data
    def add_record(self, contact):
        self.data[contact.name.value] = contact 

    # find record by the name      
    def find(self, name):
        return self.data.get(name)
    
    # delete record by the name      
    def delete(self, name):
        if name in self.data:
            del self.data[name]

##### You can test code here #####

book = AddressBook()

# create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# add John to the address book
book.add_record(john_record)

# create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# output of all entries in the book
for name, record in book.data.items():
    print(record)

# find and edit phone for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  

# search for a specific phone in the John record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# delete Jane
book.delete("Jane")
for name, record in book.data.items():
    print(record)