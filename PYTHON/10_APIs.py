import requests

'''
# Basic GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code) # 200 means OK
print(response.text) # Shows raw response text

# Working with JSON data
data = response.json() # Converts JSON text to Python dictionary
print(data)
print("Title:", data["title"])


# Fetching multiple posts
response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
  posts = response.json()
  for post in posts[:5]:
    print(f"{post['id']}. {post['title']}")
else:
  print("Error fetching data:", response.status_code)

  
# POST Request (Send Data)
new_post = {
  "title": "My new post",
  "body": "Learning APIs with Python!",
  "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

print("Status:", response.status_code) # 201 means post successful
print("Response:", response.json())


# Handling Errors Gracefully
try:
  response = requests.get("https://jsonplaceholder.typicode.com/invalid")
  response.raise_for_status() # raise error for bad responses (4xx or 5xx)
except requests.exceptions.RequestException as e:
  print("Error:", e)

# Example project: Simple API Data Viewer
def get_random_quote():
  url = "https://api.quotable.io/random"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    print(f"\"{data["content"]}\" - {data["author"]}") 
  else:
    print("Unable to fetch quote")

get_random_quote()

# Exercise 1
def fetch_joke():
  url = "https://official-joke-api.appspot.com/random_joke"
  joke_request = requests.get(url)
  if joke_request.status_code == 200:
    joke = joke_request.json()
    print(joke["setup"],"\n", joke["punchline"])
  else:
    print("Could not fetch the joke")

fetch_joke()


try:
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  response.raise_for_status() # raises error for bad responses (4xx or 5xx)
except requests.exceptions.RequestException as e:
  print("Error: ", e)
'''