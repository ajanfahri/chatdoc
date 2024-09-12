import google.generativeai as genai
import os

#genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
genai.configure(api_key="AIzaSyAzvDxDGeUfK1RYcU1co9gvQa2vEcptTiI")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)