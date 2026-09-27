import streamlit as st
from groq import Groq
import re

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Free CV Maker Pakistan | AI CV Generator",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CONSTANTS
# =========================================================

LOGO_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/logo.jpg"
SAMPLE_CV_URL = "https://raw.githubusercontent.com/labraizraja8-prog/freecvmakerpk/main/cv.jpeg"

WHATSAPP_NUMBER = "923109018979"
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --navy: #0f172a;
    --text: #334155;
    --muted: #64748b;
    --border: #e2e8f0;
    --background: #f8fafc;
    --white: #ffffff;
    --success: #16a34a;
}

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(37, 99, 235, 0.08),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(14, 165, 233, 0.06),
            transparent 30%
        ),
        #f8fafc;
}

/* Remove excessive top space */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1250px !important;
}

/* Main animation */
.block-container {
    animation: pageFade 0.7s ease-out;
}

@keyframes pageFade {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    text-align: center;
    padding: 10px 20px 25px 20px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #bfdbfe;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero-title {
    font-size: clamp(32px, 5vw, 52px);
    line-height: 1.05;
    font-weight: 800;
    letter-spacing: -1.8px;
    color: #0f172a;
    margin: 5px 0 12px 0;
}

.hero-title span {
    background: linear-gradient(
        135deg,
        #1d4ed8,
        #2563eb,
        #0284c7
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 700px;
    margin: auto;
    color: #64748b;
    font-size: 16px;
    line-height: 1.7;
}

/* =========================================================
   TRUST CARDS
   ========================================================= */

.trust-card {
    background: rgba(255,255,255,0.9);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px 12px;
    text-align: center;
    min-height: 120px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    transition: all .25s ease;
}

.trust-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(15,23,42,0.09);
}

.trust-icon {
    font-size: 27px;
    margin-bottom: 7px;
}

.trust-title {
    color: #0f172a;
    font-size: 15px;
    font-weight: 800;
}

.trust-text {
    color: #64748b;
    font-size: 12px;
    margin-top: 5px;
}

/* =========================================================
   SECTION HEADERS
   ========================================================= */

.section-title {
    color: #0f172a;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 5px;
}

.section-description {
    color: #64748b;
    font-size: 13px;
    margin-bottom: 18px;
}

/* =========================================================
   FORM CARD
   ========================================================= */

.form-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 15px 40px rgba(15,23,42,0.06);
}

