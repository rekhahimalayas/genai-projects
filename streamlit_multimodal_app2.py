import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO


load_dotenv()


client = genai.Client()
st.title("AI Image Caption Generator")


uploaded_image = st.file_uploader("Upload an image for caption generation", type=["png", "jpg", "jpeg"])


if uploaded_image:
   image = Image.open(uploaded_image)
   st.image(image, caption="Uploaded Image")


   if st.button("Generate Caption"):
       try:
           with st.spinner("Generating caption..."):
               response = client.models.generate_content(
               model="gemini-2.0-flash",
               contents=["What is this image?", image])
               st.subheader("Generated Caption:")
               st.write(response.text)
       except Exception as e:
           st.error("Error generating caption")


st.title("AI YouTube Video Summarizer")
youtube_url = st.text_input("Enter YouTube Video URL")


if st.button("Summarize Video"):
   if not youtube_url:
       st.warning("No YouTube URL Present!")
   else:
       try:
           with st.spinner("Generating summary..."):
               response = client.models.generate_content(
                   model='models/gemini-2.0-flash',
                   contents=types.Content(
                       parts=[
                           types.Part(text='Can you summarize this video?'),
                           types.Part(
                               file_data=types.FileData(file_uri=youtube_url)
                           )
                       ]
                   )
               )
           st.subheader("Video Summary")
           st.write(response.text)
       except Exception as e:
           st.error("Error generating summary")