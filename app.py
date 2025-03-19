from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated vulnerabilities (with random website URLs)
vulnerabilities = [
    {"name": "Cross-Site Scripting", "description": "Reflected XSS vulnerability on example.com", "url": "http://example1.com"},
    {"name": "SQL Injection", "description": "SQL injection vulnerability on example2.com", "url": "http://example2.com"},
    {"name": "Cross-Site Request Forgery", "description": "CSRF vulnerability on example3.com", "url": "http://example3.com"},
    {"name": "Directory Traversal", "description": "Directory traversal vulnerability on example4.com", "url": "http://example4.com"},
    {"name": "Insecure Cookie", "description": "Insecure cookie storage on example5.com", "url": "http://example5.com"},
    {"name": "Remote Code Execution", "description": "Remote code execution vulnerability on example6.com", "url": "http://example6.com"},
    {"name": "Broken Authentication", "description": "Broken authentication on example7.com", "url": "http://example7.com"},
    {"name": "Sensitive Data Exposure", "description": "Sensitive data exposure on example8.com", "url": "http://example8.com"},
    {"name": "Security Misconfiguration", "description": "Security misconfiguration on example9.com", "url": "http://example9.com"},
    {"name": "Broken Access Control", "description": "Broken access control on example10.com", "url": "http://example10.com"}
]

@app.route("/", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        # Get data from the form
        vuln_name = request.form.get("vuln_name")
        vuln_description = request.form.get("vuln_description")
        vuln_url = request.form.get("vuln_url")
        
        # Add the new vulnerability to the list
        vulnerabilities.append({"name": vuln_name, "description": vuln_description, "url": vuln_url})
    
    return render_template("report.html", vulnerabilities=vulnerabilities)

if __name__ == "__main__":
    app.run(debug=True)
