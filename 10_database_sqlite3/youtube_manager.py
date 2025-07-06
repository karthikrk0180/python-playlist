import sqlite3

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute('SELECT * FROM videos')
    rows = cursor.fetchall()
    if not rows:
        print("\n No videos Found ")
    else:
        for row in rows:
            print(row)
            
            

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?,time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    con.commit()
    
def search_video(keyword):
    cursor.execute("SELECT * FROM videos WHERE name LIKE ?", (keyword,))
    rows = cursor.fetchall()
    if not rows:
        print("\n No videos Found ")
    else:
        for row in rows:
            print(row)
    

def main():
    
    with sqlite3.connect('youtube_videos.db') as con:
        cursor = con.cursor()
    
    while True:
        print("\n Youtube Manager with DB")
        print("1. List All videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Search the video")
        print("6. Exit the application")
        
        choice = input("Enter the Choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            if not name.strip():
                print("Name cant be empty")
                continue
            time = input("Enter the video time: ")
            if not time.strip():
                print("Cant be empty")
                continue
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update")
            if not video_id.isdigit():
                print("Invalid input")
                continue
            name = input("Enter the updated video name: ")
            if not name.strip():
                print("Invalid Input")
                continue
            time = input("Enter the updated video time: ")
            if not time.strip():
                print("Invalid time input")
                continue
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete")
            if not video_id.isdigit():
                print("Invalid id. Must be a number")
                continue
            delete_video(video_id)
        elif choice == '5':
            keyword = input("Enter the youtube video to search: ")
            if not keyword.strip():
                print("Invalid characters")
                continue
            search_video(keyword) 
        elif choice == '6':
            break
        else:
            print("Invalid Choice 💣 ")
            
    
                


if __name__ == "__main__":
    main()