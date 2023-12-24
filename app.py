# Q&A Chatbot
# from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import requests


def get_public_ip():
    try:
        response = requests.get("https://httpbin.org/ip")
        ip = response.json()["origin"]
        # print(f"My public IP address is: {ip}")
        return f"my ip is: {ip}"
    except requests.RequestException as e:
        # print("Couldn't get the IP address:", e)
        return "couldnt find the ip"


# get_public_ip()


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones


def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text


##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")
st.subheader(get_public_ip())
# input = st.text_input("Input: ", key="input")


# submit = st.button("Ask the question")
with st.form(key="my_form"):
    # Add inputs here, for example:
    # username = st.text_input(label="Enter your name")
    input = st.text_input("Input: ", key="input")
    # password = st.text_input(label="Enter your password", type="password")

    # Every form must have a submit button.
    submit_button = st.form_submit_button(label="Submit")

## If ask button is clicked

if submit_button:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
