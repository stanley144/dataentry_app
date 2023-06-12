# Import necessary libraries
import streamlit as st
import openai

# Set up OpenAI API
openai.api_key = 'your_openai_key'

# Title of the app
st.title("D.E.B.")
st.header("Data Entry Backup")


st.subheader("1. Industry Classification")

# Input text box for the user to enter a question
input_text = st.text_input("Enter the company name")

st.divider()

# When the user enters a question and hits Enter
if input_text:

    st.write(f"Current: Paste the below to [ChatGPT Plus with Bing Search](https://chat.openai.com/?model=gpt-4-browsing):")
    st.write("")

    st.write(f"""
        *For the company '{input_text}', try to select the closest industry based on NAICS codes.
        Give up to 3 best matches and add confidence to each selection* """)
    st.write("")

    st.write("Future: auto-pull results using ChatGPT Plus with API")

    # for later
    # # Use the OpenAI API to get a response from GPT-3
    # response = openai.ChatCompletion.create(
    #   model="gpt-3.5-turbo",  # Use the latest version of GPT-3
    #   messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": input_text}
    #     ]
    # )

    # # Display the response from GPT-3
    # st.write(response['choices'][0]['message']['content'])

st.subheader("2. Additional Locations")

st.write(f"TBD") 