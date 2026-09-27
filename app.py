import re
import streamlit as st
from groq import Groq


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
# CONFIG
# =========================================================

LOGO_URL = (
    "https://raw.githubusercontent.com/"
    "labraizraja8-prog/freecvmakerpk/main/logo.jpg"
)

SAMPLE_CV_URL = (
    "https://raw.githubusercontent.com/"
    "labraizraja8-prog/freecvmakerpk/main/cv.jpeg"
)

WHATSAPP_NUMBER = "923109018979"
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

/* ---------------------------------------------------------
   GLOBAL
--------------------------------------------------------- */

html,
body,
[class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background: #f4f7fb;
    color: #172033;
}

.block-container {
    max-width: 1180px !important;
    padding-top: 28px !important;
    padding-bottom: 35px !important;
}


/* ---------------------------------------------------------
   HEADER
--------------------------------------------------------- */

.header {
    text-align: center;
    margin-bottom: 28px;
}

.header img {
    border-radius: 12px;
}

.header-title {
    color: #172033;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-top: 12px;
    margin-bottom: 7px;
}

.header-title span {
    color: #2563eb;
}

.header-subtitle {
    color: #64748b;
    font-size: 15px;
    line-height: 1.6;
}


/* ---------------------------------------------------------
   TRUST ROW
--------------------------------------------------------- */

.trust-card {
    background: #ffffff;
    border: 1px solid #e5eaf1;
    border-radius: 12px;
    padding: 15px 10px;
    text-align: center;
    min-height: 105px;
}

.trust-icon {
    font-size: 22px;
    margin-bottom: 5px;
}

.trust-title {
    color: #172033;
    font-size: 14px;
    font-weight: 700;
}

.trust-description {
    color: #718096;
    font-size: 11px;
    margin-top: 4px;
}


/* ---------------------------------------------------------
   MAIN CARDS
--------------------------------------------------------- */

.main-card {
    background: #ffffff;
    border: 1px solid #e1e7ef;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
}

.card-heading {
    color: #172033;
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 4px;
}

.card-description {
    color: #718096;
    font-size: 13px;
    line-height: 1.6;
    margin-bottom: 18px;
}


/* ---------------------------------------------------------
   STREAMLIT FORM
--------------------------------------------------------- */

div[data-testid="stForm"] {
    border: none !important;
    background: transparent !important;
    padding: 0 !important;
}


/* ---------------------------------------------------------
   INPUTS
--------------------------------------------------------- */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background: #f8fafc !important;
    border: 1px solid #d7dee8 !important;
    border-radius: 9px !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #172033 !important;
    font-size: 14px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.08) !important;
}

label {
    color: #334155 !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}


/* ---------------------------------------------------------
   GENERATE BUTTON
--------------------------------------------------------- */

.stFormSubmitButton > button {
    width: 100%;
    height: 48px;
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    transition: 0.2s ease;
}

.stFormSubmitButton > button:hover {
    background: #1d4ed8 !important;
    transform: translateY(-1px);
}


/* ---------------------------------------------------------
   SAMPLE CV
--------------------------------------------------------- */

.sample-label {
    display: inline-block;
    background: #eff6ff;
    color: #1d4ed8;
    border: 1px solid #dbeafe;
    border-radius: 6px;
    padding: 5px 9px;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 10px;
}

.sample-notice {
    background: #f8fafc;
    border: 1px solid #e5eaf1;
    border-radius: 9px;
    padding: 11px 12px;
    margin-top: 10px;
    margin-bottom: 15px;
    color: #64748b;
    font-size: 12px;
    line-height: 1.5;
}


/* ---------------------------------------------------------
   WHATSAPP SERVICE CARD
--------------------------------------------------------- */

.service-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 17px;
    margin-top: 18px;
}

.service-title {
    color: #172033;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 5px;
}

.service-description {
    color: #64748b;
    font-size: 12px;
    line-height: 1.55;
    margin-bottom: 12px;
}

.service-price {
    color: #172033;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 12px;
}


/* ---------------------------------------------------------
   WHATSAPP BUTTON
--------------------------------------------------------- */

.stLinkButton > a {
    width: 100% !important;
    background: #16a34a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    min-height: 46px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    transition: 0.2s ease !important;
}

