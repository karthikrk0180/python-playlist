import string
import random
import getpass

def check_suggest(input_password):
    issues = []
    
    if len(input_password) < 8:
        issues.append("Password length must be 8 characters long.")
    
    if not any(c.islower() for c in input_password):
        issues.append("Password must atleast one lowercase letter")
        
    if not any(c.isupper() for c in input_password):
        issues.append("Password must atleast one uppercase letter")
        
    if not any(c.isdigit() for c in input_password):
        issues.append("Password must atleast one digit")

    if not any(c in string.punctuation for c in input_password):
        issues.append("Password must contain at least one special character.")
        
    if not issues:
        print("\n Your Password is Strong")
    else:
        print("\n Your Password is Weak!")
        for issue in issues:
            print(f"- {issue}")
        print("\n Suggesting better Password\n")
        suggest_password()
        
        
    
def suggest_password(length=7):
    chars = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"\n The suggested Strong Password is {password} \n")

def main():
    print("************************ Password Strength Checker and Suggestion Tool ***************************\n")
    
    while True:
        print("1. Check password strength and suggest Better.\n")
        print("2. Suggest Strong Password\n")
        print("3. Exit the Application\n")
        
        choice = input("Enter the Choice: ").strip()
        
        match choice:
            case '1':
                input_password = getpass.getpass("Enter the Password: ").strip()
                check_suggest(input_password)
                break
            case '2':
                suggest_password()
                break
            case '3':
                print("Thank You for using the Application! Exited\n")
                break
            case _:
                print("Invalid Choice NIGGAAAA!")            
            
        
        

if __name__ == "__main__":
    main()