import streamlit as st
import pandas as pd

# Define grading logic
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# App Page Configurations
st.set_page_config(page_title="Student Mark Analyzer", layout="wide")
st.title(" Student Mark List Analyzer")
st.write("Enter student names and marks below to calculate totals, averages, grades, and class analytics.")

# Initialize session state for storing student data safely across web reruns
if "student_data" not in st.session_state:
    st.session_state.student_data = []

# Sidebar for inputs
st.sidebar.header(" Input Student Data")

student_name = st.sidebar.text_input("Student Name", placeholder="e.g. John Doe")
math_mark = st.sidebar.number_input("Math Marks", min_value=0, max_value=100, value=0)
science_mark = st.sidebar.number_input("Science Marks", min_value=0, max_value=100, value=0)
english_mark = st.sidebar.number_input("English Marks", min_value=0, max_value=100, value=0)

# Button to append new record
if st.sidebar.button(" Add Student"):
    if student_name.strip() == "":
        st.sidebar.error("Please enter a valid student name.")
    else:
        # Data processing logic
        total = math_mark + science_mark + english_mark
        average = round(total / 3, 2)
        grade = calculate_grade(average)
        
        # Save record
        st.session_state.student_data.append({
            "Student Name": student_name,
            "Math": math_mark,
            "Science": science_mark,
            "English": english_mark,
            "Total": total,
            "Average": average,
            "Grade": grade
        })
        st.sidebar.success(f"Added {student_name} successfully!")

# Actions to clear data
if st.session_state.student_data:
    if st.sidebar.button(" Clear All Data"):
        st.session_state.student_data = []
        st.rerun()

# Main Display Logic
if st.session_state.student_data:
    # Convert list of dicts to a Dataframe
    df = pd.DataFrame(st.session_state.student_data)
    
    # 1. Main Mark Sheet Table
    st.subheader(" Student Mark Sheet")
    st.dataframe(df, use_container_width=True)
    
    # Export to CSV option
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Download Report as CSV",
        data=csv,
        file_name="student_marks_report.csv",
        mime="text/csv",
    )
    
    # 2. Performance Summary Analytics
    st.markdown("---")
    st.subheader(" Class Performance Analytics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        st.metric("Class Average Score", f"{round(df['Average'].mean(), 2)}%")
    with col3:
        top_student = df.loc[df['Total'].idxmax()]['Student Name']
        top_score = df['Total'].max()
        st.metric("Class Topper", f"{top_student} ({top_score} pts)")
    with col4:
        pass_count = len(df[df['Grade'] != 'F'])
        st.metric("Passing Students", f"{pass_count} / {len(df)}")

    # 3. Graphical Insights
    st.subheader(" Subject-wise Comparison")
    chart_data = df.set_index("Student Name")[["Math", "Science", "English"]]
    st.bar_chart(chart_data)

else:
    st.info("No data added yet. Use the sidebar menu to start adding students!")