.stLinkButton > a:hover {
    background: #15803d !important;
    transform: translateY(-1px);
}


/* ---------------------------------------------------------
   RESULT
--------------------------------------------------------- */

.result-container {
    background: #ffffff;
    border: 1px solid #dbeafe;
    border-radius: 14px;
    padding: 20px;
    margin-top: 24px;
}

.result-title {
    color: #172033;
    font-size: 19px;
    font-weight: 800;
}

.result-description {
    color: #64748b;
    font-size: 12px;
    margin-top: 3px;
    margin-bottom: 12px;
}

.stDownloadButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 9px !important;
    font-weight: 700 !important;
}


/* ---------------------------------------------------------
   FOOTER
--------------------------------------------------------- */

.footer {
    text-align: center;
    color: #94a3b8;
    border-top: 1px solid #e2e8f0;
    margin-top: 45px;
    padding-top: 20px;
    font-size: 12px;
    line-height: 1.7;
}


/* ---------------------------------------------------------
   MOBILE
--------------------------------------------------------- */

@media (max-width: 768px) {

    .block-container {
        padding: 18px 12px 25px 12px !important;
    }

    .header-title {
        font-size: 30px;
    }

    .header-subtitle {
        font-size: 13px;
    }

    .main-card {
        padding: 18px;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# HEADER
# =========================================================

st.markdown("<div class='header'>", unsafe_allow_html=True)

st.image(LOGO_URL, width=115)

st.markdown(
    """
    <div class="header-title">
        Free <span>CV Maker</span> Pakistan
    </div>

    <div class="header-subtitle">
        Create a professional, ATS-friendly CV with AI —
        quickly, simply and for free.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# TRUST CARDS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">⚡</div>
            <div class="trust-title">Fast</div>
            <div class="trust-description">
                Generate your CV in seconds
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">🎯</div>
            <div class="trust-title">ATS Friendly</div>
            <div class="trust-description">
                Clean professional structure
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">✍️</div>
            <div class="trust-title">Professional</div>
            <div class="trust-description">
                Corporate English writing
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">💯</div>
            <div class="trust-title">Simple</div>
            <div class="trust-description">
                No complicated registration
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# GROQ CLIENT
# =========================================================

try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=groq_api_key)
except Exception:
    client = None


# =========================================================
# MAIN CONTENT
# =========================================================

left, right = st.columns(
    [1.25, 0.95],
    gap="large",
)


# =========================================================
# LEFT: CV FORM
# =========================================================

with left:

    st.markdown(
        """
        <div class="main-card">

            <div class="card-heading">
                📝 Create Your CV
            </div>

            <div class="card-description">
                Enter your details below. The AI will organize
                your information into a professional CV.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("cv_form"):

        name = st.text_input(
            "Full Name *",
            placeholder="Muhammad Ali Khan",
        )

        phone = st.text_input(
            "WhatsApp / Phone Number",
            placeholder="0312-1234567",
        )

        email = st.text_input(
            "Email Address",
            placeholder="muhammad@gmail.com",
        )

        location = st.text_input(
            "City / Location",
            placeholder="Islamabad, Pakistan",
        )

        education = st.text_area(
            "Education *",
            placeholder=(
                "Example:\n"
                "BS Computer Science, University of Punjab, "
                "2020 - 2024"
            ),
            height=90,
        )

        experience = st.text_area(
            "Work Experience",
            placeholder=(
                "Example:\n"
                "Data Entry Operator - XYZ Ltd\n"
                "2022 - 2024\n"
                "Handled data entry and Excel reports."
            ),
            height=120,
        )

        skills = st.text_area(
            "Skills *",
            placeholder=(
                "Example:\n"
                "MS Excel, Python, Communication, "
                "Graphic Design, Teamwork"
            ),
            height=90,
        )

        submit = st.form_submit_button(
            "✨ Generate My CV"
        )


# =========================================================
# GENERATE CV
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
            "GROQ_API_KEY is missing. "
            "Please configure your Streamlit secrets."
        )

    else:

        prompt = f"""
You are a Senior HR Specialist and Professional CV Writer
with more than 15 years of corporate recruitment experience.

Create a professional, ATS-friendly CV in English.

STRICT REQUIREMENTS:

1. Use English only.
2. Never invent information.
3. Never invent employers, job titles, dates,
   qualifications, achievements or certifications.
4. Use only information supplied by the candidate.
5. Do not use placeholders.
6. Do not create tables.
7. Do not mention AI.
8. Do not include references unless provided.
9. Do not include a photo section.
10. Keep the professional summary concise.
11. Use strong professional language where supported
    by the candidate's information.
12. Keep the CV clean and ATS-friendly.
13. Do not exaggerate the candidate's experience.
14. If the candidate has little or no experience,
    create an honest entry-level summary.

USE THIS STRUCTURE:

FULL NAME
Phone | Email | Location

PROFESSIONAL SUMMARY

EDUCATION

WORK EXPERIENCE

SKILLS

CANDIDATE INFORMATION:

Name:
{name}

Phone:
{phone}

Email:
{email}

Location:
{location}

Education:
{education}

Experience:
{experience}

Skills:
{skills}

Return only the final CV.
Do not add explanations before or after the CV.
"""

        with st.spinner(
            "🤖 Creating your professional CV..."
        ):

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert professional "
                                "CV writer. Follow all instructions "
                                "strictly."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                    temperature=0.3,
                    max_tokens=1800,
                )

                generated_cv = (
                    response.choices[0]
                    .message
                    .content
                    .strip()
                )

                st.session_state["generated_cv"] = generated_cv
                st.session_state["cv_name"] = name.strip()

            except Exception as error:

                st.error(
                    "Something went wrong while generating "
                    "your CV. Please try again."
                )

                st.caption(str(error))


# =========================================================
# GENERATED CV RESULT
# =========================================================

if "generated_cv" in st.session_state:

    st.markdown(
        """
        <div class="result-container">

            <div class="result-title">
                ✅ Your CV is Ready
            </div>

            <div class="result-description">
                Your AI-generated CV is shown below.
                You can copy it or download it.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    generated_cv = st.session_state["generated_cv"]

    st.text_area(
        "Generated CV",
        value=generated_cv,
        height=500,
    )

    cv_name = st.session_state.get(
        "cv_name",
        "Professional"
    )

    safe_name = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        cv_name,
    )

    st.download_button(
        "📥 Download My CV",
        data=generated_cv,
        file_name=f"{safe_name}_Professional_CV.txt",
        mime="text/plain",
        use_container_width=True,
    )


# =========================================================
# RIGHT: SAMPLE CV
# =========================================================

with right:

    st.markdown(
        """
        <div class="main-card">

            <div class="sample-label">
                SAMPLE CV
            </div>

            <div class="card-heading">
                📄 Professional CV Example
            </div>

            <div class="card-description">
                This is only a sample showing the type of
                professionally formatted CV we can create
                for you.
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
        <div class="sample-notice">
            ℹ️ <strong>This is a sample CV.</strong><br>
            It is not the CV generated from the form above.
            If you want a professionally designed PDF CV
            like this, contact us on WhatsApp.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # PROFESSIONAL SERVICE
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="service-card">

            <div class="service-title">
                💼 Want a Professional PDF CV?
            </div>

            <div class="service-description">
                We can professionally format your CV and
                provide a clean, job-ready PDF version.
            </div>

            <div class="service-price">
                Rs. 300 per CV
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "💬 Contact on WhatsApp",
        WHATSAPP_URL,
        use_container_width=True,
    )

    st.caption(
        "Click the button above to open WhatsApp."
    )


# =========================================================
# SIMPLE HOW IT WORKS
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center;">
        <div class="card-heading">
            How It Works
        </div>

        <div class="card-description">
            Create your CV in three simple steps.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

s1, s2, s3 = st.columns(3)

with s1:

    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">1️⃣</div>
            <div class="trust-title">
                Enter Your Details
            </div>
            <div class="trust-description">
                Add your education, experience and skills.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s2:

    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">2️⃣</div>
            <div class="trust-title">
                Generate CV
            </div>
            <div class="trust-description">
                AI turns your information into professional
                CV content.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s3:

    st.markdown(
        """
        <div class="trust-card">
            <div class="trust-icon">3️⃣</div>
            <div class="trust-title">
                Download or Contact Us
            </div>
            <div class="trust-description">
                Download your CV or request professional
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
