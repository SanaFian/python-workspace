contacts = []


def show_menu():
    """Display the main menu to the user"""
    print("\n" + "=" * 35)
    print("      📖 Smart Contact Book")
    print("=" * 35)
    print("1. ➕ Add new contact")
    print("2. 📋 Show all contacts")
    print("3. 🔍 Search contact by name")
    print("4. ❌ Delete contact")
    print("5. 🚪 Exit")
    print("=" * 35)


def add_contact():
    """Get input and add a new contact to the list"""
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # Basic validation
    if not name or not phone:
        print("⚠️ Error: Name and Phone are required!")
        return

    # Check for duplicate numbers
    for contact in contacts:
        if contact["phone"] == phone:
            print(f"⚠️ A contact with phone {phone} already exists ({contact['name']})!")
            return

    # Create dictionary for the new contact
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "Not provided"
    }

    # Append to the list
    contacts.append(new_contact)
    print(f"✅ Contact '{name}' added successfully.")


def list_contacts():
    """Display all stored contacts"""
    print("\n--- Contact List ---")
    if not contacts:
        print("📭 Phonebook is empty!")
        return

    # Using enumerate for nice row numbering
    for index, contact in enumerate(contacts, start=1):
        print(f"[{index}] Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")


def search_contact():
    """Search for a contact (Case-insensitive)"""
    print("\n--- Search Contact ---")
    query = input("Enter the name to search: ").strip().lower()

    if not query:
        print("⚠️ Input cannot be empty!")
        return

    found_contacts = []
    for contact in contacts:
        if query in contact["name"].lower():
            found_contacts.append(contact)

    if found_contacts:
        print(f"🎯 Found {len(found_contacts)} result(s):")
        for contact in found_contacts:
            print(f"👉 Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
    else:
        print("❌ No contact found with that name.")


def delete_contact():
    """Delete a contact based on exact name"""
    print("\n--- Delete Contact ---")
    target_name = input("Enter the exact name to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == target_name:
            contacts.remove(contact)
            print(f"🗑️ Contact '{contact['name']}' deleted successfully.")
            return

    print("❌ No contact found with this name.")


def main():
    """Main loop"""
    while True:
        show_menu()
        choice = input("Please select an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n👋 Goodbye! Have a great day.")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
