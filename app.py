import streamlit as st
from groq import Groq

st.set_page_config(page_title="Free CV Maker Pakistan", page_icon="📄", layout="wide")

# 👇 Corporate Level UI & Animations CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

    /* Main Background */
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Fade-in Animation */
    .main .block-container {
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Typography */
    h1 { color: #0f172a; font-weight: 800; text-align: center; margin-bottom: 0; }
    h2, h3 { color: #1e293b; font-weight: 700; }
    p { color: #475569; text-align: center; }

    /* Trust Badges */
    .badge-box {
        background: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    .badge-box:hover { transform: translateY(-5px); }
    .badge-box h4 { color: #1e293b; margin: 10px 0 5px 0; font-size: 16px; }
    .badge-box p { font-size: 13px; margin: 0; color: #64748b; }

    /* Cards for Form and Sample CV */
    div[data-testid="stForm"], div[data-testid="column"] {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }
    
    /* Input Fields */
    .stTextInput>div>div>input {
        background-color: #f8fafc;
        color: #0f172a;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 12px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #2563eb;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }

    /* Primary Button */
    .stButton>button, .stFormSubmitButton>button {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.3);
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4);
    }

    /* WhatsApp Button */
    .stLinkButton>a {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-weight: 700 !important;
        text-align: center !important;
        display: block !important;
        transition: all 0.3s ease !important;
        text-decoration: none !important;
    }
    .stLinkButton>a:hover {
        background-color: #128C7E !important;
        transform: scale(1.02);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #64748b;
        font-size: 14px;
        margin-top: 50px;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# URLs
LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(LOGO_URL, width=150)
    st.title("Free CV Maker Pakistan")
    st.write("AI-Powered Professional CV Generation")

st.markdown("<br>", unsafe_allow_html=True)

# Trust Badges (Why Choose Us)
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown("<div class='badge-box'><h4>⚡ 5 Second Result</h4><p>Instant AI generation</p></div>", unsafe_allow_html=True)
with b2:
    st.markdown("<div class='badge-box'><h4>🎯 ATS Optimized</h4><p>Passes HR software</p></div>", unsafe_allow_html=True)
with b3:
    st.markdown("<div class='badge-box'><h4>💼 HR Approved</h4><p>Written by Senior HR</p></div>", unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Main Content
col_form, col_sample = st.columns([1.3, 1], gap="large")

# Left Column: Form
with col_form:
    with st.container():
        st.subheader("📝 Enter Your Details")
        with st.form("cv_form"):
            name = st.text_input("1. Full Name", help="Likhne ka tareeqa: Muhammad Ali Khan")
            phone = st.text_input("2. WhatsApp Number", help="Apna active WhatsApp number dalein")
            edu = st.text_input("3. Education", help="Example: BSCS from Punjab University (2020-2024)")
            exp = st.text_input("4. Experience", help="Example: 2 years as Data Entry Operator at XYZ Ltd")
            skills = st.text_input("5. Skills", help="Example: Python, MS Excel, Graphic Design")
            
            submit_button = st.form_submit_button("Mera CV Banao ✨")

        if submit_button:
            if name == "":
                st.error("Please enter your name")
            else:
                with st.spinner("AI is generating your CV..."):
                    # 👇 UPGRADED PROFESSIONAL PROMPT (Senior HR Specialist)
                    prompt = f"""
                    You are a Senior HR Specialist and Professional CV Writer with 15 years of experience in top multinational companies.
                    Your task is to write a highly professional, ATS-optimized, and corporate-level CV in ENGLISH ONLY.
                    
                    STRICT RULES:
                    1. Do NOT use Hindi, Urdu, or any other language. Use formal, corporate English.
                    2. Do NOT write any placeholder text (e.g., "Your Address Here"). Only use the provided information.
                    3. Use strong action verbs (e.g., Managed, Developed, Increased, Streamlined).
                    4. Keep the Professional Summary to 3-4 impactful sentences.
                    5. Format the output cleanly with UPPERCASE section headers (e.g., PROFESSIONAL SUMMARY, EDUCATION, WORK EXPERIENCE, SKILLS).
                    6. Use bullet points for Experience and Skills.
                    7. Do NOT include a table or complex formatting.

                    INFORMATION PROVIDED:
                    Name: {name}
                    Phone: {phone}
                    Education: {edu}
                    Experience: {exp}
                    Skills: {skills}

                    OUTPUT FORMAT:
                    Start directly with the Name and Contact Info at the top.
                    Then PROFESSIONAL SUMMARY.
                    Then EDUCATION.
                    Then WORK EXPERIENCE.
                    Then SKILLS.
                    """
                    response = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    cv = response.choices[0].message.content

                st.success("✅ Professional CV Ready Hai!")
                st.text_area("📋 Yahan se Copy Karo:", cv, height=350)
                st.download_button("📥 Download Karo", cv, file_name=f"{name}_Professional_CV.txt")
                
                st.info("💡 Professional PDF ya Cover Letter chahiye? WhatsApp karein!")

# Right Column: Sample CV
with col_sample:
    with st.container():
        st.subheader("📌 Sample CV")
        st.image(SAMPLE_CV_URL, use_container_width=True)
        
        st.markdown("---")
        st.write("💼 **To get your CV professionally formatted:**")
        st.link_button("📞 WhatsApp: 0310-9018979", "https://wa.me/923109018979")
        st.write("💰 Price: Rs. 300 per CV")

# Footer
st.markdown("<div class='footer'>© 2026 Free CV Maker Pakistan. All rights reserved.</div>", unsafe_allow_html=True)
