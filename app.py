import re
from groq import Groq
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Free CV Maker Pakistan",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# WEBSITE SETTINGS
# =========================================================

LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"
WHATSAPP_NUMBER = "923109018979"
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}"

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #f8faff 0%, #eef4fb 100%);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

h1 {
    color: #0f172a !important;
    font-weight: 800 !important;
    letter-spacing: -1.5px;
    font-size: 42px !important;
}

h2, h3 {
    color: #0f172a !important;
    font-weight: 700 !important;
}

p { color: #64748b; }

.trust-bar {
    background: linear-gradient(90deg, #eff6ff, #f0f9ff);
    border: 1px solid #dbeafe;
    border-radius: 12px;
    padding: 14px 24px;
    text-align: center;
    color: #1e40af;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 30px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e5eaf1 !important;
    border-radius: 18px !important;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04) !important;
    transition: all 0.3s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08) !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background: #fbfcfe !important;
    border: 1px solid #dce2ea !important;
    border-radius: 10px !important;
    transition: all 0.3s ease;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
    background: #ffffff !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #0f172a !important;
    font-size: 14px !important;
}

label {
    color: #334155 !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

.stFormSubmitButton > button {
    width: 100%;
    min-height: 52px;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.25);
    transition: all 0.3s ease !important;
}

.stFormSubmitButton > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.35);
}

.stLinkButton > a {
    width: 100% !important;
    min-height: 50px !important;
    background: linear-gradient(135deg, #16a34a, #15803d) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    box-shadow: 0 8px 20px rgba(22, 163, 74, 0.22);
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.stLinkButton > a:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 12px 28px rgba(22, 163, 74, 0.32);
}

.stDownloadButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 12px !important;
    font-weight: 700 !important;
    background: #ffffff !important;
    color: #2563eb !important;
    border: 2px solid #2563eb !important;
    transition: all 0.3s ease !important;
}

.stDownloadButton > button:hover {
    background: #2563eb !important;
    color: #ffffff !important;
    transform: translateY(-2px);
}

.stTextArea textarea {
    font-family: 'Courier New', monospace !important;
    font-size: 13px !important;
    line-height: 1.6 !important;
    background: #fdfdfd !important;
    border: 1px solid #e5eaf1 !important;
    border-radius: 10px !important;
}

@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    h1 { font-size: 28px !important; }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

header_col = st.columns([1, 2, 1])

with header_col[1]:
    st.image(LOGO_URL, width=120)
    st.markdown(
        "<h1 style='text-align:center;'>"
        "Free <span style='color:#2563eb;'>CV Maker</span> Pakistan"
        "</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; font-size:16px;'>"
        "Create a professional, ATS-friendly CV with AI — "
        "quickly, simply and for free."
        "</p>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<div class='trust-bar'>"
    "✅ 100% Free AI CV Maker &nbsp;|&nbsp; "
    "🎯 ATS-Optimized &nbsp;|&nbsp; "
    "⚡ Instant Result &nbsp;|&nbsp; "
    "🇵🇰 Made in Pakistan"
    "</div>",
    unsafe_allow_html=True,
)

# =========================================================
# TRUST FEATURES
# =========================================================

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    with st.container(border=True):
        st.markdown("### ⚡")
        st.markdown("**Fast**")
        st.caption("Generate your CV in seconds")

with feature2:
    with st.container(border=True):
        st.markdown("### 🎯")
        st.markdown("**ATS Friendly**")
        st.caption("Clean professional structure")

with feature3:
    with st.container(border=True):
        st.markdown("### ✍️")
        st.markdown("**Professional**")
        st.caption("Corporate English writing")

with feature4:
    with st.container(border=True):
        st.markdown("### ✓")
        st.markdown("**Free**")
        st.caption("Create your text CV free")

st.write("")
st.write("")

# =========================================================
# GROQ CLIENT
# =========================================================

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    client = None

# =========================================================
# MAIN AREA
# =========================================================

form_column, sample_column = st.columns([1.25, 0.95], gap="large")

# =========================================================
# LEFT SIDE — FREE AI CV GENERATOR
# =========================================================

with form_column:
    with st.container(border=True):
        st.subheader("📝 Create Your Free CV")
        st.caption(
            "Enter your information below. "
            "AI will turn it into professional CV content."
        )
        st.write("")

        with st.form("cv_form"):
            name = st.text_input("Full Name *", placeholder="Muhammad Ali Khan")
            phone = st.text_input("WhatsApp / Phone Number", placeholder="0312-1234567")
            email = st.text_input("Email Address", placeholder="muhammad@gmail.com")
            location = st.text_input("City / Location", placeholder="Islamabad, Pakistan")

            education = st.text_area(
                "Education *",
                placeholder="Example:\nBS Computer Science - University of Punjab\n2020 - 2024",
                height=90,
            )

            experience = st.text_area(
                "Work Experience",
                placeholder="Example:\nData Entry Operator - XYZ Ltd\n2022 - 2024\nHandled daily data entry and Excel reports.",
                height=120,
            )

            skills = st.text_area(
                "Skills *",
                placeholder="Example:\nMS Excel, Python, Communication, Graphic Design, Teamwork",
                height=90,
            )

            submit = st.form_submit_button("✨ Generate My Free CV")

# =========================================================
# AI CV GENERATION
# =========================================================

