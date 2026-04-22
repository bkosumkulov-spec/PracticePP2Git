import csv
from connect import connect

# ------------------------
# CRUD FUNCTIONS
# ------------------------

def insert_contact(username, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")

def get_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def update_contact(contact_id, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET username = %s WHERE id = %s", (new_name, contact_id))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (new_phone, contact_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated!")

def delete_contact(contact_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted!")

# ------------------------
# SEARCH FUNCTIONS
# ------------------------

def search_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s", ('%' + name + '%',))
    rows = cur.fetchall()
    if not rows:
        print("No contacts found with that name.")
    else:
        for row in rows:
            print(row)
    cur.close()
    conn.close()

def search_by_phone_prefix(prefix):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + '%',))
    rows = cur.fetchall()
    if not rows:
        print("No contacts found with that phone prefix.")
    else:
        for row in rows:
            print(row)
    cur.close()
    conn.close()

# ------------------------
# CSV IMPORT
# ------------------------

def import_contacts_from_csv(file_path="contacts.csv"):
    conn = connect()
    cur = conn.cursor()
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row['username'], row['phone']))
        conn.commit()
        print(f"Contacts imported from {file_path}!")
    except FileNotFoundError:
        print(f"CSV file '{file_path}' not found.")
    cur.close()
    conn.close()

# ------------------------
# INTERACTIVE MENU
# ------------------------

def menu():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Show all contacts")
        print("2. Add new contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Import contacts from CSV")
        print("6. Search by name")
        print("7. Search by phone prefix")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "1":
            get_contacts()
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_contact(name, phone)
        elif choice == "3":
            contact_id = int(input("Enter contact ID to update: "))
            new_name = input("Enter new name (leave blank to skip): ").strip()
            new_phone = input("Enter new phone (leave blank to skip): ").strip()
            update_contact(contact_id, new_name if new_name else None, new_phone if new_phone else None)
        elif choice == "4":
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == "5":
            file_path = input("Enter CSV file path (default contacts.csv): ").strip() or "contacts.csv"
            import_contacts_from_csv(file_path)
        elif choice == "6":
            name = input("Enter name to search: ")
            search_by_name(name)
        elif choice == "7":
            prefix = input("Enter phone prefix: ")
            search_by_phone_prefix(prefix)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-8.")

# ------------------------
# MAIN
# ------------------------

if __name__ == "__main__":
    menu()