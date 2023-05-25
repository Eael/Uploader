import os
import requests

# Specify the web service URL
web_service_url = "http://35.225.95.53/feedback/"

# Get the list of files in the specified directory
files = os.listdir(".")

# Iterate over each file
for file in files:
    # Read the contents of the file
    with open(file, "r") as f:
        content = f.read()

    # Extract the title, name, date, and feedback from the file contents
    title, name, date, feedback = content.split("\n")

    # Create a dictionary with the extracted information
    feedback_dict = {
        "title": title,
        "name": name,
        "date": date,
        "feedback": feedback
    }

    # Send a POST request to the web service for each file
    response = requests.post(web_service_url, json=feedback_dict)

    # Check the response status code
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))

    print("Feedback added!")
