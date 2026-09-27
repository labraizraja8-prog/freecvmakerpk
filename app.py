import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄", layout="wide")

# 👇 Professional Dark Theme CSS
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    /* Headings */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 700;
    }
    /* Input Fields */
    .stTextInput>div>div>input {
        background-color: #1e293b;
        color: #ffffff;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 10px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
    }
    /* Buttons */
    .stButton>button, .stFormSubmitButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover {
        background-color: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #020617;
        border-right: 1px solid #1e293b;
    }
    /* Links */
    a {
        color: #60a5fa !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    /* Alert Boxes */
    .stAlert {
        border-radius: 8px;
        background-color: #1e293b;
        color: #e2e8f0;
        border: 1px solid #334155;
    }
</style>
""", unsafe_allow_html=True)

# URLs
LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"

# Header Section (Logo aur Title)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(LOGO_URL, width=150)
    st.title("Free CV Maker Pakistan")
    st.write("Get a professional, ATS-friendly CV in seconds.")

st.markdown("---")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Main Content (2 Columns: Left for Form, Right for Sample CV)
col_form, col_sample = st.columns([1.5, 1])

# Left Column: Form
with col_form:
    st.subheader("📝 Enter Your Details")
    with st.form("cv_form"):
        name = st.text_input("1. Full Name")
        phone = st.text_input("2. WhatsApp Number")
        edu = st.text_input("3. Education")
        exp = st.text_input("4. Experience")
        skills = st.text_input("5. Skills")
        
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
            
            st.info("⚠️ Professional editing chahiye? Click the WhatsApp button!")

# Right Column: Sample CV & Contact
with col_sample:
    st.subheader("📌 Sample CV")
    st.image(SAMPLE_CV_URL, use_container_width=True)
    
    st.markdown("---")
    st.write("💼 **To get your CV made:**")
    st.link_button("📞 WhatsApp: 0310-9018979", "https://wa.me/923109018979")
    st.write("💰 Price: Rs. 300 per CV")
