import re
from groq import Groq
import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Free CV Maker Pakistan - ATS Resume Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# SETTINGS
# =========================================================

LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"
WHATSAPP_URL = "https://wa.me/923109018979"

# =========================================================
# ADSTERRA AD CODES
# =========================================================

# 728x90 Banner
AD_728x90 = """
<script>
  atOptions = {
    'key' : '39c52b8e4f878194634c7f5180494659',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://www.highrevenueformat.com/39c52b8e4f878194634c7f5180494659/invoke.js"></script>
"""

# 300x250 Banner
AD_300x250 = """
<script>
  atOptions = {
    'key' : 'd01929cee1521e814eb525fd5373e9a4',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://www.highrevenueformat.com/d01929cee1521e814eb525fd5373e9a4/invoke.js"></script>
"""

# Native Banner
AD_NATIVE = """
<script async="async" data-cfasync="false" src="https://pl31550229.profitableratecpmnetwork.com/67434af7d43e6dce4442b743cdcbcc77/invoke.js"></script>
<div id="container-67434af7d43e6dce4442b743cdcbcc77"></div>
"""

# 320x50 Banner
AD_320x50 = """
<script>
  atOptions = {
    'key' : 'a33a4e191058fe48de9619a113ad9507',
    'format' : 'iframe',
    'height' : 50,
    'width' : 320,
    'params' : {}
  };
</script>
<script src="https://www.highrevenueformat.com/a33a4e191058fe48de9619a113ad9507/invoke.js"></script>
"""

# Social Bar
AD_SOCIAL_BAR = """
<script src="https://pl31550228.profitableratecpmnetwork.com/19/25/56/19255660631a617bbfeaf81328ae8d9b.js"></script>
"""

# =========================================================
# BOLD NEW CSS (FIXED VISIBILITY)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: #1e293b !important;
}

.stApp {
    background-color: #f8fafc !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 0rem;
    padding-bottom: 2rem;
}

#MainMenu, footer { visibility: hidden; }

.top-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #3b82f6 100%);
    padding: 40px 30px;
    border-radius: 0 0 30px 30px;
    text-align: center;
    color: white !important;
    margin-bottom: 30px;
    box-shadow: 0 10px 40px rgba(30, 58, 138, 0.3);
}
.top-banner h1 {
    color: white !important;
    font-size: 40px !important;
    font-weight: 800 !important;
    margin: 15px 0 10px 0 !important;
    letter-spacing: -1px;
}
.top-banner p {
    color: #dbeafe !important;
    font-size: 16px;
    margin: 0;
}
.top-banner img {
    border-radius: 50%;
    border: 3px solid rgba(255,255,255,0.3);
}

.trust-strip {
    background: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    color: #1e3a8a !important;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 25px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06) !important;
    transition: all 0.3s ease !important;
    padding: 15px !important;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.1) !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background-color: #ffffff !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    background-color: #ffffff !important;
}
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #0f172a !important;
    font-weight: 500 !important;
}
label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

