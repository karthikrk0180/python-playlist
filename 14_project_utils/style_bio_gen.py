import textwrap
import re

def get_user_input():
    
    try:
        name = input("Enter the Name: ").strip()
        proffession = input("Enter the proffession: ").strip() 
        goal = input("Enter the Goal of life: ").strip()
        emoji = input("Enter your fav emoji (optional): ").strip()
        link = input("Enter your social media: ").strip()
        
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return {
        "name": name,
        "proffession": proffession,
        "goal": goal,
        "emoji": emoji,
        "link": link
    }
    
def generate_bio(**kwargs):
    bio = textwrap.dedent (f"""
        Hi, I'm {kwargs.get('name')}, a passionate {kwargs.get('proffession')}.
        My ultimate goal in life is: {kwargs.get("goal")}.
    """)
    
    if kwargs.get('emoji'):
        bio += f"Here’s my favorite emoji: {kwargs.get('emoji')}\n"
        
    if kwargs.get('link'):
        bio += f"Connect with me Here: {kwargs.get('link')}"
        
    
    return bio.strip()

def save_data(bio, name):
    safe_name = re.sub(r'\W+', '_', name.strip().lower())
    file_name = f"{safe_name}_bio.txt"
    with open(file_name, 'w', encoding ='utf-8') as f:
        f.write(bio)
    
    

def main():
    
    user_data = get_user_input()
    bio = generate_bio(**user_data)
    
    print("\n📄 Generated Bio:\n")
    print(bio)
    
    print("\n")
    
    while True:
    
        choice = input("Do you want to save this bio in Text file (y/n): ")

        if choice == 'y':
            save_data(bio, user_data['name'])
            print("Your bio is saved in file! ✅")
            break
        elif choice == 'n':
            print("Okay not Saving! 💔")
            break
        else:
            print("Please enter valid input (y/n)")
    
    
    
    
    
    

if __name__ == "__main__":
    main()
