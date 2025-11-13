import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        # Handle HTTP errors
        if response.status_code != 200:
            print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
            return

        users = response.json()

        # Handle empty response
        if not users:
            print("Error: No users found in the API response.")
            return

        print("\nAll Users:\n")

        for index, user in enumerate(users, start=1):
            print(f"User {index}:")
            print(f"Name: {user.get('name')}")
            print(f"Username: {user.get('username')}")
            print(f"Email: {user.get('email')}")
            print(f"City: {user.get('address', {}).get('city')}")
            print("------------------------")

        # Optional Bonus: City starting with 'S'
        print("\nUsers whose city starts with 'S':\n")

        for user in users:
            city = user.get("address", {}).get("city", "")
            if city.startswith("S"):
                print(f"Name: {user.get('name')}")
                print(f"Username: {user.get('username')}")
                print(f"Email: {user.get('email')}")
                print(f"City: {city}")
                print("------------------------")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    fetch_users()
