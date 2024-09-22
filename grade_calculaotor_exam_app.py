import streamlit as st

# Set page configuration with a new icon and centered layout
st.set_page_config(page_title="Grade Calculator", layout="centered")

# Inject modern custom CSS for a sleek theme
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        max-width: 800px;
        margin: auto;
    }
    h1 {
        color: #007BFF;
        text-align: center;
        font-size: 36px;
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }
    .stNumberInput input {
        background-color: #ffffff;
        color: #333;
        font-family: 'Arial', sans-serif;
        border: 1px solid #007BFF;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-family: 'Arial', sans-serif;
        font-size: 16px;
        margin-top: 10px;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stNumberInput div, .stMarkdown {
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .result-text {
        color: #007BFF;
        font-size: 18px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# New title without the laptop icon
st.title("Grade Calculator")

# Function to calculate required midterm and final grades based on the prelim grade and target
def calculate_required_grades(prelim_grade, target_grade):
    prelim_weight, midterm_weight, finals_weight = 0.2, 0.3, 0.5

    # Calculate remaining grade needed
    remaining_grade = target_grade - (prelim_grade * prelim_weight)

    # Calculate the required midterm and final grades
    midterm_needed = (remaining_grade * midterm_weight) / (midterm_weight + finals_weight)
    final_needed = (remaining_grade * finals_weight) / (midterm_weight + finals_weight)

    return midterm_needed, final_needed

# Input fields for absences and grades
absences = st.number_input("Enter number of absences:", min_value=0, step=1)

# Check for failure due to absences
if absences >= 4:
    st.markdown("<p class='result-text'>💀 <strong>FAILED due to absences.</strong></p>", unsafe_allow_html=True)
else:
    # Inputs for grade components
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
    st.markdown(f"<p class='result-text'>Prelim Grade: <strong>{prelim_grade:.2f}</strong></p>", unsafe_allow_html=True)

    # Define target grades for passing and Dean's Lister
    target_pass, target_deans = 75, 90

    # Calculate required grades for passing and Dean's Lister
    midterm_needed_pass, final_needed_pass = calculate_required_grades(prelim_grade, target_pass)
    midterm_needed_deans, final_needed_deans = calculate_required_grades(prelim_grade, target_deans)

    # Display required grades to pass
    st.markdown(f"<p class='result-text'>To pass with a 75% overall grade, you need:</p>"
                f"<p class='result-text'><strong>Midterm grade:</strong> {midterm_needed_pass:.2f}, "
                f"<strong>Final grade:</strong> {final_needed_pass:.2f}</p>", unsafe_allow_html=True)

    # Display required grades for Dean's Lister
    st.markdown(f"<p class='result-text'>To achieve Dean's Lister status with a 90% overall grade, you need:</p>"
                f"<p class='result-text'><strong>Midterm grade:</strong> {midterm_needed_deans:.2f}, "
                f"<strong>Final grade:</strong> {final_needed_deans:.2f}</p>", unsafe_allow_html=True)
