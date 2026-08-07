import streamlit as st
import pandas as pd
import json
import os

# --- FILE CONFIGURATION ---
DATA_FILE = "habits_data.json"
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# --- DATA STORAGE FUNCTIONS ---
def load_data():
    """Loads habit data from a local JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    # Default initial data if file doesn't exist
    return {
        "Drink Water": {day: False for day in DAYS_OF_WEEK},
        "Exercise": {day: False for day in DAYS_OF_WEEK},
        "Read 10 Pages": {day: False for day in DAYS_OF_WEEK}
    }

def save_data(data):
    """Saves habit data to a local JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- INITIALIZE SESSION STATE ---
if "habits" not in st.session_state:
    st.session_state.habits = load_data()

# --- APP LAYOUT ---
st.set_page_config(page_title="Weekly Habit Tracker", layout="wide")
st.title(" Weekly Habit Tracker")
st.write("Track your consistency and build better routines every day.")

# --- SIDEBAR: ADD & DELETE HABITS ---
with st.sidebar:
    st.header("Manage Habits")
    
    # Add a new habit
    new_habit = st.text_input("Create a new habit:", placeholder="e.g., Meditate")
    if st.button("Add Habit", use_container_width=True):
        if new_habit.strip() and new_habit not in st.session_state.habits:
            st.session_state.habits[new_habit] = {day: False for day in DAYS_OF_WEEK}
            save_data(st.session_state.habits)
            st.success(f"Added: '{new_habit}'")
            st.rerun()
        elif new_habit in st.session_state.habits:
            st.warning("This habit already exists!")
            
    st.write("---")
    
    # Delete an existing habit
    if st.session_state.habits:
        habit_to_delete = st.selectbox("Select a habit to remove:", list(st.session_state.habits.keys()))
        if st.button("Delete Habit", type="primary", use_container_width=True):
            del st.session_state.habits[habit_to_delete]
            save_data(st.session_state.habits)
            st.success(f"Removed: '{habit_to_delete}'")
            st.rerun()
    else:
        st.write("No habits available to delete.")

# --- MAIN DASHBOARD: HABIT GRID ---
if not st.session_state.habits:
    st.info("Your tracker is empty! Use the sidebar to add your first habit. ")
else:
    st.subheader("Your Weekly Progress")
    
    # Create the grid headers (Habit Name + Days of the week + Progress)
    cols = st.columns([2] + [1] * 7 + [1.5])
    
    cols[0].write("**Habit**")
    for i, day in enumerate(DAYS_OF_WEEK):
        cols[i+1].write(f"**{day[:3]}**")  # Displays Mon, Tue, Wed...
    cols[-1].write("**Completion**")
    st.write("---")

    # Render a row for each habit
    for habit_name, days in list(st.session_state.habits.items()):
        row_cols = st.columns([2] + [1] * 7 + [1.5])
        
        # Column 0: Habit Name
        row_cols[0].write(f"**{habit_name}**")
        
        # Columns 1 to 7: Checkboxes for days
        completed_days = 0
        for i, day in enumerate(DAYS_OF_WEEK):
            # Unique key for each checkbox to prevent Streamlit rendering conflicts
            cb_key = f"cb_{habit_name}_{day}"
            
            # Render checkbox and listen for user clicks
            is_checked = row_cols[i+1].checkbox("", value=days[day], key=cb_key, label_visibility="collapsed")
            
            # If the user toggled the checkbox, update state and save file immediately
            if is_checked != days[day]:
                st.session_state.habits[habit_name][day] = is_checked
                save_data(st.session_state.habits)
                st.rerun()
                
            if is_checked:
                completed_days += 1
        
        # Column 8: Progress metric and bar
        success_rate = int((completed_days / 7) * 100)
        row_cols[-1].metric(label="Done", value=f"{success_rate}%", delta=f"{completed_days}/7 Days")
        row_cols[-1].progress(completed_days / 7)
        st.write("---")

    # --- RESET BUTTON ---
    if st.button("Clear Week / Reset All Checkboxes"):
        for habit_name in st.session_state.habits:
            st.session_state.habits[habit_name] = {day: False for day in DAYS_OF_WEEK}
        save_data(st.session_state.habits)
        st.success("All habits reset for a fresh week!")
        st.rerun()