# AI_SQL_Workflow
 Let English Drive Your SQL Queries
 
 💡 Natural Language to SQL Query Generator
Effortlessly convert English questions into SQL queries and fetch results directly from your database. This application leverages Google Gemini AI for generating SQL queries and provides a seamless way to retrieve and export query results.

🌟 Features
Natural Language to SQL Conversion: Translates user input into optimized SQL queries using AI.
Interactive Query Execution: Executes SQL queries on a SQLite database and displays results.
Export to Excel: Download query results as an Excel file for offline use.
User-Friendly Interface: Built with Streamlit for an intuitive and interactive experience.
🛠️ Tech Stack
Python: Core programming language.
Streamlit: For building the web interface.
SQLite: Lightweight database for query execution.
Google Gemini AI: To generate SQL queries from natural language prompts.
Pandas: For data manipulation and display.
🚀 How It Works
Input a Question: Enter a natural language question in the Streamlit app.
Generate SQL Query: AI generates a SQL query based on your question.
Fetch Data: The SQL query is executed on the SQLite database, and the results are displayed.
Download Results: Option to export query results as an Excel file.
🖥️ Usage Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/repo-name.git  
cd repo-name  
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt  
3. Configure Environment Variables
Create a .env file in the project directory and add your Google Gemini AI API key:

dotenv
Copy code
GOOGLE_API_KEY=your_api_key_here  
4. Run the Application
bash
Copy code
streamlit run app.py  
5. Interact with the App
Input questions like:
"How many records are present in the database?"
"Show all students in the Data Science class."
View query results instantly and download them as Excel files.
📂 Project Structure
bash
Copy code
📁 repo-name  
├── app.py                   # Main Streamlit app  
├── requirements.txt         # Python dependencies  
├── .env                     # Environment variables  
└── README.md                # Project documentation  
📷 Screenshots
1. App Interface
Example of the interactive question input and query results display.

🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

📄 License
This project is licensed under the MIT License.

✨ Future Enhancements
Add support for other databases (e.g., MySQL, PostgreSQL).
Improve AI-generated query accuracy for complex questions.
Add user authentication for enhanced security.
