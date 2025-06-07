
# 🔐 Secure CLI Password Manager

A fully featured, secure, multi-user Command-Line Password Manager written in Python.
Built with real-world security practices in mind, it supports password encryption, recovery, clipboard copying, and more.

---

## ✨ Features

* ✅ Multi-user login and registration
* 🔐 Master password hashing (bcrypt)
* 🧠 Password recovery using security questions
* 🔄 Vault encryption using Fernet (key derived from master password)
* ➕ Add new password entries (manual or generated)
* 📋 Copy password to clipboard (with paste confirmation)
* 🔍 Search vault by site name
* 📝 Update site password or username/email
* 🗑️ Delete stored credentials
* 🔐 Change master password securely
* 📁 Modular structure: clean, readable, and extendable

---

## 🔧 Technologies Used

* Python 3
* **bcrypt** – master password hashing
* **cryptography** – Fernet symmetric encryption
* **pyperclip** – copy passwords to clipboard
* **json** – data storage in `user_data.json`

---

## 🛠️ Project Structure

```
password_manager/
├── main.py               # Entry point CLI  
├── login.py              # Handles login and vault functionality  
├── newreg.py             # Handles new user registration  
├── file_checker.py       # JSON read/write utilities  
├── passgenerator.py      # Random password generator  
├── strength_checker.py   # Validates password strength  
├── secure_helper.py      # Hashing and encryption helpers  
└── user_data.json        # (auto-created; ignored in .gitignore)  
```

---

## 🚀 How to Run

1. **Install dependencies**

   ```bash
   pip install bcrypt cryptography pyperclip
   ```

2. **Run the program**

   ```bash
   python main.py
   ```

---

## 📁 Sample Credentials (Test Only)

* **Username**: `testuser`
* **Password**: `Test@123`
* **Security Answer**: `astronaut`

---

## 📌 Notes

* 🔐 All site passwords are encrypted and stored in JSON
* 🧠 Master passwords are hashed — not reversible or readable
* 📂 The `user_data.json` file is excluded from Git to protect real data

---



## 📄 License

**MIT License**
Built by **Amritpal Singh** with ❤️ and a whole lot of `try + except`.
**Internship-ready project 🚀**


