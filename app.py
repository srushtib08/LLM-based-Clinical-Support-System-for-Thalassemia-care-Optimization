import streamlit as st
import requests

st.title("ThalCare AI – Thalassemia Support")
query = st.text_area("Ask a question or describe a symptom:")
if st.button("Submit"):
    response = requests.post("http://localhost:8000/ask", json={"patient_query": query})
    st.write("### Response:")
    st.write(response.json()["response"])
