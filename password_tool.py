import re
import random
import string

def check_password_strength(password):
    # Base criteria scoring
    score = 0
    remarks = ""
    
    # Length check
    if len(password) >= 8:
        score += 1
    # Number check
    if re.search(r"\d", password):
        score += 1
    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    # Special character check
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>_]", password):
        score += 1

    # Scoring assessment
    if score <= 1:
        remarks = "Weak 🔴"
    elif score == 2 or score == 3:
        remarks = "Medium 🟡"
    elif score == 4:
        remarks = "Strong 🟢"
        
    return remarks

def generate_secure_password(length=12):
    # Saare characters ka pool banana
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    # Randomly select karna
    secure_password = "".join(random.choice(all_characters) for i in range(length))
    return secure_password

if __name__ == "__main__":
    print("=== Password Security Tool ===")
    
    # 1. Test Strength Checker
    user_pass = input("[?] Enter a password to test: ")
    strength = check_password_strength(user_pass)
    print(f"[+] Password Strength: {strength}\n")
    
    # 2. Test Generator
    print("[*] Generating a secure replacement password...")
    new_pass = generate_secure_password()
    print(f"[+] Suggested Secure Password: {new_pass}")
