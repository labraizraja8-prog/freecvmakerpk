import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄")
st.title("📄 Free CV Maker - AI Wala")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Yahan labels English mein kar diye gaye hain
name = st.text_input("1. Full Name")
phone = st.text_input("2. WhatsApp Number")
edu = st.text_input("3. Education")
exp = st.text_input("4. Experience")
skills = st.text_input("5. Skills")

if st.button("Mera CV Banao ✨"):
    if name == "":
        st.error("Please enter your name")
    else:
        with st.spinner("AI is generating your CV..."):
            prompt = f"""
            You are an expert CV writer. Create a highly professional, ATS-friendly CV in ENGLISH ONLY.
            Do not use Hindi, Urdu, or any other language. Do not write any placeholder text.
            Use exactly the information provided below. 

            Name: {name}
            Phone: {phone}
            Education: {edu}
            Experience: {exp}
            Skills: {skills}

            Structure the CV with these exact sections:
            1. Professional Summary (Objective)
            2. Education
            3. Work Experience
            4. Skills

            Write it in a professional tone. Format it neatly with bold headings and bullet points.
            """
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "user", "content": prompt}]
            )
            cv = response.choices[0].message.content

        st.success("CV Ready Hai!")
        st.text_area("Yahan se Copy Karo", cv, height=400)
        st.download_button("📥 Download Karo", cv, file_name=f"{name}_CV.txt")
