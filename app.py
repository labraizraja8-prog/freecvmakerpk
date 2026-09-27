import re
from textwrap import dedent

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
# PREMIUM LIGHT THEME
# =========================================================

st.markdown(
    dedent(
        """
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
        );

        /* ==============================
           GLOBAL
        ============================== */

        html, body, [class*="css"] {
            font-family: "Inter", sans-serif;
        }

        .stApp {
            background: #f7f9fc;
            color: #172033;
        }

        .block-container {
            max-width: 1160px !important;
            padding-top: 28px !important;
            padding-bottom: 35px !important;
        }

        /* Hide Streamlit decoration */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            background: transparent !important;
        }


        /* ==============================
           HERO
        ============================== */

        .hero {
            text-align: center;
            padding: 5px 10px 28px 10px;
        }

        .hero-title {
            color: #172033;
            font-size: 40px;
            font-weight: 800;
            letter-spacing: -1.2px;
            margin-top: 12px;
            margin-bottom: 8px;
            line-height: 1.15;
        }

        .hero-title span {
            color: #2563eb;
        }

        .hero-subtitle {
            color: #64748b;
            font-size: 15px;
            line-height: 1.6;
            max-width: 680px;
            margin: 0 auto;
        }


        /* ==============================
           TRUST CARDS
        ============================== */

        .trust-card {
            background: #ffffff;
            border: 1px solid #e7ebf2;
            border-radius: 14px;
            padding: 18px 10px;
            text-align: center;
            min-height: 104px;
            box-shadow: 0 3px 12px rgba(15, 23, 42, 0.035);
        }

        .trust-icon {
            font-size: 23px;
            margin-bottom: 5px;
        }

        .trust-title {
            color: #172033;
            font-size: 14px;
            font-weight: 700;
        }

        .trust-text {
            color: #7b8798;
            font-size: 11px;
            margin-top: 5px;
        }


        /* ==============================
           PREMIUM CONTAINERS
        ============================== */

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #ffffff !important;
            border: 1px solid #e4e9f0 !important;
            border-radius: 16px !important;
            box-shadow: 0 5px 22px rgba(15, 23, 42, 0.045) !important;
        }


        /* ==============================
           SECTION HEADINGS
        ============================== */

        .section-title {
            color: #172033;
            font-size: 21px;
            font-weight: 800;
            margin-bottom: 4px;
        }

        .section-text {
            color: #718096;
            font-size: 13px;
            line-height: 1.6;
            margin-bottom: 15px;
        }


        /* ==============================
           FORM
        ============================== */

        div[data-testid="stForm"] {
            border: none !important;
            background: transparent !important;
            padding: 0 !important;
        }


        /* ==============================
           INPUT FIELDS
        ============================== */

        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #fbfcfe !important;
            border: 1px solid #dce2ea !important;
            border-radius: 9px !important;
        }

        div[data-baseweb="input"] > div:hover,
        div[data-baseweb="textarea"] > div:hover {
            border-color: #b9c4d3 !important;
        }

        div[data-baseweb="input"] > div:focus-within,
        div[data-baseweb="textarea"] > div:focus-within {
            border-color: #60a5fa !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.08) !important;
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="textarea"] textarea {
            color: #172033 !important;
            font-size: 14px !important;
        }

        label {
            color: #334155 !important;
            font-size: 13px !important;
            font-weight: 600 !important;
        }


        /* ==============================
           GENERATE BUTTON
        ============================== */

        .stFormSubmitButton > button {
            width: 100%;
            min-height: 48px;
            background: #2563eb !important;
            color: white !important;
            border: none !important;
            border-radius: 9px !important;
            font-size: 15px !important;
            font-weight: 700 !important;
            box-shadow: 0 5px 14px rgba(37, 99, 235, 0.18);
            transition: all 0.2s ease;
        }

        .stFormSubmitButton > button:hover {
            background: #1d4ed8 !important;
            transform: translateY(-1px);
            box-shadow: 0 7px 18px rgba(37, 99, 235, 0.24);
        }


        /* ==============================
           SAMPLE BADGE
        ============================== */

        .sample-badge {
            display: inline-block;
            background: #eff6ff;
            color: #2563eb;
            border: 1px solid #dbeafe;
            border-radius: 6px;
            padding: 5px 9px;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 0.4px;
            margin-bottom: 9px;
        }


        /* ==============================
           SAMPLE NOTICE
        ============================== */

        .sample-notice {
            background: #f8fafc;
            border: 1px solid #e5eaf0;
            border-radius: 9px;
            padding: 11px 13px;
            margin-top: 10px;
            color: #64748b;
            font-size: 12px;
            line-height: 1.55;
        }

        .sample-notice strong {
            color: #334155;
        }


        /* ==============================
           SERVICE CARD
        ============================== */

        .service-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 11px;
            padding: 16px;
            margin-top: 16px;
        }

        .service-title {
            color: #172033;
            font-size: 15px;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .service-text {
            color: #64748b;
            font-size: 12px;
            line-height: 1.55;
            margin-bottom: 10px;
        }

        .service-price {
            color: #2563eb;
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 12px;
        }


        /* ==============================
           WHATSAPP BUTTON
        ============================== */

        .stLinkButton > a {
            width: 100% !important;
            min-height: 45px !important;
            background: #16a34a !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 9px !important;
            font-size: 14px !important;
            font-weight: 700 !important;
            text-decoration: none !important;
            box-shadow: 0 4px 12px rgba(22, 163, 74, 0.14);
            transition: all 0.2s ease !important;
        }

        .stLinkButton > a:hover {
            background: #15803d !important;
            transform: translateY(-1px);
        }


        /* ==============================
           RESULT AREA
        ============================== */

        .result-box {
            background: #ffffff;
            border: 1px solid #dbeafe;
            border-radius: 14px;
            padding: 17px;
            margin-top: 25px;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.045);
        }

        .result-title {
            color: #172033;
            font-size: 18px;
            font-weight: 800;
        }

        .result-text {
            color: #64748b;
            font-size: 12px;
            margin-top: 3px;
        }

        .stDownloadButton > button {
            width: 100%;
            min-height: 45px;
            border-radius: 9px !important;
            font-weight: 700 !important;
        }


        /* ==============================
           FOOTER
        ============================== */

        .footer {
            text-align: center;
            border-top: 1px solid #e4e9f0;
            margin-top: 45px;
            padding-top: 20px;
            color: #94a3b8;
            font-size: 12px;
            line-height: 1.7;
        }


        /* ==============================
           MOBILE
        ============================== */

        @media (max-width: 768px) {

            .block-container {
                padding: 18px 12px 25px 12px !important;
            }

            .hero-title {
                font-size: 30px;
            }

            .hero-subtitle {
                font-size: 13px;
            }

        }

        </style>
        """
    ),
    unsafe_allow_html=True,
)


