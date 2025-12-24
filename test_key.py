import os
from dotenv import load_dotenv

load_dotenv() # Load the .env file

key = os.getenv("GOOGLE_API_KEY")

if key:
    print("SUCCESS: Key found!")
    print(f"Key starts with: {key[:5]}...")
else:
    print("ERROR: Key is None. Check your .env file name and location.")