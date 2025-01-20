import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Configure the page to use the whole widescreen
st.set_page_config(page_title="Training Data App 2025", page_icon="📊", layout="wide")

# Load data from the first Google Sheet (workout_details)
sheet_id_workout_details = "11XJvtO2068nqdZhQvo87tDh8WneDH1dQQOQC12dGAYc"
sheet_name_workout_details = "workout_details"
url_workout_details = f"https://docs.google.com/spreadsheets/d/{sheet_id_workout_details}/gviz/tq?tqx=out:csv&sheet={sheet_name_workout_details}"
df_workout_details = pd.read_csv(url_workout_details, dtype=str).fillna("")

# Load data from the second Google Sheet (workout_summary)
sheet_id_workout_summary = "1VHAfQNLvXh9cfSCh9qh1RUgHULYmVAPp7-eHlsLy_H8"
sheet_name_workout_summary = "workout_summary"
url_workout_summary = f"https://docs.google.com/spreadsheets/d/{sheet_id_workout_summary}/gviz/tq?tqx=out:csv&sheet={sheet_name_workout_summary}"
df_workout_summary = pd.read_csv(url_workout_summary, dtype=str).fillna("")

# Load data from the third Google Sheet (fatigue_tracking)
sheet_id_fatigue_tracking = "1Mw9qQ6w5LKFqH5zgRPU-xpEDi1slPJ1waQWO2OCRMK4"
sheet_name_fatigue_tracking = "fatigue_tracking"
url_fatigue_tracking = f"https://docs.google.com/spreadsheets/d/{sheet_id_fatigue_tracking}/gviz/tq?tqx=out:csv&sheet={sheet_name_fatigue_tracking}"
df_fatigue_tracking = pd.read_csv(url_fatigue_tracking, dtype=str).fillna("")

# Title and Introduction
st.title("Training Data Analysis App 2025 📈🏋🏻‍♂️")
st.markdown("This project is a comprehensive nine-month endeavor aimed at tracking and analyzing personal gym training data using Python. The project is designed to showcase data analysis skills. It involves building and maintaining three structured databases that capture various aspects of gym workouts and performance.")

# Sidebar for navigation
st.sidebar.title("Navigation 🗺️")
pages = ["Overview", "Workout Details", "Workout Summary", "Fatigue Tracking", "KPIs"]
page = st.sidebar.radio("Go to", pages)

