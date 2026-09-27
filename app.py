import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄", layout="wide")

# 👇 Premium Light Theme & Animations CSS
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* Main Background with Soft Multishade Gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Inter', sans-serif;
    }

    /* Fade-in Animation for Main Content */
    .main .block-container {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Headings */
    h1, h2, h3 {
        color: #1e293b;
        font-weight: 700;
        text-align: center;
    }
    p {
        text-align: center;
        color: #475569;
    }

    /* Card Design for Form and Sample CV */
    div[data-testid="stForm"], div[data-testid="column"] {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    /* Input Fields */
    .stTextInput>div>div>input {
        background-color: #f8fafc;
        color: #1e293b;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 12px;
        font-size: 15px;
        transition: all 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        border-color: #4f46e5;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
        background-color: #ffffff;
    }

    /* Buttons with Hover Animation */
    .stButton>button, .stFormSubmitButton>button {
        background: linear-gradient(90deg, #4f46e5, #4338ca);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.3);
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
        background: linear-gradient(90deg, #4338ca, #4f46e5);
    }

    /* WhatsApp Button Style */
    .stLinkButton>a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        text-align: center !important;
        display: block !important;
        transition: all 0.3s ease !important;
        text-decoration: none !important;
    }
    .stLinkButton>a:hover {
        background-color: #128C7E !important;
        transform: scale(1.02);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# URLs
LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"

# Header Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(LOGO_URL, width=150)
    st.title("Free CV Maker Pakistan")
    st.write("Get a professional, ATS-friendly CV in seconds.")

st.markdown("<br>", unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Main Content (2 Columns: Left for Form, Right for Sample CV)
col_form, col_sample = st.columns([1.5, 1], gap="large")

# Left Column: Form inside a Card
with col_form:
    with st.container():
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
                st.text_area("Yahan se Copy Karo", cv, height=300)
                st.download_button("📥 Download Karo", cv, file_name=f"{name}_CV.txt")
                
                st.info("⚠️ Professional editing chahiye? Click the WhatsApp button!")

# Right Column: Sample CV inside a Card
with col_sample:
    with st.container():
        st.subheader("📌 Sample CV")
        st.image(SAMPLE_CV_URL, use_container_width=True)
        
        st.markdown("---")
        st.write("💼 **To get your CV made:**")
        st.link_button("📞 WhatsApp: 0310-9018979", "https://wa.me/923109018979")
        st.write("💰 Price: Rs. 300 per CV")
