import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x600")

        # Background Color
        self.root.configure(bg="lightblue")

        # Notebook Tabs
        self.tabControl = ttk.Notebook(root)
        self.list_tab = tk.Frame(self.tabControl, bg="lightblue")
        self.chat_tab = tk.Frame(self.tabControl, bg="lightgreen")
        self.call_tab = tk.Frame(self.tabControl, bg="lightyellow")
        self.note_tab = tk.Frame(self.tabControl, bg="lightgrey")
        self.about_tab = tk.Frame(self.tabControl, bg="lightpink")

        self.tabControl.add(self.list_tab, text='List')
        self.tabControl.add(self.chat_tab, text='Chat')
        self.tabControl.add(self.call_tab, text='Call')
        self.tabControl.add(self.note_tab, text='Note')
        self.tabControl.add(self.about_tab, text='About')
        self.tabControl.pack(expand=1, fill="both")

        self.contacts = []  # List to hold all contacts

        # Setting up Tabs
        self.setup_list_tab()
        self.setup_chat_tab()
        self.setup_call_tab()
        self.setup_note_tab()
        self.setup_about_tab()

    def setup_list_tab(self):
        """Setup for the List tab to show all contacts and manage them."""
        ttk.Label(self.list_tab, text="Contacts", background="lightblue", font=("Arial", 14)).pack(pady=5)

        self.contact_listbox = tk.Listbox(self.list_tab, width=40, height=15, font=("Arial", 12))
        self.contact_listbox.pack(pady=5)
        self.contact_listbox.bind("<<ListboxSelect>>", lambda event: self.show_contact_details())

        # Buttons
        button_frame = tk.Frame(self.list_tab, background="lightblue")
        button_frame.pack(pady=5)
        tk.Button(button_frame, text="Add", command=lambda: self.add_contact()).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit", command=self.edit_contact).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete", command=self.delete_contact).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Search", command=self.search_contact).grid(row=0, column=3, padx=5)

    def setup_chat_tab(self):
        """Setup for the Chat tab to allow communication options."""
        ttk.Label(self.chat_tab, text="Chat Options", background="lightgreen", font=("Arial", 14)).pack(pady=10)
        self.chat_frame = tk.Frame(self.chat_tab, background="lightgreen")
        self.chat_frame.pack(pady=10)

        self.chat_option = tk.StringVar(value="WhatsApp")
        tk.Radiobutton(self.chat_tab, text="WhatsApp", variable=self.chat_option, value="WhatsApp", background="lightgreen").pack()
        tk.Radiobutton(self.chat_tab, text="Email", variable=self.chat_option, value="Email", background="lightgreen").pack()

    def setup_call_tab(self):
        """Setup for the Call tab to allow call options."""
        ttk.Label(self.call_tab, text="Call Options", background="lightyellow", font=("Arial", 14)).pack(pady=10)
        self.call_frame = tk.Frame(self.call_tab, background="lightyellow")
        self.call_frame.pack(pady=10)

        self.call_option = tk.StringVar(value="WhatsApp")
        tk.Radiobutton(self.call_tab, text="WhatsApp", variable=self.call_option, value="WhatsApp", background="lightyellow").pack()
        tk.Radiobutton(self.call_tab, text="Google Duo", variable=self.call_option, value="Google Duo", background="lightyellow").pack()

    def setup_note_tab(self):
        """Setup for the Note tab to allow notes for each contact."""
        ttk.Label(self.note_tab, text="Notes", background="lightgrey", font=("Arial", 14)).pack(pady=5)
        self.note_text = tk.Text(self.note_tab, width=40, height=10)
        self.note_text.pack(pady=5)

    def setup_about_tab(self):
        """Setup for the About tab to describe the app."""
        about_text = (
            "Contact Manager App\n"
            "====================\n"
            "This is a simple contact manager app built with Python and Tkinter.\n"
            "It allows you to manage your contacts, including adding, editing, and deleting contacts.\n"
            "You can also search for contacts and view their details.\n"
            "Additionally, you can use the chat and call tabs to communicate with your contacts.\n"
            "The note tab allows you to add notes for each contact.\n"
        )
        ttk.Label(self.about_tab, text=about_text, background="lightpink", font=("Arial", 12)).pack(pady=10)

    def add_contact(self):
        """Add a new contact."""
        self.create_contact_window("Add Contact")

    def edit_contact(self):
        """Edit an existing contact."""
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.create_contact_window("Edit Contact", selected_index[0])
        else:
            messagebox.showerror("Error", "Please select a contact to edit.")

    def delete_contact(self):
        """Delete a contact."""
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def search_contact(self):
        """Search for a contact."""
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number")
        if search_term:
            for i, contact in enumerate(self.contacts):
                if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                    self.contact_listbox.select_set(i)
                    self.contact_listbox.see(i)
                    break
            else:
                messagebox.showinfo("Not Found", "Contact not found.")

    def show_contact_details(self):
        """Show details of a selected contact."""
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            details = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}"
            messagebox.showinfo("Contact Details", details)

    def create_contact_window(self, title, index=None):
        """Create a window to add or edit a contact."""
        window = tk.Toplevel(self.root)
        window.title(title)

        tk.Label(window, text="Name").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(window, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(window, text="Phone").grid(row=1, column=0, padx=5, pady=5)
        phone_entry = tk.Entry(window, width=30)
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Email").grid(row=2, column=0, padx=5, pady=5)
        email_entry = tk.Entry(window, width=30)
        email_entry.grid(row=2, column=1, padx=5, pady=5)

        if index is not None:
            contact = self.contacts[index]
            name_entry.insert(0, contact["name"])
            phone_entry.insert(0, contact["phone"])
            email_entry.insert(0, contact["email"])

        def save_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            if index is not None:
                self.contacts[index] = {"name": name, "phone": phone, "email": email}
            else:
                self.contacts.append({"name": name, "phone": phone, "email": email})
            self.contact_listbox.insert(tk.END, name)
            window.destroy()

        tk.Button(window, text="Save", command=save_contact).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
