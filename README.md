# Uploader
A python script to Process Text Files with Python Dictionaries and Upload to Running Web Service
The script can be called using the ./run.py command after enabling execute permissions. It follows the structure:
List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.

Uses os.listdir() method for this, which returns a list of all files and directories in the specified path.

It now has a list that contains all of the feedback files from the path /data/feedback. It traverses over each file and, from the contents of these text files, creates a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.

Now, we have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.

We use the Python requests module to post the dictionary to the company's website. Using the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.

To make sure an error message isn't returned. We print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.