if submit:
    errors = []
    if not name.strip():
        errors.append("Please enter your full name.")
    if not education.strip():
        errors.append("Please enter your education.")
    if not skills.strip():
        errors.append("Please enter your skills.")

    if errors:
        for error in errors:
            st.error(error)
    elif client is None:
        st.error("GROQ_API_KEY is not configured. Please add it to Streamlit Secrets.")
    else:
        prompt = f"""
You are a Senior HR Specialist and Professional CV Writer 
with 15 years of experience in top multinational companies.

YOUR TASK:
Write a clean, professional, ATS-optimized, corporate-level CV 
in ENGLISH ONLY using ONLY the information provided below.

STRICT RULES:
1. Use only formal, professional English. No Hindi, Urdu, or slang.
2. NEVER invent information — no fake companies, dates, titles, achievements, or certifications.
3. Do NOT use placeholder text like "Your Address Here" or "N/A".
4. If any information is missing, simply omit that section.
5. Use strong action verbs (Managed, Developed, Increased, Streamlined, Achieved, Led).
6. Keep the Professional Summary to 3-4 impactful sentences.
7. Use bullet points for Experience and Skills.
8. Use UPPERCASE for section headers.
9. Do NOT use tables, images, or complex formatting.
10. Do NOT mention AI or the CV maker anywhere.
11. Return ONLY the final CV — no explanations before or after.

OUTPUT STRUCTURE (follow exactly):

FULL NAME
Phone | Email | Location

PROFESSIONAL SUMMARY
(3-4 lines, professional tone)

EDUCATION
- Degree, Institution, Year

WORK EXPERIENCE
- Job Title, Company, Duration
- Key responsibilities as bullet points

SKILLS
- Skill 1, Skill 2, Skill 3...

CANDIDATE INFORMATION:
Name: {name}
Phone: {phone}
Email: {email}
Location: {location}
Education: {education}
Experience: {experience}
Skills: {skills}
"""

        with st.spinner("🤖 Creating your professional CV..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": "You are an expert professional CV writer. Follow all instructions strictly."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.3,
                    max_tokens=1800,
                )
                generated_cv = response.choices[0].message.content.strip()
                st.session_state["generated_cv"] = generated_cv
                st.session_state["cv_name"] = name.strip()
            except Exception as error:
                st.error("CV generation failed. Please try again.")
                st.caption(str(error))

# =========================================================
# GENERATED CV OUTPUT
# =========================================================

if "generated_cv" in st.session_state:
    st.write("")
    with st.container(border=True):
        st.subheader("✅ Your Free CV is Ready")
        st.caption("Your AI-generated professional CV is below. Copy it or download it.")

        generated_cv = st.session_state["generated_cv"]
        st.text_area("Your CV", value=generated_cv, height=500)

        cv_name = st.session_state.get("cv_name", "Professional")
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", cv_name)

        st.download_button(
            "📥 Download My Free CV",
            data=generated_cv,
            file_name=f"{safe_name}_Professional_CV.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.info(
            "💡 **Want a designed PDF version like the sample?** "
            "Click the WhatsApp button on the right →"
        )

# =========================================================
# RIGHT SIDE — SAMPLE / PAID SERVICE
# =========================================================

with sample_column:
    with st.container(border=True):
        st.markdown(
            """
            <div style="
                display:inline-block;
                padding:6px 12px;
                background:#fef3c7;
                color:#92400e;
                border:1px solid #fde68a;
                border-radius:8px;
                font-size:11px;
                font-weight:700;
                letter-spacing:0.5px;
            ">
                ⭐ SAMPLE DESIGN
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.subheader("📄 Professional CV Design")
        st.caption("This is our premium, designed CV format — perfect for job applications.")

        st.image(SAMPLE_CV_URL, use_container_width=True)

        st.markdown("---")

        st.markdown("### 💼 Want Your CV Like This?")
        st.write(
            "Get your CV professionally designed and formatted "
            "as a polished PDF — ready to send to employers."
        )

        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, #eff6ff, #dbeafe);
                padding: 14px;
                border-radius: 10px;
                text-align: center;
                margin: 12px 0;
            ">
                <span style="font-size: 24px; font-weight: 800; color:#1e40af;">Rs. 300</span>
                <span style="color:#1e40af; font-size: 14px;"> / CV</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Order on WhatsApp",
            WHATSAPP_URL,
            use_container_width=True,
        )

        st.caption("Click to chat directly on WhatsApp")

# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")
st.write("")

st.markdown(
    "<h3 style='text-align:center; margin-bottom:20px;'>How It Works</h3>",
    unsafe_allow_html=True,
)

info1, info2, info3 = st.columns(3)

with info1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.markdown("**Enter Your Information**")
        st.caption("Add your education, experience and skills.")

with info2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**AI Creates Your CV**")
        st.caption("Your information is converted into professional text — free.")

with info3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Want a Designed PDF?**")
        st.caption("Order our premium design service on WhatsApp.")

# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")

st.markdown("---")
st.markdown(
    """
    <p style="
        text-align:center;
        color:#94a3b8;
        font-size:13px;
        line-height:1.8;
    ">
        <strong style="color:#475569;">Free CV Maker Pakistan</strong><br>
        AI-Powered Professional CV Generation<br>
        📞 WhatsApp: 0310-9018979<br><br>
        © 2026 Free CV Maker Pakistan. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True,
)
