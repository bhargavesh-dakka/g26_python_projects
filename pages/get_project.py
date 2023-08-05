import deta
import streamlit as st
Key = "d0qzwyt1lmi_UCUcbRxy93KBG7jHv5hcQbCWQKB57paF"
obj = deta.Deta(Key)
db = obj.Base("G26_Python_Projects")

st.write(st.session_state["Project_details"])

name = st.text_input("Enter your name : ")
project_number = st.number_input("Enter the project number : ",1, 33)

if st.button("Submit"):
    st.success("Project selected successfully.")

        
