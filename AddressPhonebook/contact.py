import tkinter as tk
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError
import sqlite3

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

class AddressBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Address Book Application")

        self.contact_list = []

        self.load_contacts()

        self.create_widgets()

    def create_widgets(self):
        # Listbox to display contacts
        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, height=10, width=50)
        self.listbox.grid(row=0, column=0, rowspan=6, padx=10, pady=10)

        # Labels
        tk.Label(self.master, text="Name:").grid(row=0, column=1, sticky=tk.W)
        tk.Label(self.master, text="Phone Number:").grid(row=1, column=1, sticky=tk.W)
        tk.Label(self.master, text="Email:").grid(row=2, column=1, sticky=tk.W)
        tk.Label(self.master, text="Address:").grid(row=3, column=1, sticky=tk.W)

        # Entry widgets
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=2, padx=10, pady=5, sticky=tk.W)

        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=2, padx=10, pady=5, sticky=tk.W)

        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

        # Buttons
        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=1, pady=10)
        tk.Button(self.master, text="Edit Contact", command=self.edit_contact).grid(row=4, column=2, pady=10)
        tk.Button(self.master, text="Delete Contact", command=self.delete_contact).grid(row=5, column=1, pady=10)
        tk.Button(self.master, text="View All Contacts", command=self.view_all_contacts).grid(row=5, column=2, pady=10)

        # Bind listbox selection to a function
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Populate listbox with contact names
        self.populate_listbox()

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contact_list:
            self.listbox.insert(tk.END, contact.name)

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone_number or not email or not address:
            self.show_message("Please fill in all fields.")
            return

        if not is_valid_email(email):
            self.show_message("Invalid email address.")
            return

        new_contact = Contact(name, phone_number, email, address)
        self.contact_list.append(new_contact)
        self.save_contacts()
        self.show_message("Contact added successfully!")
        self.populate_listbox()

    def edit_contact(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.show_message("Please select a contact to edit.")
            return

        index = selected_index[0]
        selected_contact = self.contact_list[index]

        # Update entry widgets with selected contact details
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, selected_contact.name)

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, selected_contact.phone_number)

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, selected_contact.email)

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, selected_contact.address)

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            self.show_message("Please select a contact to delete.")
            return

        index = selected_index[0]
        deleted_contact = self.contact_list.pop(index)
        self.save_contacts()
        self.show_message(f"Contact '{deleted_contact.name}' deleted successfully!")
        self.populate_listbox()

    def view_all_contacts(self):
        if not self.contact_list:
            self.show_message("No contacts found.")
        else:
            contact_details = "\n".join([f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}" for contact in self.contact_list])
            self.show_message(contact_details)

    def on_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_contact = self.contact_list[index]

            # Update entry widgets with selected contact details
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_contact.name)

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, selected_contact.phone_number)

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, selected_contact.email)

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, selected_contact.address)

    def load_contacts(self):
        try:
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                              (name TEXT, phone_number TEXT, email TEXT, address TEXT)''')

            cursor.execute("SELECT * FROM contacts")
            data = cursor.fetchall()

            self.contact_list.extend([Contact(*contact_data) for contact_data in data])

            conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            if conn:
                conn.close()

    def save_contacts(self):
        try:
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()

            # Clear existing data and insert new data
            cursor.execute("DELETE FROM contacts")
            cursor.executemany("INSERT INTO contacts VALUES (?, ?, ?, ?)", [(contact.name, contact.phone_number, contact.email, contact.address) for contact in self.contact_list])

            conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)
        finally:
            if conn:
                conn.close()

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()
