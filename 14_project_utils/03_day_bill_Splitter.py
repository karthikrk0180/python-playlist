def get_user_count():
    print("*" * 150)
    print("\nBill Splitter\n")
    
    try:
        user_count = int(input("Enter the number of people you want to divide: "))
        return user_count
    except ValueError:
        print("\n Error Please enter a valid integer number")
    except Exception as e:
        print(f"\n error : {e} ")   
    
    return None

def get_user_names(num_persons):
    users = []
    for i in range(num_persons):
        while True:
            name = input(f"Enter the name of {i+1} person: ").strip()
            if name.replace(" ","").isalpha():
                users.append(name)
                break
            else:
                print("Invalid name! Please enter only letters")     
    return users

def get_bill_amount():
    try:
        amount = float(input("\nEnter the Amount: "))
        return amount
    except ValueError:
        print("Please enter a valid float")
    except Exception as e:
        print(f"Error: {e}")
        
    return None

def get_per_share(amount, num_persons):
    per_share = round(amount / num_persons)
    return per_share
    
def print_summary(persons, amount, per_share):
    print("\n" + '*' * 150)
    print(f"Total Bill Amount: {amount}")
    print(f"Each person Share is {per_share}")
    print("\n Breakdown:- ")
    
    for name in persons:
        print(f" {name} owes {per_share}")
    print("*" * 150)



def main():
    
    while True:
    
        num_persons = get_user_count()
        
        if num_persons is None or num_persons <= 0:
            print("\nNothing here, no friends to split. Sad life.")
            break
        
        print(f"\nSo, cool! There are {num_persons} people in the friends group to be split.\n")

        persons = get_user_names(num_persons)
        # print(persons)
        
        amount = get_bill_amount()
        # print(amount)
        
        per_share = get_per_share(amount, num_persons)
        # print(per_share)
        
        print_summary(persons, amount, per_share)
        break
        
    

if __name__ == "__main__":
    main()