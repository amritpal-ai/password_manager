from login import login_user
from newreg import register_user

def main():
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
