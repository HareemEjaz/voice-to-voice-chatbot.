import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(f"{fp.name}.mp3")
        os.system(f"start {fp.name}.mp3")  # On Windows, use "start". Change for macOS/Linux.

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
        st.write("Recognizing...")
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            st.write("Could not understand audio")
            return None
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return None

# Streamlit UI
st.title("Voice to Voice Chatbot")

if st.button("Start Chat"):
    user_input = recognize_speech()
    if user_input:
        st.write(f"You said: {user_input}")
        
        # Simple bot response (replace with your chatbot logic)
        bot_response = f"You said: {user_input}. This is a placeholder response."
        
        st.write(f"Bot: {bot_response}")
        text_to_speech(bot_response)
