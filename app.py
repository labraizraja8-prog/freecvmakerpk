import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄", layout="wide")

# 👇 YAHAN APNI LOGO IMAGE KA SAHI LINK DAALEIN (File ka naam check kar lena: .jpg ya .png)
LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"

# Sidebar
with st.sidebar:
    st.header("📌 Sample CV")
    st.image("https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg", use_container_width=True)
    
    st.markdown("---")
    st.write("💼 **To get your CV made:**")
    st.link_button("📞 WhatsApp: 0310-9018979", "https://wa.me/923109018979")
    st.write("💰 Price: Rs. 300 per CV")
    st.markdown("---")

# Main Area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Logo aur Title
    st.image(LOGO_URL, width=150)
    st.title("Free CV Maker - AI Wala")
    st.write("Get a professional, ATS-friendly CV in seconds.")
    
    st.markdown("---")

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    # Form
    with st.form("cv_form"):
        st.subheader("📝 Enter Your Details")
        col_a, col_b = st.columns(2)
        with col_a:
            name = st.text_input("1. Full Name")
            edu = st.text_input("3. Education")
            skills = st.text_input("5. Skills")
        with col_b:
            phone = st.text_input("2. WhatsApp Number")
            exp = st.text_input("4. Experience")
        
        submit_button = st.form_submit_button("Mera CV Banao ✨")

    if submit_button:
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
            
            st.info("⚠️ Professional editing chahiye? Click the WhatsApp button in the sidebar!")
