import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test =  json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Video:  {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)
    
def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new Video Name")
        time = input("Enter the new Video Duration")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index Seected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a youtube Video")
        print("5. Exit the Application")
        choice = input("Enter the choice ✨: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
# if there is some function whose name is main in this file then please run main function it signifies
if __name__ == "__main__":
    main()
        
    
    