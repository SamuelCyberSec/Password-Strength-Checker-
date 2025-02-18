import re

def check_password_strength(password):
    """
    Checks the strength of a password based on predefined criteria.
    """
    # Define strength criteria
    min_length = 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[@$!%*?&]", password))
    
    # Calculate strength score
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    # Assess password strength
    if len(password) < min_length:
        return "Weak: Password should be at least 8 characters long."
    elif score == 1:
        return "Weak: Try adding uppercase letters, numbers, and special characters."
    elif score == 2:
        return "Moderate: Consider adding more variety to strengthen your password."
    elif score >= 3:
        return "Strong: Your password is well-formed!"
    
# Get user input and check password strength
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(check_password_strength(user_password))
