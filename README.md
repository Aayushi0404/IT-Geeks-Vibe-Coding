The Rulebook That Argues With Itself

Author: Aayushi Verma

Institution: Shri G.S. Institute of Technology & Science (SGSITS), Indore

Branch: Computer Science and Engineering

Submission: Vibe Coding Round - IT Geeks AI Developer Role

Project Overview

I built this project for Problem Statement 1. It is an intelligent document retrieval and verification system designed to read a 6,000-word university rulebook and handle internal contradictions. Instead of a generic chatbot response, I evaluated questions against the entire corpus and strictly classified them into three deterministic states: ANSWERED, NOT_COVERED, and CONTRADICTION.

Why Standard RAG Fails and My Solution

Traditional vector-based RAG pipelines break down on rulebooks because chunk retrieval grabs the first matching paragraph and stops, missing conflicting rules hidden chapters later. 
To solve this, I used Full-Context Parsing with JSON Enforced Schemas. I leveraged Gemini's massive context capacity to analyze the entire 6,000-word rulebook in a single pass. I used JSON-enforced output formatting to lock the model outputs into the three required states and set the temperature to zero to eliminate hallucinations.

Project Structure

- app.py: Streamlit dashboard featuring a split-screen view, interactive chat, and my integrated Live Eval Dashboard in the sidebar.
- generate_data.py: Automated generator that compiles an authentic SGSITS rulebook embedding three deliberate contradictions.
- eval.py: Standalone Python script executing an automated 25-question test bank.
- rulebook.md: The generated regulation text corpus.
- requirements.txt: Python libraries needed to run the project.

Setup and Local Execution

1. Clone the repository.
2. Install dependencies by running: pip install -r requirements.txt
3. Generate the regulation corpus by running: python generate_data.py
4. Configure the API Key in app.py.
5. Run the dashboard by running: streamlit run app.py

Evaluation and Metrics
To measure accuracy, I built an automated test harness. You can run the eval.py script via terminal or click the Run Live Eval button directly inside the Streamlit sidebar to check performance against edge cases.
