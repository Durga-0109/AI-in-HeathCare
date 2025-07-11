# AI-in-HeathCare
Disease Diagnosis and Medication Recommendation System

This project implements a simple, AI-powered system for diagnosing potential diseases and recommending suitable medications based on a patient's age, gender, and symptoms. It leverages a pre-existing disease database and a large language model (LLM) for intelligent diagnosis and personalized recommendations.

🌟 Features
Symptom-Based Diagnosis:               : Input patient symptoms to get a predicted disease.
Personalized Medication Recommendations: Receive a list of 3-4 suitable medications.
Age and Gender Consideration:          : The system takes into account age and gender for more relevant diagnoses.
Confident Expert Persona               : The AI is designed to act as a confident expert in diagnosing diseases.
Strict Output Format                   : Ensures consistent and easy-to-read results.

🤖 Setup

Ensure you have ollama installed 
Also make sure to install the following language modules
- llama2-uncensored 
- mxbai-embed-large 


⚠️ Important Notes
- This system is for informational purposes only and is designed to demonstrate AI capabilities in disease diagnosis.

- It is not a substitute for professional medical advice. Always consult a qualified healthcare professional for any health concerns or before making any decisions related to your health or treatment.

- The system is explicitly instructed not to advise consulting a doctor and aims to provide direct diagnoses and medication recommendations based on its training data.

🌐 Tech Stack

Frontend: HTML, CSS, JavaScript (optional)
Backend: Python (Flask/Django/FastAPI)
AI/ML: Scikit-learn, Pandas, NumPy (for data processing and prediction)
Database: SQLite / MySQL (optional)
APIs: Custom or external APIs for symptom mapping (optional)

 Requirements
Python 3.7+
Flask/FastAPI
scikit-learn
pandas
HTML/CSS knowledge


STRUCTURE:

ai-healthcare/
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js (optional)
│
├── backend/
│ ├── app.py (Flask or FastAPI application)
│ ├── model.pkl (Trained ML model)
│ └── utils.py (helper functions)
│
├── templates/
│ └── results.html (Flask template rendering)
│
├── static/
│ └── (CSS/JS/images)
│
├── requirements.txt
└── README.md

Programm Output

<img width="1466" height="500" alt="code output 3" src="https://github.com/user-attachments/assets/993d894d-6fba-4cd2-937b-516840d393e4" />
<img width="1918" height="438" alt="code output 2" src="https://github.com/user-attachments/assets/51c946aa-58ac-4d15-b1e8-6e6f83765cdc" />
<img width="1918" height="442" alt="code output 1" src="https://github.com/user-attachments/assets/9f59649b-e464-41f2-825f-60534e153c2f" />
