import csv
import os

FILENAME = 'contacts.csv'


def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name','Phone','Email'])
            
def add_contact():
    name = input("\nEnter the name: ").strip()
    phone = input("\nEnter the Phone: ").strip()
    email = input("\nEnter the Email: ").strip()
    
    with open(FILENAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name.lower() == row['Name'].strip().lower():
                print("Already Name Exists\n")
                return
            
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,phone,email])
        print("Contact Added Successfully! ")


def view_all():
    with open(FILENAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        print("\n{:<20} | {:<15} | {:<30}".format("Name", "Phone", "Email"))
        print("-" * 70)
        for row in reader:
             print("{:<20} | {:<15} | {:<30}".format(row['Name'], row['Phone'], row['Email']))
        print()
        
        
def search_contact():
    
    search_name = input("Enter the name to Search: ").strip().lower()
    found = False
    
    with open(FILENAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if search_name in row['Name'].strip().lower():
                print("\n Found Contact \n")
                print("Name: " , row['Name'])
                print("Phone: " , row['Phone'])
                print("Email: " , row['Email'])
                found = True
    
    if not found:
        print("No Matching Found")
                
                
def update_contact():
    name_input = input("Enter the name to update: ").strip().lower()
    updated = False
    
    with open(FILENAME, mode='r', newline='') as file:
        contacts = list(csv.DictReader(file))
        
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name','Phone','Email'])
        writer.writeheader()
        for row in contacts:
            if row['Name'].strip().lower() == name_input:
                print("Updating Contact..")
                row['Name'] = input("Enter new Name: ").strip()
                row['Phone'] = input("Enter new Phone: ").strip()
                row['Email'] = input("Enter new Email: ").strip()
                updated = True
            writer.writerow(row)
            
        if updated:
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
            
                
def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").strip().lower()
    deleted = False

    with open(FILENAME, mode='r', newline='') as file:
        contacts = list(csv.DictReader(file))

    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email'])
        writer.writeheader()
        for row in contacts:
            if row['Name'].strip().lower() != name_to_delete:
                writer.writerow(row)
            else:
                deleted = True

    if deleted:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
    
    
        
    

def main():
    init_file()
    
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Good bye")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 6")    
            
        

if __name__ == "__main__":
    main()