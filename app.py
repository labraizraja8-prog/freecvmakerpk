import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄")
st.title("📄 Free CV Maker - AI Wala")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

name = st.text_input("1. Pura Naam")
phone = st.text_input("2. WhatsApp Number")
edu = st.text_input("3. Taleem")
exp = st.text_input("4. Tajurba")
skills = st.text_input("5. Hunar")

if st.button("Mera CV Banao ✨"):
    if name == "":
        st.error("Naam likho")
    else:
        with st.spinner("AI CV bana raha hai..."):
            prompt = f"Ek professional CV banao. Name: {name}, Education: {edu}, Experience: {exp}, Skills: {skills}. Achhi English me objective bhi likho."
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            cv = response.choices[0].message.content

        st.success("CV Ready Hai!")
        st.text_area("Yahan se Copy Karo", cv, height=400)
        st.download_button("📥 Download Karo", cv, file_name=f"{name}_CV.txt")
