import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit as st

st.title("What Type of Scientist Are You?")

st.write("Answer these questions to find out whether you are more interested in biology, chemistry, or computer science!")

# Question 1
q1 = st.radio(  # NEW
    "1. What is the most interesting class out of the following to you?",
    ["Biology", "Chemistry", "Computer Science"]
)

# Question 2
q2 = st.selectbox(  # NEW
    "2. You want to:",
    ["Study cells", "Mix chemicals", "Write code"]
)

# Question 3
q3 = st.slider(  # NEW
    "3. Do you like working with technology?",
    1, 5
)

# Question 4
q4 = st.radio(
    "4. You would rather work at a:",
    ["Biology lab", "Chemistry lab", "Tech company"]
)

# question 5
q5 = st.number_input("5. How many hours per week would you spend conducting experiments or writing code?", min_value=0, max_value=20, value=5
                     )

current_folder = Path(__file__).parent
st.image(current_folder / "biologist.jpg")  # NEW
st.image(current_folder / "chemist.jpg")
st.image(current_folder / "computer.jpg")

biology = 0
chemistry = 0
computer_science = 0


if q1 == "Biology":
    biology += 1
elif q1 == "Chemistry":
    chemistry += 1
else:
    computer_science += 1


if q2 == "Study cells":
    biology += 1
elif q2 == "Mix chemicals":
    chemistry += 1
else:
    computer_science += 1


if q3 >= 4:
    computer_science += 1
elif q3 <= 2:
    biology += 1
else:
    chemistry += 1


if q4 == "Biology lab":
    biology += 1
elif q4 == "Chemistry lab":
    chemistry += 1
else:
    computer_science += 1

if q5 >= 10:
    computer_science += 1
else:
    biology += 1


if st.button("See My Result"):
    if biology >= chemistry and biology >= computer_science:
        st.write("Youre a biologist!")
        st.write("You enjoy learning about living things.")
    elif chemistry >= biology and chemistry >= computer_science:
        st.write("You are a Chemist!")
        st.write("You enjoy learning about molecules.")
    else:
        st.write("You are a Computer Scientist!")
        st.write("You enjoy coding and are great at CS 1301!!!!!")

    st.balloons()  # NEW
