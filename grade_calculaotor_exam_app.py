import streamlit as st

# Set page config with a blue and green theme
st.set_page_config(page_title="Grade Calculator", page_icon="📘", layout="centered")

# Custom CSS for a simple blue and green theme
st.markdown(
    """
    <style>
    body {
        background-color: white;  /* Simple white background */
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: white;
        padding: 20px;
    }
    h1 {
        color: #0066cc;  /* Solid blue */
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 28px;
        margin-bottom: 30px;
    }
    .stNumberInput > div > div > input {
        background-color: #e6f7ff;  /* Light blue background for input fields */
        color: black;
        font-family: 'Arial', sans-serif;
        border: 1px solid #0066cc;  /* Solid blue border */
        padding: 8px;
        width: 100%;
        border-radius: 0px;  /* No rounded corners */
    }
    .stButton button {
        background-color: #28a745;  /* Solid green button */
        color: white;
        padding: 10px 20px;
        border: none;
        font-family: 'Arial', sans-serif;
        border-radius: 0px;  /* No rounded corners */
    }
    .stButton button:hover {
        background-color: #218838;  /* Darker green on hover */
    }
    .stNumberInput div {
        font-family: 'Arial', sans-serif;
        color: black;
        margin-bottom: 15px;  /* Spacing between input fields */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with blue and green theme
st.title("Grade Calculator")

# Function to calculate required midterm and final grades
def calculate_midterm_final(prelim_grade, target_grade):
    prelim_weight = 0.2
    midterm_weight = 0.3
    finals_weight = 0.5

    # Remaining grade needed after prelims
    remaining_grade = target_grade - (prelim_grade * prelim_weight)

    # Let Midterm and Finals have equal contribution
    midterm_needed = remaining_grade / (midterm_weight + finals_weight) * midterm_weight
    final_needed = remaining_grade / (midterm_weight + finals_weight) * finals_weight

    return midterm_needed, final_needed

# Input fields with straightforward design
st.write("### Student Information")

absences = st.number_input("Number of Absences:", min_value=0, step=1)

if absences >= 4:
    st.write("💀 *FAILED due to absences.*")
else:
    st.write("### Grade Inputs")
    
    prelim_exam = st.number_input("Prelim Exam Grade (0-100):", 0.0, 100.0)
    quizzes = st.number_input("Quizzes Grade (0-100):", 0.0, 100.0)
    requirements = st.number_input("Requirements Grade (0-100):", 0.0, 100.0)
    recitation = st.number_input("Recitation Grade (0-100):", 0.0, 100.0)

    # Attendance calculation
    attendance = 100 - (absences * 10)

    # Class standing calculation
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

    # Prelim Grade calculation
    prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

    # Display calculated Prelim Grade
    st.write(f"**Prelim Grade:** {prelim_grade:.2f}")

    # Calculate required midterm and finals to pass or achieve Dean's Lister
    target_pass = 75
    target_deans = 90

    midterm_needed_for_pass, final_needed_for_pass = calculate_midterm_final(prelim_grade, target_pass)
    midterm_needed_for_deans, final_needed_for_deans = calculate_midterm_final(prelim_grade, target_deans)

    # Display required midterm and final grades for passing
    st.write(f"To pass with 75% overall grade, you need a Midterm grade of {midterm_needed_for_pass:.2f} "
             f"and a Final grade of {final_needed_for_pass:.2f}.")
    
    # Display required midterm and final grades for Dean's Lister
    st.write(f"To achieve Dean's Lister status with 90% overall grade, you need a Midterm grade of "
             f"{midterm_needed_for_deans:.2f} and a Final grade of {final_needed_for_deans:.2f}.")
