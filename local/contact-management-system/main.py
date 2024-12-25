import sqlite3

def display_options():
    print(
    "\nOptions available :\n"
    "1 -> Add Contact\n"
    "2 -> Edit Contact\n"
    "3 -> Delete Contact\n"
    "4 -> View Contact\n"
    "5 -> Search Contact\n"
    "6 -> Exit App\n"
)
    
def display_update_choice():
    print(
    "\nOptions available :\n"
    "1 -> Update First Name\n"
    "2 -> Update last Name\n"
    "3 -> Update Phone Number\n"
    "4 -> Exit App\n"
)

def create_database():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    phonenumber TEXT UNIQUE NOT NULL
                )
            ''')
    
    # cur.execute("DROP TABLE contacts")

    con.commit()
    con.close()

def add_contact():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")
    phone_number = input("Please enter the phone number: ")
    
    try:
        cur.execute("INSERT INTO contacts(firstname, lastname, phonenumber) VALUES (?,?,?)", (first_name, last_name, phone_number))
        con.commit()
        print("\nContact added succesfully")
        con.close()
    except sqlite3.IntegrityError:
        print("\nPhone number already present!")

def view_contacts():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    con.close()
    
    if contacts:
        print("\nContacts:")
        print("*"*40)
        for contact in contacts:
            print(f"ID: {contact[0]:<5} First Name: {contact[1]:<15} Last Name: {contact[2]:<10} Phone Number: {contact[3]:<11}")
    else:
        print("\nNo contacts found!")

def update_contacts():
    view_contacts()
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    # contacts = cur.fetchall()
    id = int(input("\nPlease select the Id of the contact you want to update: "))
    while True:
        display_update_choice()
        user_choice = int(input("\nPlease select the option to update(First Name/Last Name/Phone Number): "))
        if user_choice==1:
            first_name = input("\nPlease enter the updated First Name: ")
            query = "UPDATE contacts SET firstname = ? WHERE id = ?"
            parameters = (first_name, id)
            cur.execute(query, parameters)
            print(f"\nFirst Name updated for contact with id - {id}")
        elif user_choice==2:
            last_name = input("\nPlease enter the updated Last Name: ")
            query = "UPDATE contacts SET lastname = ? WHERE id = ?"
            parameters = (last_name, id)
            cur.execute(query, parameters)
            print(f"\nLast Name updated for contact with id - {id}")
        elif user_choice==3:
            phone_number = input("\nPlease enter the updated Phone Number: ")
            query = "UPDATE contacts SET phonenumber = ? WHERE id = ?"
            parameters = (phone_number, id)
            print(f"\nPhone Number updated for contact with id - {id}")
            cur.execute(query, parameters)
        elif user_choice==4:
            con.commit()
            con.close()
            break
        else:
            print("\nPlease select a valid options!")

def delete_contact():
    view_contacts()
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    id = int(input("\nPlease selete the id of contact you want to delete: "))
    query = "DELETE FROM contacts WHERE id = ?"
    paramter = (id,)
    cur.execute(query, paramter)
    print("\nContact Deleted:")
    print("*"*40)
    for contact in contacts:
        if contact[0] == id:
            print(f"ID: {contact[0]:<5} First Name: {contact[1]:<15} Last Name: {contact[2]:<10} Phone Number: {contact[3]:<11}")
            break
    con.commit()
    con.close()

def search_contact():
    try:
        con = sqlite3.connect("contacts.db")
        cur = con.cursor()
        user_query = input("\nPlease enter First Name or Last Name or Phone Number to search: ")
        query = "SELECT * FROM contacts WHERE firstname LIKE ? OR lastname LIKE ? OR phonenumber LIKE ?"
        parameters = (f"%{user_query}%", f"%{user_query}%", f"%{user_query}%")
        cur.execute(query, parameters)
        contacts = cur.fetchall()
        con.close()
        if contacts:
            print("\nSearch Result:")
            print("-"*40)
            for contact in contacts:
                print(f"ID: {contact[0]:<5} First Name: {contact[1]:<15} Last Name: {contact[2]:<10} Phone Number: {contact[3]:<11}")
        else:
            print("\nNo contacts found")
    except Exception as e:
        print(f"Error: {e}")
            

def main():
    create_database()
    print("\nWelcome to Contact Management System")

    while True:
        try:
            display_options()
            user_input = int(input("Please select from the available options: "))

            if user_input == 1:
                add_contact()
            elif user_input == 2:
                update_contacts()
            elif user_input == 3:
                delete_contact()
            elif user_input == 4:
                view_contacts()
            elif user_input == 5:
                search_contact()
            elif user_input == 6:
                print("\nExiting App: Thank you for using our App!!")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()