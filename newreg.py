from file_checker import load_data, save_data
from secure_helper import hash_password
from strength_checker import prompt_password

def register_user():
    data = load_data()

    username = input("Choose a username: ")
    if username in data:
        print("⚠️ Username already exists. Try logging in.")
        return

    while True:
        password = prompt_password()
        if password:
            break
        else:
            print("❌ Registration cancelled.")
            return

    hashed_password = hash_password(password)

    print("\n🔐 Security Question: What was your dream job as a child?")
    answer = input("Enter your answer: ").strip().lower()
    hashed_answer = hash_password(answer)

    data[username] = {
        "password": hashed_password,
        "security_answer": hashed_answer,
        "vault": {}
    }

    save_data(data)
    print("✅ Registration successful! You can now log in.")
