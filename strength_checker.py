import string

def check_password_strength(pw):
    length = len(pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in string.punctuation for c in pw)

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    if score <= 2: return "Weak"
    if score <= 4: return "Medium"
    return "Strong"

def prompt_password():
    print("\nPassword must be 8+ chars, mix of uppercase, lowercase, digits & symbols.")
    while True:
        password = input("Enter password: ").strip()
        strength = check_password_strength(password)

        if strength == "Strong":
            confirm = input("Confirm password: ").strip()
            if confirm != password:
                print("❌ Passwords do not match. Try again.")
                continue
            return password
        elif strength == "Medium":
            print("⚠️ Password strength: Medium. Please try again.")
        else:
            print("⚠️ Password strength: Weak. Please try again.")

        retry = input("Do you want to try again? (yes to retry, no to go back): ").lower().strip()
        if retry != "yes":
            return None
