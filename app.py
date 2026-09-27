import streamlit as st
from groq import Groq

# Page Config (Wide layout for professional look)
st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄", layout="wide")

# 👇 Custom CSS for Professional Look
st.markdown("""
<style>
    /* Main background and font */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Poppins', sans-serif;
    }
    /* Headings */
    h1, h2, h3 {
        color: #1f3a5f;
        font-weight: 700;
    }
    /* Input fields */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #d1d5db;
        padding: 10px;
        font-size: 16px;
    }
    /* Main Button */
    .stButton>button {
        background: linear-gradient(90deg, #1f3a5f, #2b5876);
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #2b5876, #1f3a5f);
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1f3a5f;
        color: white;
    }
    [data-testid="stSidebar"] h2 {
        color: white;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #e5e7eb;
    }
    /* Success/Error messages */
    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section with Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg", width=200)
    st.markdown("<h1 style='text-align: center;'>Free CV Maker - AI Wala</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4b5563;'>Get a professional, ATS-friendly CV in seconds.</p>", unsafe_allow_html=True)

# Sidebar Section
with st.sidebar:
    st.header("📌 Sample CV")
    st.image("https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg", use_container_width=True)
    
    st.markdown("---")
    st.write("💼 **To get your CV made:**")
    st.link_button("📞 WhatsApp: 0310-9018979", "https://wa.me/923109018979")
    st.write("💰 Price: Rs. 300 per CV")
    st.markdown("---")

# API Client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Main Form Section
st.markdown("### 📝 Enter Your Details")
with st.form("cv_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("1. Full Name")
        edu = st.text_input("3. Education")
        skills = st.text_input("5. Skills")
    with col2:
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
        
        st.warning(f"⚠️ Professional editing chahiye? Click the WhatsApp button in the sidebar!")
