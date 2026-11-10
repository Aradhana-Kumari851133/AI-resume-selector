import streamlit as st

st.set_page_config(
    page_title="HireSense AI",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0B1020, #111827);
    color: #F8FAFC;
}

/* Header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #29364D;
}

/* Main Headings */
h1, h2, h3 {
    color: #C4B5FD !important;
    font-weight: 700 !important;
}

/* Normal Text */
p, label, .stMarkdown {
    color: #E2E8F0;
}

/* Input Fields */
.stTextInput input,
.stTextArea textarea {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
    border: 1px solid #7C3AED !important;
    border-radius: 10px !important;
}

/* Input Focus */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 1px solid #C084FC !important;
    box-shadow: 0 0 8px #7C3AED55 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #9333EA);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: 700;
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {
    background: linear-gradient(90deg, #9333EA, #A855F7);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px #7C3AED55;
}

/* Metric Cards */
[data-testid="stMetric"] {
    background: #1E293B;
    border: 1px solid #374151;
    padding: 20px;
    border-radius: 14px;
}

/* Metric Values */
[data-testid="stMetricValue"] {
    color: #C4B5FD;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background: #1E293B;
    border: 1px dashed #A78BFA;
    border-radius: 12px;
    padding: 15px;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #1E293B;
    border: 1px solid #374151;
    border-radius: 12px;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #374151;
}

/* Radio Buttons */
.stRadio label {
    color: #E2E8F0 !important;
}

/* Select and Dropdown */
[data-baseweb="select"] > div {
    background-color: #1E293B;
    border-color: #7C3AED;
    color: white;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

st.title("HireSense AI")
st.write("Resume Screening System")


name = st.text_input("Enter your name")

if st.button("Submit name"):

    if name.strip() == "":
        st.error("Please enter your name!")

    else:
        st.success(f"Welcome {name}")

st.subheader("1. Job Description")

job_description = st.text_area(
    "Paste Job Description",
    placeholder="Enter job requirements here...",
    height=200
)

if st.button("Submit job description"):

    if job_description.strip() == "":
        st.error("Please enter the job description!")

    else:
        st.success("Job description submitted successfully!")
        st.write("Your Job Description:")
        st.write(job_description)

st.subheader("2. Upload Candidate Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} resumes uploaded!")

    for file in uploaded_files:
        st.write(file.name)



