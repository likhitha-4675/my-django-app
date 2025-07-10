import requests

# Replace 1 with the ID of the student you want to delete
student_id = 1

url = f"http://localhost:5000/students/2"
response = requests.delete(url)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response:", response.json())
