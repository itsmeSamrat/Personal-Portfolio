from pathlib import Path
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Samrat Thapa"
PAGE_ICON = ":wave:"
NAME = "Samrat Thapa"
headline = """ ML/AI Engineer | Data Analyst | Data Science | Expertise in Python, R, ML, & Cloud Computing | Proficient in Data Visualization & Database Management | Open for challenging opportunities |"""
DESCRIPTION = """
Committed Data Scientist and Data Analyst with a keen interest in leveraging advanced technologies to drive impactful solutions. 
With over 2+ years of experience in ML, AI, Python and SQL, I have successfully helped companies enhance their operations and achieve their goals by harnessing the power of data and AI.
"""
EMAIL = "tsamrath40@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/itsmesamrat/",
    "GitHub": "https://github.com/itsmeSamrat",
    "Medium": "https://medium.com/@itsmeSamrat",
}
PROJECTS = {
    "🏆 AI Engineer | Skinopathy | Major Research Project | Toronto, Ontario, Canada | 4 months": "https://www.linkedin.com/in/itsmesamrat/",
    "🏆 Data Analyst | Beenova AI | Major Research Project | Toronto, Canada | 6 months": "https://www.linkedin.com/in/itsmesamrat/",
    "🏆 EDA-on-Seattle-Airbnb-Data": "https://github.com/itsmeSamrat/EDA-on-Seattle-Airbnb-Data",
    "🏆 CreditCardFraudAnalysis-Using-Pytorch": "https://github.com/itsmeSamrat/CreditCardFraudAnalysis-Using-Pytorch",
    "🏆 Eye-Classification": "https://github.com/itsmeSamrat/Eye-Classification",
    "🏆 Sentiment-Analysis-of-Amazon-App-Reviews-using-Azure-Services": "https://github.com/itsmeSamrat/Sentiment-Analysis-of-Amazon-App-Reviews-using-Azure-Services",
    "🏆 Iris-Data-Splitting-Experiment": "https://github.com/itsmeSamrat/Iris-Data-Splitting-Experiment",
    "🏆 German-Credit-Card-Assessment-A-Streamlit-Based-App": "https://github.com/itsmeSamrat/German-Credit-Card-Assessment-A-Streamlit-Based-App",
    "🏆 RawDataToPredictiveModel-Red-Wine-Quality": "https://github.com/itsmeSamrat/RawDataToPredectiveModel-Red-Wine-Quality",
    "🏆 MLJAR - AutoML": "https://github.com/itsmeSamrat/MLJAR-AutoML",
}

CERTIFICATE = {
    "📜 AWS Academy Graduate - AWS Academy Cloud Foundations": "https://www.credly.com/badges/a7ed94e2-8e94-429d-b3eb-f20104160d4e/linked_in_profile",
    "📜 AWS Academy Graduate - AWS Academy Machine Learning Foundations": "https://www.credly.com/badges/1a90355b-2ff6-468b-9685-c60a3e47956e/linked_in_profile",
    "📜 Machine Learning | Stanford University": "https://www.coursera.org/account/accomplishments/verify/5QDWPRFMLT7N?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course",
    "📜 Data Science Math Skills | Duke University": "https://www.coursera.org/account/accomplishments/verify/CPP688LG4EGL?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course",
    "📜 Genomics Data Science with Galaxy": "https://www.coursera.org/account/accomplishments/certificate/JV2RG6CC4ZHK",
    "📜 Algorithms for DNA Sequencing": "https://www.coursera.org/account/accomplishments/certificate/XPFPKKAR57KT",
    "📜 Command Line Tools for Genomic Data Science ": "https://www.coursera.org/account/accomplishments/certificate/CYSKLYNSHU2B",
    "📜 How to Write and Publish a Scientific Paper ": "https://www.coursera.org/account/accomplishments/certificate/GAHFA5QH9WAK",
    "📜 Applied Analytics Using SAS Enterprise Miner": "https://www.credly.com/badges/3a4285f5-c4a4-4789-be12-e39d87bb33bd?source=linked_in_profile",
    "📜 Personal & Family Financial Planning": "https://www.coursera.org/account/accomplishments/certificate/YPJXCVTHBA78",
}

lottie_file_education = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_4rq0nvpt.json")

lottie_file_connect = load_lottieurl(
    'https://assets7.lottiefiles.com/temp/lf20_U1CPFF.json')

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ------  Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #586e75;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certificate">Certificate</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image(profile_pic, width=230)
    st.write(headline)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Skills ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python, R, SAS, Hadoop, PySpark
- 📊 Data Visualization: Power BI, Tableau, Plotly, Matplotlib, Seaborn
- 📚 Modeling: Scikit-learn, Keras, TensorFLow, PyTorch
- 🗄️ Databases:  SQL, MongoDB, Cassandra
- ☁️ Cloud Computing: Azure, AWS
- 🌐 Deployment: Flask, Azure MachineLearning Studio, Streamlit
- ⚡ Version Control: Git and Github
- 🖥️ Front End: HTML, CSS, JS
- 🗃️ Data Handling:  Pandas, Excel, Selenium, BeautifulSoup
"""
)





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- Education

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.write('\n')
    st.subheader("Education")

    # --- education 1
    st.write("🏅", "**Artificial Intelligence – AIDI**")
    st.write("Georgian College • Dec 2022 • 89.94%")

    # --- education 2
    st.write('\n')
    st.write("🏅", "**Big Data Analytics - BDAT**")
    st.write("Georgian College • Dec 2021 • 90.58%")

    # --- education 3
    st.write('\n')
    st.write("🏅", "**B. Tech in Biotechnology**")
    st.write("Kathmandu University • Nov 2019 • 81%")

with col2:
    st_lottie(lottie_file_education, height=300, key='education')

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")


# --- JOB 1
st.write('\n')
st.write("👨🏻‍💻", "**Cygnus Tech Nepal | Jr. Data Analyst**")
st.write("July 2020 - Dec 2020 | Kathmandu, Nepal |")
st.write(
    """
- ✔️ Successfully collected data through web scraping for research and client needs.
- ✔️ Revamped client’s dashboards, resulting in a `20% increase in satisfaction and a 15% improvement in issue resolution`.
- ✔️ Designed and implemented ETL (Extract, Transform, Load) operations that significantly improved workflow and efficiency, resulting in a `5X increase and reducing repetitive tasks`. These optimizations streamlined data processing and contributed to overall productivity and effectiveness.
- ✔️ Developed user-friendly websites using WordPress, leveraging my skills in HTML, CSS, and JavaScript.
"""
)

# --- JOB 2
st.write('\n')
st.write("👨🏻‍💻", "**National Academy of Science and Technology | Biotechnology Laboratory Assistant**")
st.write("March 2018 - Aug 2018 | Internship | Kathmandu, Nepal |")
st.write(
    """
- ✔️ Involved in the assessment of the `antimicrobial, antifungal, antioxidant activity, and dye extraction` of the endophytic fungi isolated from Rhododendron spp. and mushroom.
- ✔️ `PCR amplification` of its ITS region
"""
)

# --- Certificate---
st.write('\n')
st.subheader("Certificate")
for certificate, link in CERTIFICATE.items():
    st.write(f"[{certificate}]({link})")

# ---- CONTACT ----
with st.container():
    st.header("Let's CONNECT")

    contact_form = """
    <form action="https://formsubmit.co/itsmesamratthapa@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_file_connect, height=300, key='connect')
