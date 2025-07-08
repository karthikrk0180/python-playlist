from pymongo import MongoClient
from bson import ObjectId

# Use correct password and URL encoding if needed
client = MongoClient("mongodb+srv://user:password@nexract.2v54olj.mongodb.net/", tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video = {"name": name, "time": time}
    result = video_collection.insert_one(video)
    print(f"✅ Video added with ID: {result.inserted_id}")

def list_videos():
    videos = video_collection.find()
    print("\n📺 List of Videos:")
    for video in videos:
        print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")

def update_video(video_id, name, time):
    try:
        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": {"name": name, "time": time}}
        )
        if result.modified_count:
            print("✅ Video updated successfully.")
        else:
            print("⚠️ No video found with the given ID.")
    except Exception as e:
        print(f"❌ Error updating video: {e}")

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("✅ Video deleted successfully.")
        else:
            print("⚠️ No video found with the given ID.")
    except Exception as e:
        print(f"❌ Error deleting video: {e}")

def main():
    while True:
        print("\n🎬 Youtube Manager APP")
        print("1. List all Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit the APP")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the name of video: ")
            time = input("Enter the time of video: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated name: ")
            time = input("Enter the updated time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting the APP. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
