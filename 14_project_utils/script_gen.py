import datetime

def main():
    print("\n" + '*' * 150)
    
    try:
        name = input("Enter the name: ").strip()
        age = int(input("Enter your age: "))
        city = input("Enter the city where you live: ").strip()
        proffession = input("Enter the profession: ").strip()
        hobbies = input("Enter your hobbies: ").strip()
    
        

        print('*' * 150)
        print("\n")

        summary = (
            f"Hi, I'm {name}, a {age}-year-old {proffession} based in {city}.\n"
            f"I absolutely enjoy my hobbies, which include {hobbies}.\n"
            f"Thank you!"
        )

        print(summary)
        print("\n")
        print('*' * 150)
        
        print(datetime.date.today().isoformat())
        
    except ValueError:
        print("\n[Error] Please Enter valid integer for your age")
        
    except Exception as e:
        print(f"Unexpected Error: {e}")
    

if __name__ == "__main__":
    main()