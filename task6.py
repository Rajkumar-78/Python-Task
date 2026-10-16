import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# GET: Fetch users
response = requests.get(f"{BASE_URL}/users")
users = response.json()

print(users[0]["name"], "Sincere@april.biz")

# POST: Create a post
data = {
    "title": "My Post",
    "body": "This is my post",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=data)
print(f"\nPOST: {response.status_code}, id:{response.json()['id']}")

# PUT: Update a post
put_response = requests.put(
    f"{BASE_URL}/posts/1",
    json={"title": "Updated Post", "body": "Updated", "userId": 1}
)

# PATCH: Partially update a post
patch_response = requests.patch(
    f"{BASE_URL}/posts/1",
    json={"title": "Patched Post"}
)

# DELETE: Delete a post
delete_response = requests.delete(f"{BASE_URL}/posts/1")

print(
    f"\nPUT: {put_response.status_code} | "
    f"PATCH: {patch_response.status_code} | "
    f"DELETE: {delete_response.status_code}"
)

# GET: Non-existing post
response = requests.get(f"{BASE_URL}/posts/9999")

if response.status_code == 404:
    print("GET /posts/9999 -> 404 Not found")

# Explain status codes
def explain_status(code):
    messages = {
        200: "OK - Request successful",
        201: "Created - Resource created successfully",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error"
    }
    return messages.get(code, "Unknown status code")