from google import genai

client = genai.Client(api_key="AIzaSyAfNXLXPIYLCA2POzUBVz-R7oE62EottL4")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello"
)

print(response.text)