# Overview page
if page == "Overview":
    tab1, tab2, tab3 = st.tabs(["Project Objectives🎯", "Databases Overview 📑", "Key Performance Indicators (KPIs) ✅"])

    with tab1:
        st.header("Project Objectives🎯",divider="red")
        
        st.subheader("Data Collection📝")
        st.markdown("""

        * **Systematic recording of workout and recovery data over nine months.** 
            * This involves diligently documenting key metrics from each workout session and tracking recovery progress.
            * Consistent data collection is crucial for building a robust and reliable dataset.""")
        
        st.subheader("Data Analysis🧠")
        st.markdown("""

        * **Application of various data analysis techniques to extract meaningful insights.** 
            * This includes:
                * **Trend analysis:** Identifying patterns and changes in workout performance over time.
                * **Progress measurement:** Tracking improvements in strength, endurance, and other fitness goals.
                * **Workout efficiency assessment:** Evaluating the effectiveness of different training programs and identifying areas for optimization.
                * **Other techniques:** Exploratory data analysis, statistical modeling, and machine learning (if applicable).""")
        
        st.subheader("Visualization🔎")
        st.markdown("""
        * **Development of interactive grphics and visualizations using Python libraries.** 
            * **Streamlit:** Building user-friendly web applications to interact with the data and explore insights.
            * **Matplotlib:** Creating a wide range of static, animated, and interactive visualizations.
            * **Plotly:** Generating interactive and visually appealing charts and graphs. 
            * **Effective visualizations:** Present data in a clear, concise, and engaging manner to facilitate understanding and interpretation.
        """)

    with tab2:
        st.header("Databases Overview 📑",divider="red")
        
        st.subheader("1. Workout Details Database📝")
        st.markdown("""

        | Column | Data Type | Description |
        |---|---|---|
        | Timestamp | Timestamp | Date and time of each workout entry |
        | Split | String | Workout split (e.g., Upper/lower, PPL, PPL/Arnold) |
        | Day | String | Day of the week (e.g., Upper 1, Lower 1, Pull Day, Push Day) |
        | Exercise | String | Name of the exercise performed |
        | Set | Integer | Set number within the exercise |
        | Weight | Float | Weight used for the exercise (in pounds) |
        | Reps | Integer | Number of repetitions performed |

        **Purpose:** This database records detailed information about each workout session, including the specific exercises performed, the number of sets and repetitions, and the amount of weight used. It serves as the primary source for tracking workout volume and progression over time.""")

        st.subheader("2. Workout Session Summary Database📖")
        st.markdown("""
        | Column | Data Type | Description |
        |---|---|---|
        | Timestamp | Timestamp | Date and time of the workout session |
        | Calories | Float | Estimated calories burned during the workout |
        | Time Trained | Timedelta | Total duration of the workout session |
        | Time of Day | String | Time of day the workout occurred (e.g., 10:00am, 12:00pm, 8:00pm) |

        **Purpose:** This database summarizes each workout session by capturing active calories burned, total duration, and the time of day the workout occurred. It provides insights into workout efficiency and patterns related to the time of day.""")

        st.subheader("3. Fatigue Tracking Database😴")
        st.markdown("""

        | Column | Data Type | Description |
        |---|---|---|
        | Timestamp | Timestamp | Date after the workout session |
        | Fatigue Level | Integer | Subjective fatigue level on a scale of 1-5 (e.g., 1 = No Fatigue, 5 = Extremely Fatigued) |

        **Purpose:** This database tracks subjective fatigue levels the day after each workout, helping to monitor recovery and assess the impact of different workout intensities on overall fatigue.
        """)
    with tab3:
        st.header("Key Performance Indicators (KPIs) ✅",divider="red")
        st.markdown("""
        **Key Performance Indicators (KPIs)**

        * **Calories Burned per Minute🔥**
            * **Definition:** Evaluates the efficiency of each workout by dividing the total active calories burned by the duration of the workout.
            * **Insights:** Helps identify workouts that are most effective in burning calories per unit of time.
            * **Mathematical Formula:**""")
        st.latex("Calories Burned per Minute=Total Active Calories Burned / Workout Duration in Minutes")

        st.markdown("""
        * **Fatigue Level Post-Workout💪🏼**
            * **Definition:** Tracks the level of fatigue felt the day after a workout, providing insights into recovery and the impact of workout intensity on overall well-being.
            * **Insights:** Helps determine optimal workout intensity and frequency to prevent excessive fatigue and ensure adequate recovery.""")

        st.markdown("""
        * **Exercise Progression Rate📐**
            * **Definition:** Tracks the rate of improvement in strength or endurance for specific exercises over time, measuring how quickly weight or reps are increased.
            * **Insights:** Provides valuable information on training progress and identifies areas where further improvement is needed.
            * **Mathematical Formula:**""")
        st.latex("Progression Rate=Current Weight or Reps−Initial Weight or Reps /Number  of Sessions")

        st.markdown("""
        * **Average Intensity per Session❤️‍🔥**
            * **Definition:** Calculates the average intensity of each workout by dividing the total weight lifted by the total number of sets.
            * **Insights:** Offers insights into workout difficulty and helps identify potential areas for improvement or adjustment in training intensity.
            * **Mathematical Formula:**""")
        st.latex("Average Intensity=Total Weight Lifted / Total Sets")

# Workout Details page
elif page == "Workout Details":
    st.header("Workout Details")
    st.write("Detailed information about each workout session.")
    st.dataframe(df_workout_details)

    # Example visualization
    st.subheader("Exercise Distribution")
    exercise_count = df_workout_details['Exercise'].value_counts()
    st.bar_chart(exercise_count)

# Workout Summary page
elif page == "Workout Summary":
    st.header("Workout Summary")
    st.write("Summary of each workout session.")
    st.dataframe(df_workout_summary)

    # Example visualization
    st.subheader("Calories Burned Over Time")
    df_workout_summary['Timestamp'] = pd.to_datetime(df_workout_summary['Timestamp'])
    fig = px.line(df_workout_summary, x='Timestamp', y='Calories', title='Calories Burned Over Time')
    st.plotly_chart(fig)

# Fatigue Tracking page
elif page == "Fatigue Tracking":
    st.header("Fatigue Tracking")
    st.write("Tracking subjective fatigue levels post-workout.")
    st.dataframe(df_fatigue_tracking)

    # Example visualization
    st.subheader("Fatigue Levels Over Time")
    df_fatigue_tracking['Timestamp'] = pd.to_datetime(df_fatigue_tracking['Timestamp'])
    fig = px.line(df_fatigue_tracking, x='Timestamp', y='Fatigue Level', title='Fatigue Levels Over Time')
    st.plotly_chart(fig)

# KPIs page
elif page == "KPIs":
    st.header("Key Performance Indicators (KPIs)")
    st.markdown("""
    - **Calories Burned per Minute**
    - **Fatigue Level Post-Workout**
    - **Exercise Progression Rate**
    - **Average Intensity per Session**
    """)

    # Example KPI calculation and visualization
    st.subheader("Calories Burned per Minute")
    df_workout_summary['Calories'] = df_workout_summary['Calories'].astype(float)
    df_workout_summary['Time Trained'] = df_workout_summary['Time Trained'].astype(float)
    df_workout_summary['Calories per Minute'] = df_workout_summary['Calories'] / df_workout_summary['Time Trained']
    st.line_chart(df_workout_summary[['Timestamp', 'Calories per Minute']])

# Footer
st.markdown("---")
st.markdown("Developed by Santiago Lara Sabas | 2025")