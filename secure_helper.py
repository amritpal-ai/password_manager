import bcrypt
from cryptography.fernet import Fernet
import base64
import hashlib

# --- 1. Hashing for master password ---

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# --- 2. Encryption using key derived from password ---

def derive_key_from_password(password):
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def get_fernet(password):
    key = derive_key_from_password(password)
    return Fernet(key)

def encrypt_data(plain_text, fernet):
    return fernet.encrypt(plain_text.encode()).decode()

def decrypt_data(encrypted_text, fernet):
    return fernet.decrypt(encrypted_text.encode()).decode()