/* Streamlit form */
div[data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* =========================================================
   INPUTS
   ========================================================= */

div[data-baseweb="input"] {
    border-radius: 10px !important;
}

div[data-baseweb="input"] > div {
    background: #f8fafc !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

div[data-baseweb="input"] input {
    color: #0f172a !important;
    font-weight: 500 !important;
}

textarea {
    color: #0f172a !important;
}

/* Labels */
label {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button,
.stFormSubmitButton > button {
    width: 100%;
    min-height: 48px;
    border: none !important;
    border-radius: 11px !important;
    background: linear-gradient(
        135deg,
        #1d4ed8,
        #2563eb
    ) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    box-shadow: 0 8px 20px rgba(37,99,235,.25);
    transition: all .25s ease !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(37,99,235,.35);
}

/* Download button */
.stDownloadButton > button {
    width: 100%;
    min-height: 46px;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

/* =========================================================
   SAMPLE CARD
   ========================================================= */

.sample-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 15px 40px rgba(15,23,42,0.06);
}

.sample-label {
    display: inline-block;
    padding: 6px 10px;
    background: #f1f5f9;
    color: #475569;
    border-radius: 7px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* =========================================================
   PRICE CARD
   ========================================================= */

.price-card {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e3a8a
    );
    color: white;
    border-radius: 16px;
    padding: 18px;
    margin-top: 18px;
}

.price-card .small {
    color: #bfdbfe;
    font-size: 12px;
    font-weight: 600;
}

.price-card .price {
    font-size: 28px;
    font-weight: 800;
    margin: 4px 0;
}

.price-card .desc {
    color: #dbeafe;
    font-size: 12px;
}

/* =========================================================
   WHATSAPP
   ========================================================= */

.whatsapp-box {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    border-radius: 14px;
    padding: 15px;
    text-align: center;
    margin-top: 15px;
}

.whatsapp-title {
    color: #166534;
    font-weight: 800;
    font-size: 14px;
}

.whatsapp-text {
    color: #15803d;
    font-size: 12px;
    margin-top: 4px;
}

/* =========================================================
   CV RESULT
   ========================================================= */

.result-box {
    background: #ffffff;
    border: 1px solid #bfdbfe;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(37,99,235,.08);
}

.result-header {
    color: #0f172a;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 5px;
}

.result-sub {
    color: #64748b;
    font-size: 12px;
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    margin-top: 50px;
    padding: 25px 10px;
    border-top: 1px solid #e2e8f0;
}

/* Mobile */
@media (max-width: 768px) {

    .block-container {
        padding: 1rem !important;
    }

    .hero-title {
        font-size: 34px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .form-card,
    .sample-card {
        padding: 18px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER / HERO
# =========================================================

st.markdown("<div class='hero'>", unsafe_allow_html=True)

st.image(LOGO_URL, width=125)

st.markdown(
    """
<div class="hero-badge">
    🇵🇰 MADE FOR JOB SEEKERS IN PAKISTAN
</div>

<div class="hero-title">
    Create a <span>Professional CV</span><br>
    with AI in Seconds
</div>

<div class="hero-subtitle">
    Generate an ATS-friendly, professionally written CV using AI.
    Perfect for fresh graduates, experienced professionals,
    freelancers and job seekers.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TRUST SECTION
# =========================================================

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">⚡</div>
            <div class="trust-title">Fast Generation</div>
            <div class="trust-text">Professional CV in seconds</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with t2:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">🎯</div>
            <div class="trust-title">ATS Friendly</div>
            <div class="trust-text">Designed for HR systems</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with t3:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">✍️</div>
            <div class="trust-title">Professional Writing</div>
            <div class="trust-text">Corporate English content</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with t4:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">🔒</div>
            <div class="trust-title">Simple & Secure</div>
            <div class="trust-text">No complicated registration</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# GROQ CLIENT
# =========================================================

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    client = None

# =========================================================
# MAIN LAYOUT
# =========================================================

col_form, col_preview = st.columns(
    [1.35, 1],
    gap="large"
)

# =========================================================
# LEFT - FORM
# =========================================================

with col_form:

    st.markdown(
        """
        <div class="form-card">
            <div class="section-title">
                📝 Build Your CV
            </div>
            <div class="section-description">
                Enter your information below. Our AI will turn it
                into professional CV content.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("professional_cv_form"):

        name = st.text_input(
            "Full Name *",
            placeholder="e.g. Muhammad Ali Khan",
        )

        phone = st.text_input(
            "WhatsApp / Phone Number",
            placeholder="e.g. 0312-1234567",
        )

        email = st.text_input(
            "Email Address",
            placeholder="e.g. muhammad@gmail.com",
        )

        location = st.text_input(
            "City / Location",
            placeholder="e.g. Islamabad, Pakistan",
        )

        education = st.text_area(
            "Education *",
            placeholder=(
                "Example:\n"
                "BS Computer Science - University of Punjab (2020-2024)"
            ),
            height=100,
        )

        experience = st.text_area(
            "Work Experience",
            placeholder=(
                "Example:\n"
                "Data Entry Operator - XYZ Company\n"
                "2022 - 2024\n"
                "Handled daily data entry and Excel reporting."
            ),
            height=130,
        )

        skills = st.text_area(
            "Skills *",
            placeholder=(
                "Example:\n"
                "MS Excel, Python, Communication, "
                "Graphic Design, Teamwork"
            ),
            height=100,
        )

        submit = st.form_submit_button(
            "✨ Generate My Professional CV"
        )

# =========================================================
# CV GENERATION
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
        st.error(
            "GROQ_API_KEY is not configured. "
            "Please add it to your Streamlit secrets."
        )

    else:

        with st.spinner("🤖 AI is professionally writing your CV..."):

            prompt = f"""
You are an expert Senior HR Recruiter, ATS Resume Specialist,
and Corporate CV Writer with 15+ years of experience.

Create a highly professional, modern, ATS-friendly CV.

IMPORTANT RULES:

1. Write ONLY in professional English.
2. Never invent qualifications, companies, job titles,
   dates, achievements, certifications or skills.
3. Use ONLY information supplied by the candidate.
4. Never add fake information.
5. Never use placeholders.
6. Never create tables.
7. Use clean plain-text formatting.
8. Use strong professional action verbs where supported
   by the provided experience.
9. Keep the professional summary concise and impactful.
10. Make the CV suitable for Pakistani and international
    job applications.
11. Do not mention that AI created the CV.
12. Do not include references unless provided.
13. Do not include a photo section.
14. Do not include unnecessary personal information.
15. If experience is limited, create an honest entry-level
    professional summary without inventing experience.

CV STRUCTURE:

FULL NAME
Contact information

PROFESSIONAL SUMMARY

EDUCATION

WORK EXPERIENCE

SKILLS

CONTACT INFORMATION:
Name: {name}
Phone: {phone}
Email: {email}
Location: {location}

EDUCATION:
{education}

WORK EXPERIENCE:
{experience}

SKILLS:
{skills}

Return ONLY the final CV.
"""

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional CV writer. "
                                "Follow the user's formatting requirements "
                                "exactly."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0.35,
                    max_tokens=1800,
                )

                cv = response.choices[0].message.content.strip()

                st.session_state["generated_cv"] = cv
                st.session_state["cv_name"] = name.strip()

            except Exception as e:
                st.error(
                    f"CV generation failed. Please try again.\n\n"
                    f"Error: {str(e)}"
                )

# =========================================================
# RESULT SECTION
# =========================================================

if "generated_cv" in st.session_state:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="result-box">
            <div class="result-header">
                ✅ Your Professional CV is Ready
            </div>
            <div class="result-sub">
                Review your CV below and download the text version.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cv = st.session_state["generated_cv"]
    cv_name = st.session_state.get("cv_name", "Professional")

    st.text_area(
        "📄 Generated CV",
        value=cv,
        height=500,
        key="cv_output",
    )

    d1, d2 = st.columns(2)

    with d1:

        safe_name = re.sub(
            r"[^a-zA-Z0-9_-]",
            "_",
            cv_name
        )

        st.download_button(
            "📥 Download CV",
            data=cv,
            file_name=f"{safe_name}_Professional_CV.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with d2:

        st.link_button(
            "💬 Get Professional PDF",
            WHATSAPP_URL,
            use_container_width=True,
        )

    st.info(
        "💡 Want a professionally designed PDF CV or Cover Letter? "
        "Contact us on WhatsApp."
    )

# =========================================================
# RIGHT COLUMN - SAMPLE
# =========================================================

with col_preview:

    st.markdown(
        """
        <div class="sample-card">
            <div class="sample-label">
                PROFESSIONAL CV EXAMPLE
            </div>
            <div class="section-title">
                📌 See the Result
            </div>
            <div class="section-description">
                This is an example of how your professionally
                generated CV can look.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.image(
        SAMPLE_CV_URL,
        use_container_width=True,
    )

    st.markdown(
        """
        <div class="price-card">
            <div class="small">
                PROFESSIONAL FORMATTING SERVICE
            </div>

            <div class="price">
                Rs. 300
            </div>

            <div class="desc">
                Get your CV professionally formatted
                and ready for job applications.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="whatsapp-box">
            <div class="whatsapp-title">
                💬 Need a Professional PDF?
            </div>
            <div class="whatsapp-text">
                Contact us on WhatsApp for formatting,
                PDF and Cover Letter services.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "📞 WhatsApp Us",
        WHATSAPP_URL,
        use_container_width=True,
    )

# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;">
        <div class="section-title">
            🚀 How It Works
        </div>
        <div class="section-description">
            Create your professional CV in three simple steps.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

h1, h2, h3 = st.columns(3)

with h1:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">1️⃣</div>
            <div class="trust-title">Enter Your Details</div>
            <div class="trust-text">
                Add your education, experience and skills.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h2:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">2️⃣</div>
            <div class="trust-title">AI Writes Your CV</div>
            <div class="trust-text">
                AI converts your information into
                professional CV content.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h3:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">3️⃣</div>
            <div class="trust-title">Download & Apply</div>
            <div class="trust-text">
                Copy your CV or request professional
                PDF formatting.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        <strong>Free CV Maker Pakistan</strong><br>
        AI-Powered Professional CV Generation
        <br><br>
        © 2026 Free CV Maker Pakistan. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
