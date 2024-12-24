import sqlite3

def display_options():
    print(
    "\nOptions available :\n"
    "1 -> Add Contact\n"
    "2 -> Edit Contact\n"
    "3 -> Delete Contact\n"
    "4 -> View Contact\n"
    "5 -> Exit App\n"
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
            id = contact[0]
            firstname = contact[1]
            lastname = contact[2]
            phonenumber = contact[3]
            print(f"ID: {id:<5} First Name: {firstname:<10} Last Name: {lastname:<10} Phone Number: {phonenumber:<11}")
    else:
        print("\nNo contacts found!")


def main():
    create_database()
    print("Welcome to Contact Management System")

    while True:
        try:
            display_options()
            user_input = int(input("Please select from the available options: "))

            if user_input == 1:
                add_contact()
            elif user_input == 4:
                view_contacts()
            elif user_input == 5:
                print("\nExiting App: Thank you for using our App!!")
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()