import streamlit as st
import sqlite3
import google.generativeai as genai
import os 
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()

# Configure GenAI Key
gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = gemini_api_key)

# Function to get response from Gemini
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        # Added error handling so the app shows why it failed
        st.error(f"SQL Error: {e}") 
        return []

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Naresh_it_employee and has the following columns - employee_name, 
    employee_role, employee_salary \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM Naresh_it_employee ;
    \nExample 2 - Tell me all the employees working in Data Science role?, 
    the SQL command will be something like this SELECT * FROM Naresh_it_employee 
    where employee_role="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App
st.set_page_config(page_title = "I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ",key = "input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    # Get the raw response from Gemini
    response = get_gemini_response(question, prompt)
    print(f"Raw Gemini Response: {response}")
    
    # CLEANING THE RESPONSE (Crucial Step)
    cleaned_sql = response.strip().replace("```sql", "").replace("```", "").replace("\n", " ")
    
    # Execute SQL
    data = read_sql_query(cleaned_sql, "Naresh_it_employee.db")
    
    st.subheader("The Response is")
    
    # Display data as a readable table instead of giant headers
    if data:
        for row in data:
            row_text = " | ".join (map(str, row))

            # Display the clean text without any index numbers
            st.write(row_text)

            st.divider()
    else:
        st.write("No data found or query failed.")