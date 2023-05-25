import os
import requests
# Get the path to the directory
directory_path = "/data/feedback/"
web_service_url = "http://34.68.218.230/feedback/"
# Define a function to read the feedback from a file
def read_feedback(file_path):
    with open(file_path, 'r') as feedtxt:
        lines = feedtxt.readlines()
    title = lines[0].strip()
    name = lines[1].strip()
    date = lines[2].strip()
    feedback = lines[3].strip()
    return {
        "title": title,
        "name": name,
        "date": date,
        "feedback": feedback
    }

# List all files in the directory
files = os.listdir(directory_path)

# Create a dictionary to store the feedback
feedback_dictionary = {}

# Iterate over the files. run your code completely in the iteration
for file in files:

    # Read the feedback from the file. (/data/feedback/007.txt)
    feedback = read_feedback('{}/{}'.format(directory_path,file))

    # Add the feedback to the dictionary
    feedback_dictionary = feedback

    # Send a POST request to the web service for each file
    response = requests.post(web_service_url, json = feedback_dictionary)
    
    # Check the response status code
    if not response.ok:
        raise Exception("Post failed with status code {} | file {}".format(response.status_code, file))
    print("feedback added")




