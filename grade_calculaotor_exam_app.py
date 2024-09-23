import streamlit as st

# Set page configuration without an icon
st.set_page_config(page_title="Grade Calculator", layout="centered")

# Apply custom styles for a terminal-like theme
st.markdown(
    """
    <style>
    body {
        background-color: black;
        font-family: 'Courier New', monospace;
    }
    .main {
        background-color: black;
    }
    h1 {
        color: #00FF00;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 30px;
        text-shadow: 0px 0px 5px #00FF00;
    }
    .stNumberInput > div > div > input {
        background-color: #333333;
        color: #00FF00;
        font-family: 'Courier New', monospace;
        border: 2px solid #00FF00;
    }
    .stButton button {
        background-color: black;
        color: #00FF00;
        border-radius: 0;
        padding: 10px 20px;
        border: 2px solid #00FF00;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 5px #00FF00;
    }
    .stButton button:hover {
        background-color: #333333;
        color: #00FF00;
    }
    .stNumberInput div {
        font-family: 'Courier New', monospace;
        color: #00FF00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title of the app
st.title("Grade Calculator")

# Function to calculate midterm and final grades based on prelim grade and target
def calculate_grades(prelim_grade, target_grade, prelim_weight=0.2, midterm_weight=0.3, finals_weight=0.5):
    remaining_grade = target_grade - (prelim_grade * prelim_weight)
    midterm_needed = (remaining_grade / (midterm_weight + finals_weight)) * midterm_weight
    final_needed = (remaining_grade / (midterm_weight + finals_weight)) * finals_weight
    return midterm_needed, final_needed

# Collect input for number of absences
absences = st.number_input("Enter number of absences: ", min_value=0, step=1)

# Check if the student fails due to excessive absences
if absences >= 4:
    st.write("💀 *FAILED due to absences.*")
else:
    # Input fields for grade components
    prelim_exam = st.number_input("Enter Prelim Exam Grade (0-100): ", 0.0, 100.0)
    quizzes = st.number_input("Enter Quizzes Grade (0-100): ", 0.0, 100.0)
    requirements = st.number_input("Enter Requirements Grade (0-100): ", 0.0, 100.0)
    recitation = st.number_input("Enter Recitation Grade (0-100): ", 0.0, 100.0)

    # Calculate attendance score
    attendance = 100 - (absences * 10)

    # Calculate class standing score
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

    # Calculate the prelim grade
    prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

    # Display the prelim grade
    st.write(f"*Prelim Grade:* {prelim_grade:.2f}")

    # Define target grades for passing and Dean's Lister
    target_pass = 75
    target_deans = 90

    # Calculate midterm and finals grades required for passing and Dean's Lister
    midterm_for_pass, final_for_pass = calculate_grades(prelim_grade, target_pass)
    midterm_for_deans, final_for_deans = calculate_grades(prelim_grade, target_deans)

    # Display results for passing grade requirement
    st.write(f"To pass with 75% overall grade, you need a Midterm grade of {midterm_for_pass:.2f} "
             f"and a Final grade of {final_for_pass:.2f}.")

    # Display results for Dean's Lister grade requirement
    st.write(f"To achieve Dean's Lister status with 90% overall grade, you need a Midterm grade of "
             f"{midterm_for_deans:.2f} and a Final grade of {final_for_deans:.2f}.")
