import openai, os

openai.api_key_path = 'apikey.txt'

# Create a directory to store the text files
if not os.path.exists("text/"):
    os.mkdir("text/")
    