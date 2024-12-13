from dotenv import load_dotenv # type: ignore
# load all the environment variables
load_dotenv()

import streamlit as st #type: ignore
import os
import sqlite3
import google.generativeai as genai #type: ignore

# configure api key
genai.configure(api_key=os.getenv("AIzaSyDsHDA4Dq9xCxRa4yx0Sk2jRTpI9yh4jFs"))#type: ignore

# Define Prompt
prompt = ['''You are an expert in converting English questions to SQL queries!. 
          The SQl Database has Name VARCHAR(25) , Class VARCHAR(25) , Section VARCHAR(25) , 
          Marks INT). For example : if a user asks how many entries or records present in an 
          SQL Database , the sql command will be somethong like Select count(*) from student. 
          Example 2: Tell me all the students studying in Data Science class ? the sql query 
          should be like select * from student where class = 'Data Science'.Also SQL query should not 
          have ``` in the beginning or end and SQL word in the output. Please please remove ``` symbol from
          starting and end of the sql query Example : if we get the output as  "```sql
SELECT
  Name,
  Class,
  Section,
  Marks
FROM Student
WHERE
  (
    Class,
    Section
  ) IN (
    SELECT
      Class,
      Section
    FROM Student
    GROUP BY
      Class,
      Section
    ORDER BY
      Marks DESC
    LIMIT 2
  )
ORDER BY
  Marks DESC;
```" then please remove the additional symbols and provide the results as :
SELECT
  Name,
  Class,
  Section,
  Marks
FROM Student
WHERE
  (
    Class,
    Section
  ) IN (
    SELECT
      Class,
      Section
    FROM Student
    GROUP BY
      Class,
      Section
    ORDER BY
      Marks DESC
    LIMIT 2
  )
ORDER BY
  Marks DESC;  ''']

# Function to load google gemini model and provide SQL query as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(([prompt[0],question]))
    return response.text

# Function to retrieve the query from the database i.e Take SQL query as input hit the DB and provide the response

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# # create a streamlit app
# st.set_page_config(page_title = "I can retrieve any sql query")
# st.header("Let English Drive Your SQL Searches")
# question = st.text_input("Input: ",key="input")
# submit = st.button("Ask the question")

# # if submit button is clicked
# if submit:
#     response = get_gemini_response(question,prompt)
#     print(response)
#     data = read_sql_query(response,"Student.db")
#     st.subheader("The response is : ")
#     for row in data:
#         print(row)
#         st.header(row)

import streamlit as st
import sqlite3
import pandas as pd
from io import BytesIO

# Function to run the query on the database
def read_sql_query(query, database):
    try:
        conn = sqlite3.connect(database)
        data = pd.read_sql_query(query, conn)
        conn.close()
        return data
    except Exception as e:
        return str(e)

# Function to create an Excel file from the dataframe
import pandas as pd
import io

def create_excel_download(data):
    # Create a BytesIO stream
    output = io.BytesIO()

    # Write data to the Excel file using pd.ExcelWriter
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        data.to_excel(writer, index=False, sheet_name='Sheet1')
        # Save and close the writer
        writer.close()

    # Seek the start of the stream to allow reading
    output.seek(0)

    return output


# Streamlit App Setup
st.set_page_config(page_title="I can retrieve any SQL query", page_icon="📊")
st.header("💡 Let English Drive Your SQL Searches")

# Input Section
question = st.text_input("Input your question: ", key="input")
submit = st.button("Ask the question")

# If submit button is clicked
if submit:
    # Assuming `get_gemini_response` generates the SQL query
    response = get_gemini_response(question, prompt)
    
    if response:
        st.subheader("Generated SQL Query:")
        st.code(response, language="sql")  # Display the generated query
        
        # Fetch data from the database
        data = read_sql_query(response, "Student.db")
        
        if isinstance(data, pd.DataFrame) and not data.empty:
            st.subheader("The response is:")
            st.dataframe(data, use_container_width=True)  # Display results in a table

            # Provide Excel download option
            excel_data = create_excel_download(data)
            st.download_button(
                label="📥 Download Results as Excel",
                data=excel_data,
                file_name="query_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("Query returned no results or there was an error in the SQL query.")
    else:
        st.error("Failed to generate an SQL query from the input.")