.stFormSubmitButton > button {
    width: 100% !important;
    min-height: 60px !important;
    background: linear-gradient(135deg, #1e40af, #2563eb, #3b82f6) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 19px !important;
    font-weight: 800 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    box-shadow: 0 10px 25px rgba(37, 99, 235, 0.35) !important;
    transition: all 0.3s ease !important;
}
.stFormSubmitButton > button:hover {
    transform: translateY(-3px) scale(1.01) !important;
    box-shadow: 0 15px 35px rgba(37, 99, 235, 0.45) !important;
}

.stLinkButton > a {
    width: 100% !important;
    min-height: 60px !important;
    background: linear-gradient(135deg, #15803d, #16a34a, #22c55e) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    font-weight: 800 !important;
    font-size: 17px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 10px 25px rgba(22, 163, 74, 0.35) !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
}
.stLinkButton > a:hover {
    transform: translateY(-3px) scale(1.01) !important;
    box-shadow: 0 15px 35px rgba(22, 163, 74, 0.45) !important;
    color: white !important;
}

.stDownloadButton > button {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    background: #ffffff !important;
    color: #2563eb !important;
    border: 2px solid #2563eb !important;
}
.stDownloadButton > button:hover {
    background: #2563eb !important;
    color: white !important;
}

.how-it-works-card {
    background: white !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    padding: 20px !important;
    text-align: center !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    height: 100%;
}
.how-it-works-card h4 {
    color: #1e293b !important;
    font-weight: 700 !important;
    margin-bottom: 5px !important;
}
.how-it-works-card p {
    color: #64748b !important;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TOP HEADER BANNER
# =========================================================

st.markdown(f"""
<div class='top-banner'>
    <img src="{LOGO_URL}" width="100">
    <h1>Free CV Maker Pakistan</h1>
    <p>✨ Create a professional, ATS-friendly CV with AI — quickly, simply and for free.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='trust-strip'>
    ✅ 100% Free AI &nbsp;•&nbsp; 🎯 ATS-Optimized &nbsp;•&nbsp; ⚡ Instant Result &nbsp;•&nbsp; 🇵🇰 Made in Pakistan
</div>
""", unsafe_allow_html=True)

# ---------- TOP AD (728x90) ----------
st.write("")
st.html(AD_728x90)
st.write("")

# =========================================================
# TRUST FEATURES
# =========================================================

feature1, feature2, feature3, feature4 = st.columns(4)

with feature1:
    with st.container(border=True):
        st.markdown("### ⚡")
        st.markdown("**Fast**")
        st.caption("CV in seconds")

with feature2:
    with st.container(border=True):
        st.markdown("### 🎯")
        st.markdown("**ATS Friendly**")
        st.caption("Professional structure")

with feature3:
    with st.container(border=True):
        st.markdown("### ✍️")
        st.markdown("**Professional**")
        st.caption("Corporate writing")

with feature4:
    with st.container(border=True):
        st.markdown("### ✓")
        st.markdown("**Free**")
        st.caption("Text CV free")

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

form_column, sample_column = st.columns([1.2, 0.8], gap="large")

# ---------- LEFT: FORM ----------
with form_column:
    with st.container(border=True):
        st.subheader("📝 Create Your Free CV")
        st.caption("Enter your details below. AI will generate your professional CV.")
        st.write("")

        with st.form("cv_form"):
            name = st.text_input("Full Name *", placeholder="Muhammad Ali Khan")
            phone = st.text_input("WhatsApp / Phone Number", placeholder="0312-1234567")
            email = st.text_input("Email Address", placeholder="muhammad@gmail.com")
            location = st.text_input("City / Location", placeholder="Islamabad, Pakistan")

            education = st.text_area(
                "Education *",
                placeholder="BS Computer Science - University of Punjab\n2020 - 2024",
                height=85,
            )
            experience = st.text_area(
                "Work Experience",
                placeholder="Data Entry Operator - XYZ Ltd\n2022 - 2024\nHandled daily data entry and Excel reports.",
                height=110,
            )
            skills = st.text_area(
                "Skills *",
                placeholder="MS Excel, Python, Communication, Graphic Design, Teamwork",
                height=85,
            )

            submit = st.form_submit_button("✨ Generate My Free CV")

# ---------- AI GENERATION ----------
if submit:
    errors = []
    if not name.strip():
        errors.append("Please enter your full name.")
    if not education.strip():
        errors.append("Please enter your education.")
    if not skills.strip():
        errors.append("Please enter your skills.")

    if errors:
        for e in errors:
            st.error(e)
    elif client is None:
        st.error("GROQ_API_KEY is not configured.")
    else:
        prompt = f"""
You are a Senior HR Specialist and Professional CV Writer with 15 years of experience in top multinational companies.

TASK: Write a clean, professional, ATS-optimized, corporate-level CV in ENGLISH ONLY using ONLY the information provided.

STRICT RULES:
1. Only formal professional English.
2. NEVER invent information.
3. NO placeholder text.
4. Omit missing sections.
5. Use action verbs.
6. Summary: 3-4 sentences.
7. Bullet points for Experience and Skills.
8. UPPERCASE section headers.
9. No tables or complex formatting.
10. Do NOT mention AI.
11. Return ONLY the CV.

FORMAT:

FULL NAME
Phone | Email | Location

PROFESSIONAL SUMMARY

EDUCATION

WORK EXPERIENCE

SKILLS

CANDIDATE INFO:
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
                        {"role": "system", "content": "You are an expert CV writer. Follow instructions strictly."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.3,
                    max_tokens=1800,
                )
                generated_cv = response.choices[0].message.content.strip()
                st.session_state["generated_cv"] = generated_cv
                st.session_state["cv_name"] = name.strip()
            except Exception as err:
                st.error("CV generation failed. Please try again.")
                st.caption(str(err))

# ---------- CV OUTPUT ----------
if "generated_cv" in st.session_state:
    st.write("")
    with st.container(border=True):
        st.subheader("✅ Your Free CV is Ready")
        st.caption("Copy or download your AI-generated CV below.")

        generated_cv = st.session_state["generated_cv"]
        st.text_area("Your CV", value=generated_cv, height=500)

        cv_name = st.session_state.get("cv_name", "Professional")
        safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", cv_name)

        st.download_button(
            "📥 Download My Free CV",
            data=generated_cv,
            file_name=f"{safe_name}_CV.txt",
            mime="text/plain",
            use_container_width=True,
        )
        st.info("💡 Want a designed PDF version? Click the WhatsApp button →")

# ---------- RIGHT: SAMPLE + PAID ----------
with sample_column:
    with st.container(border=True):
        st.markdown("""
        <div style="display:inline-block;padding:6px 12px;background:#fef3c7;
        color:#92400e;border:1px solid #fde68a;border-radius:8px;font-size:11px;
        font-weight:700;letter-spacing:0.5px;">⭐ SAMPLE DESIGN</div>
        """, unsafe_allow_html=True)

        st.subheader("📄 Professional CV Design")
        st.caption("Our premium designed format — perfect for job applications.")

        st.image(SAMPLE_CV_URL, use_container_width=True)

        st.markdown("---")
        st.markdown("### 💼 Want Your CV Like This?")
        st.write("Get your CV professionally designed as a polished PDF — ready to send.")

        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            border: 2px solid #f59e0b;
            padding: 22px;
            border-radius: 14px;
            text-align: center;
            margin: 15px 0;
            box-shadow: 0 6px 15px rgba(245, 158, 11, 0.15);
        ">
            <div style="font-size: 12px; color: #92400e; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">Professional PDF Design</div>
            <div style="font-size: 42px; font-weight: 900; color: #b45309; line-height: 1; margin: 8px 0;">Rs. 300</div>
            <div style="font-size: 13px; color: #92400e; font-weight: 600;">per CV</div>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("💬 Order on WhatsApp", WHATSAPP_URL, use_container_width=True)
        st.caption("Click to chat directly on WhatsApp")

        # ---------- SIDEBAR ADS (Right Column) ----------
        st.markdown("---")
        st.html(AD_300x250)
        st.markdown("---")
        st.html(AD_NATIVE)

# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")
st.markdown("<h3 style='text-align:center; margin-bottom:20px; color:#1e293b;'>How It Works</h3>", unsafe_allow_html=True)

i1, i2, i3 = st.columns(3)

with i1:
    st.markdown("""
    <div class="how-it-works-card">
        <h4>1️⃣ Enter Your Information</h4>
        <p>Add your education, experience and skills.</p>
    </div>
    """, unsafe_allow_html=True)

with i2:
    st.markdown("""
    <div class="how-it-works-card">
        <h4>2️⃣ AI Creates Your CV</h4>
        <p>Your information becomes professional text — free.</p>
    </div>
    """, unsafe_allow_html=True)

with i3:
    st.markdown("""
    <div class="how-it-works-card">
        <h4>3️⃣ Want a Designed PDF?</h4>
        <p>Order our premium design on WhatsApp.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# BOTTOM ADS
# =========================================================

st.write("")
st.markdown("---")
st.html(AD_320x50)

# =========================================================
# FOOTER
# =========================================================

st.write("")
st.markdown("---")
st.markdown("""
<p style="text-align:center;color:#94a3b8;font-size:13px;line-height:1.8;">
<strong style="color:#475569;">Free CV Maker Pakistan</strong><br>
AI-Powered Professional CV Generation<br>
📞 WhatsApp: 0310-9018979<br><br>
© 2026 Free CV Maker Pakistan. All rights reserved.
</p>
""", unsafe_allow_html=True)

# ---------- SOCIAL BAR AD ----------
st.html(AD_SOCIAL_BAR)
