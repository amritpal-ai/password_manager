# 🔐 Secure CLI Password Manager

A fully featured, secure, multi-user **Command-Line Password Manager** written in Python. Built with real-world security practices in mind, it supports password encryption, recovery, clipboard copying, and more.

---

## ✨ Features

- ✅ **Multi-user login and registration**
- 🔐 **Master password hashing** (bcrypt)
- 🧠 **Password recovery using security questions**
- 🔄 **Vault encryption using Fernet** (key derived from master password)
- ➕ **Add new password entries** (manual or generated)
- 📋 **Copy password to clipboard** (with paste confirmation)
- 🔍 **Search vault by site name**
- 📝 **Update site password or username/email**
- 🗑️ **Delete stored credentials**
- 🔐 **Change master password securely**
- 📁 Modular structure: clean, readable, and extendable

---

## 🔧 Technologies Used

- Python 3
- `bcrypt` – master password hashing
- `cryptography` – Fernet symmetric encryption
- `pyperclip` – copy passwords to clipboard
- `json` – data storage in `user_data.json`

---

## 🛠️ Project Structure
