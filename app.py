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
# PREMIUM LIGHT CSS
# =========================================================

st.markdown(
    """
<style>

/* =====================================================
   GENERAL
===================================================== */

.stApp {
    background: #f6f8fc;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hide unnecessary Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* =====================================================
   TEXT
===================================================== */

h1 {
    color: #172033 !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #172033 !important;
    font-weight: 700 !important;
}

p {
    color: #64748b;
}


/* =====================================================
   NATIVE CONTAINERS
===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e5eaf1 !important;
    border-radius: 16px !important;
    box-shadow: 0 6px 24px rgba(15, 23, 42, 0.045) !important;
}


/* =====================================================
   INPUTS
===================================================== */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background: #fbfcfe !important;
    border: 1px solid #dce2ea !important;
    border-radius: 9px !important;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #60a5fa !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.08) !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #172033 !important;
}

label {
    color: #334155 !important;
    font-weight: 600 !important;
}


/* =====================================================
   GENERATE BUTTON
===================================================== */

.stFormSubmitButton > button {
    width: 100%;
    min-height: 48px;
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 15px rgba(37, 99, 235, 0.18);
}

.stFormSubmitButton > button:hover {
    background: #1d4ed8 !important;
}


/* =====================================================
   WHATSAPP BUTTON
===================================================== */

.stLinkButton > a {
    width: 100% !important;
    min-height: 46px !important;
    background: #16a34a !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 15px rgba(22, 163, 74, 0.15);
}

.stLinkButton > a:hover {
    background: #15803d !important;
}


/* =====================================================
   DOWNLOAD BUTTON
===================================================== */

.stDownloadButton > button {
    width: 100%;
    min-height: 46px;
    border-radius: 9px !important;
    font-weight: 700 !important;
}


/* =====================================================
   SAMPLE IMAGE
===================================================== */

.sample-image {
    border-radius: 10px;
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    h1 {
        font-size: 30px !important;
    }

}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# HEADER
# =========================================================

header_col = st.columns([1, 2, 1])

with header_col[1]:

    st.image(
        LOGO_URL,
        width=105,
    )

    st.markdown(
        "<h1 style='text-align:center;'>"
        "Free <span style='color:#2563eb;'>CV Maker</span> Pakistan"
        "</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "Create a professional, ATS-friendly CV with AI — "
        "quickly, simply and for free."
        "</p>",
        unsafe_allow_html=True,
    )


st.write("")


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
# GROQ
# =========================================================

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception:
    client = None


# =========================================================
# MAIN AREA
# =========================================================

form_column, sample_column = st.columns(
    [1.25, 0.95],
    gap="large",
)


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
                    "BS Computer Science - University of Punjab\n"
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
                    "Handled daily data entry and Excel reports."
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
                "✨ Generate My Free CV"
            )


# =========================================================
# AI CV GENERATION
# =========================================================

if submit:

    errors = []

    if not name.strip():
        errors.append(
            "Please enter your full name."
        )

    if not education.strip():
        errors.append(
            "Please enter your education."
        )

    if not skills.strip():
        errors.append(
            "Please enter your skills."
        )

    if errors:

        for error in errors:
            st.error(error)

    elif client is None:

        st.error(
            "GROQ_API_KEY is not configured. "
            "Please add it to Streamlit Secrets."
        )

    else:

        prompt = f"""
You are a Senior HR Specialist and Professional CV Writer.

Create a clean, professional and ATS-friendly CV
in English using ONLY the information provided below.

STRICT RULES:

1. English only.
2. Never invent information.
3. Never invent companies.
4. Never invent job titles.
5. Never invent dates.
6. Never invent qualifications.
7. Never invent achievements.
8. Never invent certifications.
9. Never use placeholder information.
10. Do not use tables.
11. Do not mention AI.
12. Do not add references unless provided.
13. Do not add a photo section.
14. Do not exaggerate experience.
15. Keep the professional summary concise.
16. Use professional action verbs when appropriate.
17. Keep the final CV clean and ATS-friendly.

FORMAT:

FULL NAME
Phone | Email | Location

PROFESSIONAL SUMMARY

EDUCATION

WORK EXPERIENCE

SKILLS

Candidate information:

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

Return ONLY the final CV.
Do not write any explanation before or after the CV.
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
                    response
                    .choices[0]
                    .message
                    .content
                    .strip()
                )

                st.session_state["generated_cv"] = generated_cv
                st.session_state["cv_name"] = name.strip()

            except Exception as error:

                st.error(
                    "CV generation failed. "
                    "Please try again."
                )

                st.caption(
                    str(error)
                )


# =========================================================
# GENERATED CV
# =========================================================

if "generated_cv" in st.session_state:

    st.write("")

    with st.container(border=True):

        st.subheader(
            "✅ Your Free CV is Ready"
        )

        st.caption(
            "This is your AI-generated text CV. "
            "You can copy it or download it."
        )

        generated_cv = (
            st.session_state["generated_cv"]
        )

        st.text_area(
            "Your CV",
            value=generated_cv,
            height=500,
        )

        cv_name = st.session_state.get(
            "cv_name",
            "Professional",
        )

        safe_name = re.sub(
            r"[^a-zA-Z0-9_-]",
            "_",
            cv_name,
        )

        st.download_button(
            "📥 Download My Free CV",
            data=generated_cv,
            file_name=(
                f"{safe_name}_Professional_CV.txt"
            ),
            mime="text/plain",
            use_container_width=True,
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
                padding:5px 10px;
                background:#eff6ff;
                color:#2563eb;
                border:1px solid #dbeafe;
                border-radius:6px;
                font-size:11px;
                font-weight:700;
            ">
                SAMPLE ONLY
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.subheader(
            "📄 Professional CV Design"
        )

        st.caption(
            "The CV below is only a sample of our "
            "professional formatting service."
        )

        st.image(
            SAMPLE_CV_URL,
            use_container_width=True,
        )

        st.info(
            "ℹ️ This is a SAMPLE CV. "
            "It is not the result generated by the "
            "free AI CV maker."
        )

        st.markdown("---")

        st.markdown(
            "### 💼 Want a CV Like This?"
        )

        st.write(
            "If you want your CV professionally "
            "designed and formatted as a polished "
            "PDF, contact us on WhatsApp."
        )

        st.markdown(
            "### **Rs. 300 per CV**"
        )

        st.link_button(
            "💬 Contact Us on WhatsApp",
            WHATSAPP_URL,
            use_container_width=True,
        )

        st.caption(
            "Click the button to open WhatsApp."
        )


# =========================================================
# SIMPLE INFORMATION SECTION
# =========================================================

st.write("")
st.write("")


info1, info2, info3 = st.columns(3)

with info1:
    with st.container(border=True):
        st.markdown("### 1️⃣")
        st.markdown("**Enter Your Information**")
        st.caption(
            "Add your education, experience and skills."
        )

with info2:
    with st.container(border=True):
        st.markdown("### 2️⃣")
        st.markdown("**AI Creates Your CV**")
        st.caption(
            "Your information is converted into professional text."
        )

with info3:
    with st.container(border=True):
        st.markdown("### 3️⃣")
        st.markdown("**Need a Designed PDF?**")
        st.caption(
            "Contact us on WhatsApp for professional formatting."
        )


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
        font-size:12px;
        line-height:1.7;
    ">
        <strong>Free CV Maker Pakistan</strong><br>
        AI-Powered Professional CV Generation<br><br>
        © 2026 Free CV Maker Pakistan. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True,
)
