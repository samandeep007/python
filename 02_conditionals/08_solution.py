# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

def checkPasswordStrength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) <= 10:
        return "Medium"
    else: 
        return "Strong"

password = input("Enter your password: ")
print("Your password is " + checkPasswordStrength(password))