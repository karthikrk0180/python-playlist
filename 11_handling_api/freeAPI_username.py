import requests
import json

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch API ")
    

def main():
    try:
        username,  country = fetch_random_user_freeapi()
        print(f"Username: {username} ,\n Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()