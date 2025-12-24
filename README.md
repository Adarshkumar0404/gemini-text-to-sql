# Gemini Text-to-SQL App

A Streamlit application that converts natural language questions into SQL queries using Google's Gemini Pro/Flash model. It executes these queries on a SQLite database and displays the results in a user-friendly format.

## Features
- **Natural Language to SQL:** Convert English questions (e.g., "Who is the manager?") into executable SQL queries.
- **Gemini Powered:** Uses Google's `gemini-1.5-flash` for high-accuracy query generation.
- **Instant Execution:** Automatically executes the generated SQL on a local SQLite database (`Naresh_it_employee.db`).
- **Clean UI:** Built with Streamlit for a simple, interactive interface.
- **No SQL Knowledge Required:** Users can retrieve data without writing a single line of code.

## Tech Stack
- **Python** (Programming Language)
- **Streamlit** (Frontend Framework)
- **Google Generative AI** (LLM for SQL generation)
- **SQLite** (Database)
