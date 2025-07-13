import datetime

def getUserInput():
    try:
        input_text = input("\nWhat have you Learned Today: ").strip()
        input_rating = int(input("Productivity rating(optional) (1-5):  ").strip())
        return [input_text, input_rating]
    except ValueError:
        print("\nPlease give valid Intger!\n")
        return getUserInput()
    except Exception as e:
        print("f{e}: Error here!")

def format_entry(learned, rating):
    time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    entry = f"\n=== {time} ===\n"
    entry += f"Task Completed: {learned}\n"
    
    if rating:
        entry += f"Productivity Ratinng: {rating}\n"
        
    entry += f"-" * 50
    
    return entry
    
    
def save_entry(entry):
    with open('jorunal.txt','a', encoding="utf-8") as f:
        f.write(entry + "\n")
        print("Logged Sucessfully")

def main():
    print("🗓️ Welcome to Your Daily Learning Journal")
    input = getUserInput()
    entry = format_entry(input[0],input[1])
    print(input[0])
    print(input[1])
    save_entry(entry)


if __name__ == "__main__":
    main()