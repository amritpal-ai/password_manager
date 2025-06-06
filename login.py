from file_checker import load_data, save_data
from passgenerator import generate_password
from strength_checker import prompt_password
from secure_helper import (
    hash_password,
    check_password,
    get_fernet,
    encrypt_data,
    decrypt_data
)
import pyperclip

def login_user():
    data = load_data()

    username = input("Enter username: ")
    if username not in data:
        print("❌ Username not found.")
        return

    while True:
        typed_password = input("Enter your password: ")
        stored_hash = data[username]["password"]

        if check_password(typed_password, stored_hash):
            print("✅ Login successful!")
            fernet = get_fernet(typed_password)
            break
        else:
            print("❌ Incorrect password.")
            forgot = input("Did you forget your password? (yes/no): ").strip().lower()

            if forgot == "yes":
                print("🔐 Security Question: What was your dream job as a child?")
                answer = input("Answer: ").strip()

                if check_password(answer, data[username]["security_answer"]):
                    while True:
                        new_pass = prompt_password()
                        if new_pass:
                            data[username]["password"] = hash_password(new_pass)
                            save_data(data)
                            print("✅ Password reset successful! Please log in again.\n")
                            return
                        else:
                            print("❌ Password reset cancelled.")
                            return
                else:
                    print("❌ Incorrect answer to security question.")
                    print("Returning to main menu for your safety.\n")
                    return
            else:
                print("🔁 Try logging in again.\n")

    # ======= Vault Menu =======
    while True:
        print("\n🔐 What would you like to do?")
        print("1. Add new password")
        print("2. View all saved passwords")
        print("3. Search for a password")
        print("4. Update site password")
        print("5. Update site username/email")
        print("6. Delete a saved password")
        print("7. Change master password")
        print("8. Logout")

        choice = input("Enter your choice: ")
        vault = data[username]["vault"]

        if choice == "1":
            site = input("Enter site name (e.g., gmail.com): ")

            if site in vault:
                confirm = input("Site already exists. Overwrite? (yes/no): ").lower()
                if confirm != "yes":
                    print("❌ Cancelled.")
                    continue

            site_user = input("Enter username/email for the site: ")

            while True:
                use_gen = input("Generate a secure password? (yes/no): ").lower().strip()

                if use_gen == "yes":
                    while True:
                        site_password = generate_password()
                        print(f"🔐 Generated password: {site_password}")

                        save_confirm = input("Do you want to save this password? (yes/no): ").strip().lower()
                        if save_confirm == "yes":
                            pyperclip.copy(site_password)
                            confirm_copy = input("Paste it here to confirm you copied it: ").strip()
                            if confirm_copy != site_password:
                                print("❌ Paste didn’t match. Try again.")
                                continue
                            break
                        else:
                            print("🔁 Okay, going back.")
                            break

                    if save_confirm == "yes":
                        break

                elif use_gen == "no":
                    site_password = prompt_password()
                    if site_password:
                        break
                else:
                    print("❌ Invalid input. Type yes or no.")

            vault[site] = {
                "username": site_user,
                "password": encrypt_data(site_password, fernet)
            }

            save_data(data)
            print(f"✅ Saved password for {site}.")

        elif choice == "2":
            if not vault:
                print("🔓 No passwords saved yet.")
            else:
                for site in vault:
                    print("Site:", site)
                    print("Username:", vault[site]["username"])
                    print("Password:", decrypt_data(vault[site]["password"], fernet))
                    print("-" * 20)

        elif choice == "3":
            site = input("Enter site name to search: ")
            if site in vault:
                print("Username:", vault[site]["username"])
                decrypted = decrypt_data(vault[site]["password"], fernet)
                print("Password:", decrypted)
                if input("Copy to clipboard? (yes/no): ").lower() == "yes":
                    pyperclip.copy(decrypted)
                    print("✅ Copied.")
            else:
                print("❌ Not found.")

        elif choice == "4":
            site = input("Enter site name to update password: ")
            if site in vault:
                while True:
                    use_gen = input("Generate a secure password? (yes/no): ").lower().strip()

                    if use_gen == "yes":
                        while True:
                            site_password = generate_password()
                            print(f"🔐 Generated password: {site_password}")

                            save_confirm = input("Do you want to save this password? (yes/no): ").strip().lower()
                            if save_confirm == "yes":
                                pyperclip.copy(site_password)
                                confirm_copy = input("Paste it here to confirm you copied it: ").strip()
                                if confirm_copy != site_password:
                                    print("❌ Paste didn’t match. Try again.")
                                    continue
                                break
                            else:
                                print("🔁 Okay, going back.")
                                break

                        if save_confirm == "yes":
                            vault[site]["password"] = encrypt_data(site_password, fernet)
                            save_data(data)
                            print("🔄 Password updated.")
                            break

                    elif use_gen == "no":
                        new_password = prompt_password()
                        if new_password:
                            vault[site]["password"] = encrypt_data(new_password, fernet)
                            save_data(data)
                            print("🔄 Password updated.")
                            break
                        else:
                            print("❌ Password update cancelled.")
                            break

                    else:
                        print("❌ Invalid input. Type yes or no.")
            else:
                print("❌ Site not found.")

        elif choice == "5":
            site = input("Enter site name to update username/email: ")
            if site in vault:
                new_user = input("Enter new username/email: ")
                vault[site]["username"] = new_user
                save_data(data)
                print("📝 Username updated.")
            else:
                print("❌ Site not found.")

        elif choice == "6":
            site = input("Enter site name to delete: ")
            if site in vault:
                confirm = input(f"Delete {site}? (yes/no): ").lower()
                if confirm == "yes":
                    del vault[site]
                    save_data(data)
                    print("🗑️ Deleted.")
            else:
                print("❌ Site not found.")

        elif choice == "7":
            current_pass = input("Enter current master password to confirm: ")
            if check_password(current_pass, data[username]["password"]):
                while True:
                    new_pass = prompt_password()
                    if new_pass:
                        data[username]["password"] = hash_password(new_pass)
                        save_data(data)
                        print("✅ Master password updated successfully.")
                        break
                    else:
                        print("❌ Master password not updated.")
                        break
            else:
                print("❌ Current password is incorrect.")

        elif choice == "8":
            print("🔒 Logged out.")
            return

        else:
            print("❌ Invalid option.")
