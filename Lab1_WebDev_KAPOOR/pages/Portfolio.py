import streamlit as st
import streamlit_shadcn_ui as ui
from pathlib import Path
# note to reader - im using shadcn since it aesthically more beautiful than the depressing streamlit vanilla variant

project_folder = Path(__file__).parent.parent
profile_picture = Path(__file__).parent / "sexyimage.png"

# description of pages in my portfolio:S
# 1. home page - houses all info about me, my experience, projects, interests, etc.
# 2. portfolio
# 3. quiz - part 2 of lab

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.set_page_config(
    page_title="Saurish Kapoor",
    page_icon=str(profile_picture),
    layout="wide",
)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        h1 {
            letter-spacing: -0.04em;
        }

        [data-testid = "stImage"] img {
            border-radius: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

about_me = """
I'm a first year ChBE student at Tech interested
in the intersection of atoms (biology) and bits (computation).

I'm a researcher at Weill Cornell Medicine and have previously lead growth at a YC port co, 
and did data engineering work at Princeton University's Dept. of Anthropology. I'm particularly interested in
using using computational tools to answer biologically and medicinally interesting questions to put forward
treatments, and, perhaps, cures to diseases.
"""

linkedin_url = "https://www.linkedin.com/in/saurishkapoor"
github_url = "https://github.com/saurishkapoor"
email_address = "saurishk0508@gmail.com"

education_data = {
    "Degree": "B.Sc Chemical and Biomolecular Engineering",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, Georgia",
    "Graduation": "2030",
}

course_data = [
    {
        "code": "CS 1301",
        "course": "Intro to Computing",
        "area": "Computer Science",
        "skill": "Python",
    },
    {
        "code": "CHEM 1211K",
        "course": "Chem Principles I",
        "area": "Chemistry",
        "skill": "General Chemistry",
    },

    {
        "code": "MATH 1554",
        "course": "Linear Algebra",
        "area": "Mathematics",
        "skill": "Linear Algebra",
    },

    {
        "code": "BIOS 2610",
        "course": "Integrative Genetics",
        "area": "Biology",
        "skill": "Genetics",
    },

    {
        "code": "PUBP 1142",
        "course": "Teams & Collaboration",
        "area": "Leadership",
        "skill": "Collaboration",
    },
]

experience_data = {
    "Researcher * Weill Cornell Medicine": [
        "Solving the last micron of drug delivery",
    ],
    "Venture Partner * Contrary": [
        "Backing founders from pre-seed to pre-IPO.",
    ],
    "Research Assistant * Princeton University": [
        "Data engineering",
    ],
}

projects_data = {
    "DrugGPS": (
        "DL to learn the chemical code governing localization of therapeatuics, engineering them to the correct place in the cell."
    ),
    "FarmHeart": (
        "DL tool for the early, automated, and non-invasive diasstgnosis of cardiovascular disease in cattle."
    ),
}

programming_data = {
    "Cooking": 90,
    "Writing": 50,
    "Python": 95,
}

spoken_data = {
    "English": "Fluent",
    "Hindi": "Fluent",
    "Chiense": "Intermediate",
}


# hero section
image_col, hero_col = st.columns([1, 3], gap="large")

with image_col:
    st.image(str(profile_picture), width=210)

with hero_col:
    st.title("Saurish Kapoor")

    st.markdown("#### Georgia Tech '30 & Weill Cornell Medicine")

    ui.badges(
        [
            ("Georgia Tech", "default"),
            ("Weill Cornell Medicine", "secondary"),
            ("Research", "outline"),
            ("Computational Biology", "outline"),
        ],
        key="hero_badges",
    )

    st.write("")
    linkedin_col, github_col, email_col, spacer = st.columns([1, 1, 1, 2])

    with linkedin_col:
        ui.link_button(
            "LinkedIn",
            linkedin_url,
            variant="default",
            width="stretch",
            key="linkedin_button",
        )

    with github_col:
        ui.link_button(
            "GitHub",
            github_url,
            variant="outline",
            width="stretch",
            key="github_button",
        )

    with email_col:
        ui.link_button(
            "Email",
            f"mailto:{email_address}",
            variant="outline",
            width="stretch",
            key="email_button",
        )

ui.separator(key="hero_separator")

# main

section = ui.tabs(
    options=[
        "About",
        "Experience",
        "Education",
        "Projects",
        "Skills",
    ],
    value="About",
    variant="line",
    width="stretch",
    key="portfolio_navigation",
)


# about me section

if section == "About":

    ui.card(
        about_me,
        key="about_card",
        width="stretch",
    )

    st.write("")

    st.subheader("Areas of Interest")

    ui.badges(
        [
            ("Computational Biology", "secondary"),
            ("Machine Learning", "secondary"),
            ("Biotechnology", "secondary"),
        ],
        key="interest_badges",
    )


# experience section

elif section == "Experience":

    st.subheader("Experience")
    st.caption(
        "Research, technology, and entrepreneurial experience."
    )

    for i, (role, bullets) in enumerate(experience_data.items()):

        content = "\n".join(
            [f"• {bullet}" for bullet in bullets]
        )

        ui.card(
            role,
            content,
            key=f"experience_{i}",
            width="stretch",
        )

        st.write("")


# edcation section

elif section == "Education":

    st.subheader("Education")

    ui.card(
        education_data["Institution"],
        education_data["Degree"],
        (
            f"{education_data['Location']}  +  "
            f"Expected graduation {education_data['Graduation']}"
        ),
        key="education_card",
        width="stretch",
    )

    st.write("")
    st.subheader("Current Coursework")

    ui.table(
        course_data,
        [
            {"key": "code", "label": "Course"},
            {"key": "course", "label": "Name"},
            {"key": "area", "label": "Area"},
            {"key": "skill", "label": "Primary Skill"},
        ],
        caption="Georgia Tech coursework",
        key="course_table",
        max_height=420,
        width="stretch",
    )


# projects
elif section == "Projects":
    st.subheader("Projects")
    project_columns = st.columns(2)
    for i, (project, description) in enumerate(projects_data.items()):
        with project_columns[i % 2]:
            ui.card(
                project,
                description,
                key=f"project_{i}",
                width="stretch",
            )


# listting my skilzzzzz
elif section == "Skills":
    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("Programming")
        for language, proficiency in programming_data.items():
            ui.progress(
                proficiency,
                label=language,
                show_value=True,
                key=f"programming_{language}",
                width="stretch",
            )
            st.write("")

    with right:
        st.subheader("Languages")
        ui.badges(
            [
                (f"{language} · {level}", "outline")
                for language, level in spoken_data.items()
            ],
            key="language_badges",
        )

        st.write("")
        st.subheader("Technical Interests")
        ui.badges(
            [
                ("Computational Biology", "outline"),
                ("Machine Learning", "outline"),
                ("Biotechnology", "outline"),
            ],
            key="technical_badges",
        )


# the footer

st.write("")
st.write("")
ui.separator(key="footer_separator")
footer_left, footer_right = st.columns([3, 1])

with footer_left:
    st.caption(
        "Saurish Kapoor © 2030"
    )
