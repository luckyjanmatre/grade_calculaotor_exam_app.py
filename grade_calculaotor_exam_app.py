import streamlit as st

# Set page configuration with a custom icon and layout
st.set_page_config(page_title="Grade Calculator", page_icon="💻", layout="centered")

# Inject custom CSS for a hacker-style theme
st.markdown(
    """
    <style>
    body {
        background-color: black;
        font-family: 'Courier New', monospace;
    }
    .stApp {
        background-color: black;
    }
    h1 {
        color: #00FF00;
        text-align: center;
        font-size: 30px;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 5px #00FF00;
    }
    .stNumberInput input {
        background-color: #333333;
        color: #00FF00;
        font-family: 'Courier New', monospace;
        border: 2px solid #00FF00;
    }
    .stButton button {
        background-color: black;
        color: #00FF00;
        border: 2px solid #00FF00;
        padding: 10px 20px;
        font-family: 'Courier New', monospace;
        text-shadow: 0px 0px 5px #00FF00;
    }
    .stButton button:hover {
        background-color: #333333;
    }
    .stNumberInput div, .stMarkdown {
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True
)

# Hacker-themed title
st.title("💻 Grade Calculator")

# Function to calculate required midterm and final grades based on the prelim grade and target
def calculate_required_grades(prelim_grade, target_grade):
    prelim_weight, midterm_weight, finals_weight = 0.2, 0.3, 0.5

    # Calculate remaining grade needed
    remaining_grade = target_grade - (prelim_grade * prelim_weight)

    # Calculate the required midterm and final grades
    midterm_needed = (remaining_grade * midterm_weight) / (midterm_weight + finals_weight)
    final_needed = (remaining_grade * finals_weight) / (midterm_weight + finals_weight)

    return midterm_needed, final_needed

# Number of absences input
absences = st.number_input("Enter number of absences:", min_value=0, step=1)

# Check for failing due to absences
if absences >= 4:
    st.markdown("💀 *FAILED due to absences.*")
else:
    # Input for various grade components
    prelim_exam = st.number_input("Enter Prelim Exam Grade (0-100):", 0.0, 100.0)
    quizzes = st.number_input("Enter Quizzes Grade (0-100):", 0.0, 100.0)
    requirements = st.number_input("Enter Requirements Grade (0-100):", 0.0, 100.0)
    recitation = st.number_input("Enter Recitation Grade (0-100):", 0.0, 100.0)

    # Calculate attendance grade
    attendance = max(0, 100 - absences * 10)

    # Calculate class standing
    class_standing = 0.4 * quizzes + 0.3 * requirements + 0.3 * recitation

    # Calculate Prelim Grade
    prelim_grade = 0.6 * prelim_exam + 0.1 * attendance + 0.3 * class_standing

    # Display the Prelim Grade
    st.markdown(f"*Prelim Grade:* **{prelim_grade:.2f}**")

    # Define target grades for passing and Dean's Lister
    target_pass, target_deans = 75, 90

    # Calculate required grades for passing and Dean's Lister
    midterm_needed_pass, final_needed_pass = calculate_required_grades(prelim_grade, target_pass)
    midterm_needed_deans, final_needed_deans = calculate_required_grades(prelim_grade, target_deans)

    # Display the required grades to pass
    st.markdown(f"To pass with a 75% overall grade, you need a Midterm grade of **{midterm_needed_pass:.2f}** "
                f"and a Final grade of **{final_needed_pass:.2f}**.")

    # Display the required grades for Dean's Lister
    st.markdown(f"To achieve Dean's Lister status with a 90% overall grade, you need a Midterm grade of "
                f"**{midterm_needed_deans:.2f}** and a Final grade of **{final_needed_deans:.2f}**.")
