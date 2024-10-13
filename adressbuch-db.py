import mysql.connector
import configparser

#Config laden
config = configparser.ConfigParser()
config.read('db_config.ini')


# Verbindung zu mysql_DB prüfen
def create_connection():
    connection = mysql.connector.connect(
        host='172.21.69.21',
        user='Huck',
        password='Manuel10!',
        database='mydatabase'  # ggf. anpassen
    )
    return connection

try:
    conn = create_connection()
    print("Verbindung zur MySQL-Datenbank erfolgreich")
    conn.close()
except mysql.connector.Error as err:
    print(f"Fehler: {err}")

# Erstellung von Curser um sql-Befehl durchzuführen.
curser = conn.curser()

# Erstellung von Tabelle 'contacts' in mydatabase
CREATE TABLE contacts ('''
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(50),
    email VARCHAR(100),
    adresse VARCHAR(255),
''' );

# Erste Funktion hinzufügen (CREATE)
def add_contact(name, nummer, email, adresse):
    cursor.execute('''
    INSERT INTO contacts (name, nummer, email, adresse) VALUES (?, ?, ?, ?)
    ''', (name, nummer, email, adresse))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ funktion
def show_contacts():
    cursor.execute('SELECT id, name FROM contacts')
    contacts = cursor.fetchall()
    for name in contacts:
        print(name)

# Update function to update contact data
def update_contact(id, name, nummer, email, adresse):
    cursor.execute('''
    UPDATE contacts SET name = ?, nummer = ?, email = ?, adresse = ?
    WHERE id = ?               
    ''',(name, nummer, email, adresse, id))
    conn.commit()
    print(f"updated contacts with id {id}")

# Adding a delete function to delete a contact

def delete_contact(id):
    cursor.execute('''
    DELETE FROM contacts WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"contact has been deleted with id {id}")

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n----- contactlist -----")
        print("1. contact  hinzufügen")
        print("2. contactlist anzeigen")
        print("3. contact aktualisieren")
        print("4. contact löschen")       
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option (1,2,3,4 oder 5): ")

        if choice == "1":
            print("Bitte gib die Daten des neuen Contacts ein: ")
            name = input("name: ")
            nummer = input("nummer: ")
            email = input("email: ")
            adresse = input("adresse: ")
            add_contact(name, nummer, email, adresse)
        elif choice == "2":
            show_contacts()
        elif choice == "3":
            print("Bitte gib die aktualisierten Daten mit id ein: ")
            id = input("id: ")
            name = input("name: ")
            nummer = input("nummer: ")
            email = input("email: ")
            update_contact(id, name, nummer, email, adresse)
        elif choice == "4":
            print("Bitte gib die ID des zu löschenden contacts ein: ")
            id = input("id: ")
            delete_item(id)
        elif choice == "5":
            print("Programm wird geschlossen. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1,2,3,4 oder 5")

if __name__ == "__main__":
    main()