# =========================================================
# HERO
# =========================================================

st.markdown('<div class="hero">', unsafe_allow_html=True)

st.image(LOGO_URL, width=105)

st.markdown(
    dedent(
        """
        <div class="hero-title">
            Free <span>CV Maker</span> Pakistan
        </div>
        <div class="hero-subtitle">
            Create a professional, ATS-friendly CV with AI —
            quickly, simply and for free.
        </div>
        """
    ),
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# TRUST CARDS
# =========================================================

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">⚡</div>
                <div class="trust-title">Fast</div>
                <div class="trust-text">
                    Generate your CV in seconds
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

with t2:
    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">🎯</div>
                <div class="trust-title">ATS Friendly</div>
                <div class="trust-text">
                    Clean professional structure
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

with t3:
    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">✍️</div>
                <div class="trust-title">Professional</div>
                <div class="trust-text">
                    Corporate English writing
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

with t4:
    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">✓</div>
                <div class="trust-title">Simple</div>
                <div class="trust-text">
                    No complicated registration
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# GROQ CLIENT
# =========================================================

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception:
    client = None


# =========================================================
# MAIN COLUMNS
# =========================================================

left, right = st.columns(
    [1.25, 0.95],
    gap="large",
)


# =========================================================
# LEFT COLUMN
# =========================================================

with left:

    with st.container(border=True):

        st.markdown(
            dedent(
                """
                <div class="section-title">
                    📝 Create Your CV
                </div>

                <div class="section-text">
                    Enter your details below. Our AI will turn
                    your information into professional CV content.
                </div>
                """
            ),
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
# CV GENERATION
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
            "GROQ_API_KEY is missing. "
            "Please configure it in Streamlit Secrets."
        )

    else:

        prompt = f"""
You are a Senior HR Specialist and Professional CV Writer
with more than 15 years of corporate recruitment experience.

Create a professional, ATS-friendly CV in English.

STRICT REQUIREMENTS:

1. English only.
2. Never invent information.
3. Never invent employers, job titles, dates,
   qualifications, achievements or certifications.
4. Use only information supplied by the candidate.
5. Never use placeholder text.
6. Do not use tables.
7. Do not mention AI.
8. Do not include references unless provided.
9. Do not include a photo section.
10. Keep the professional summary concise.
11. Use strong professional language where supported.
12. Keep the CV clean and ATS-friendly.
13. Do not exaggerate experience.
14. If the candidate has little or no experience,
    create an honest entry-level summary.

STRUCTURE:

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

Return ONLY the final CV.
Do not add explanations before or after it.
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
# GENERATED RESULT
# =========================================================

if "generated_cv" in st.session_state:

    st.markdown(
        dedent(
            """
            <div class="result-box">
                <div class="result-title">
                    ✅ Your CV is Ready
                </div>
                <div class="result-text">
                    Review your AI-generated CV below.
                    You can copy or download it.
                </div>
            </div>
            """
        ),
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
        "Professional",
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
# RIGHT COLUMN - SAMPLE CV
# =========================================================

with right:

    with st.container(border=True):

        st.markdown(
            dedent(
                """
                <div class="sample-badge">
                    SAMPLE CV
                </div>

                <div class="section-title">
                    📄 Professional CV Example
                </div>

                <div class="section-text">
                    This image is only an example of a
                    professionally formatted CV.
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        st.image(
            SAMPLE_CV_URL,
            use_container_width=True,
        )

        st.markdown(
            dedent(
                """
                <div class="sample-notice">
                    ℹ️ <strong>This is a sample CV.</strong><br>
                    This is not the CV generated from the form.
                    If you want a professionally designed PDF
                    CV like this, contact us on WhatsApp.
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            dedent(
                """
                <div class="service-card">

                    <div class="service-title">
                        💼 Professional CV Formatting
                    </div>

                    <div class="service-text">
                        Want your CV professionally designed
                        and formatted into a clean, job-ready
                        PDF?
                    </div>

                    <div class="service-price">
                        Rs. 300 per CV
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )

        st.link_button(
            "💬 Contact on WhatsApp",
            WHATSAPP_URL,
            use_container_width=True,
        )

        st.caption(
            "Click above to open WhatsApp."
        )


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    dedent(
        """
        <div style="text-align:center;">
            <div class="section-title">
                How It Works
            </div>

            <div class="section-text">
                Create your professional CV in three simple steps.
            </div>
        </div>
        """
    ),
    unsafe_allow_html=True,
)

h1, h2, h3 = st.columns(3)

with h1:

    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">1️⃣</div>
                <div class="trust-title">
                    Enter Your Details
                </div>
                <div class="trust-text">
                    Add your education, experience and skills.
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

with h2:

    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">2️⃣</div>
                <div class="trust-title">
                    Generate Your CV
                </div>
                <div class="trust-text">
                    AI organizes your information professionally.
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

with h3:

    st.markdown(
        dedent(
            """
            <div class="trust-card">
                <div class="trust-icon">3️⃣</div>
                <div class="trust-title">
                    Download or Contact Us
                </div>
                <div class="trust-text">
                    Download your CV or request PDF formatting.
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    dedent(
        """
        <div class="footer">
            <strong>Free CV Maker Pakistan</strong><br>
            AI-Powered Professional CV Generation
            <br><br>
            © 2026 Free CV Maker Pakistan. All rights reserved.
        </div>
        """
    ),
    unsafe_allow_html=True,
)
