# Code-Alpha-Task-03
Bug Bounty

# 🛡️ Bug Bounty Reporting Flask App  

## 📌 Overview  
This is a Flask-based web application designed to log and display security vulnerabilities found on various websites. The project was developed in a **WSL (Windows Subsystem for Linux) environment** and includes **10 simulated security flaws** for demonstration.

## 🚀 Features  
- Add & display common **security vulnerabilities** (XSS, SQL Injection, CSRF, etc.).  
- Simple **Flask web interface** with a form for reporting vulnerabilities.  
- Runs on `127.0.0.1:5000` with **debug mode enabled** for local development.  

## 📁 Project Structure  
bug_bounty/ │── app.py # Main Flask application │── templates/ │ ├── report.html # HTML template for displaying vulnerabilities │── static/ # Static assets (CSS, JS) │── venv/ # Virtual environment (excluded in repo) │── README.md # Project documentation


## ⚙️ Installation  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/bug_bounty_flask.git
   cd bug_bounty_flask

2. **Set Up a Virtual Environment**
  python3 -m venv venv
  source venv/bin/activate

3. **Install Dependencies**
  pip install -r requirements.txt

4. **Run the Application**
  python app.py

5. **Access the Web App**
  Open your browser and go to http://127.0.0.1:5000


🛠️ Troubleshooting
WSL Path Issues: Use cd /mnt/c/Users/YourUsername/Desktop/bug_bounty to access the correct folder.
Flask Debugging: If the app doesn't update changes, restart Flask with CTRL+C and python app.py.


📢 Future Improvements
Connect to a database for persistent vulnerability storage.
Implement user authentication for better reporting.
Add real-time vulnerability scanning features.

