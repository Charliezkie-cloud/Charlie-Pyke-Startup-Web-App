import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCTOF13iWWaldpg1zAjGmoSOlpmL-RvM9U")

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Look at this sequence of three shapes. What shape should come as the fourth shape? Explain your reasoning with detailed descriptions of the first shapes.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The sequence is a triangle, a square, a pentagon. The pattern is to increase the number of sides by one with each shape. So, the fourth shape should be a hexagon, which has six sides. \n",
      ],
    },
  ]
)

response = chat_session.send_message("Hi, how are you?")

print(chat_session.history)