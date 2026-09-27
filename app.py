import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄")
st.title("📄 Free CV Maker - AI Wala")

# CV Image Ka Direct Link
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"

# Sidebar mein Sample CV aur Contact Details
with st.sidebar:
    st.header("📌 Sample CV")
    st.write("Here is a sample professional CV:")
    st.image(SAMPLE_CV_URL, caption="Sample Professional CV", use_container_width=True)

    st.markdown("---")
    st.success("💼 To get your CV made:\n📞 0310-9018979")
    st.write("💰 Price: Rs. 300 per CV")
    st.markdown("---")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Main Form
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

        st.success("CV Ready Hai! 🎉")
        st.text_area("Yahan se Copy Karo", cv, height=400)
        st.download_button("📥 Download Karo", cv, file_name=f"{name}_CV.txt")
        
        st.warning(f"⚠️ Professional editing chahiye? WhatsApp: 0310-9018979")
