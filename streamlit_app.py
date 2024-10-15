import streamlit as st
import requests

# Streamlit UI
st.title('Tally XML to xlsx Converter')
st.write('Upload your Tally XML file and convert it to xlsx (filtering only "Receipt" type vouchers).')

# File uploader
uploaded_file = st.file_uploader("Choose a Tally XML file", type="xml")

# Convert button
if uploaded_file is not None:
    # Convert the file
    files = {'file': uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/convert-xml-to-xlsx/", files=files)
    
    if response.status_code == 200:
        st.download_button(label="Download xlsx", data=response.content, file_name="output.xlsx", mime="text/xlsx")
    else:
        st.write("Error in conversion.")
