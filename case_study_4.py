password = "Maneesh@123"
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "@#$%!&*"

if len(password) >= 8:
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True
        elif ch >= '0' and ch <= '9':
            has_digit = True
        elif ch in special_chars:
            has_special = True

print(f"Password: {password}")
if has_upper and has_lower and has_digit and has_special:
    print("Password Valid - Strong Password")
else:
    print("Password Invalid - Must have Upper, Lower, Digit, Special @#$%")
    print(f"Upper:{has_upper} Lower:{has_lower} Digit:{has_digit} Special:{has_special}")
