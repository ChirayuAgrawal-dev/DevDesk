import os
from flask import Flask, render_template_string, request, redirect, jsonify

app = Flask(__name__)
tickets = []
COMMIT = os.getenv("GIT_COMMIT", os.getenv("RENDER_GIT_COMMIT", "local"))[:7]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>DevDesk - IT Support Register</title></head>
<body>
    <h1>DevDesk: Campus IT & Lab Support Register</h1>
    <p>Pending Tickets: <strong>{{ pending }}</strong></p>
    <form method="POST" action="/submit">
        <input name="student_name" placeholder="Your Name" required>
        <input name="lab_number" placeholder="Lab/Room (e.g., Lab 302)" required>
        <input name="issue" placeholder="Describe issue" required>
        <button type="submit">Submit Ticket</button>
    </form>
    <h2>Active Ticket Log</h2>
    <ul>
        {% for t in tickets %}
            <li>#{{ t.id }} - {{ t.student_name }} ({{ t.lab_number }}): {{ t.issue }} [<em>{{ t.status }}</em>]</li>
        {% else %}
            <li>No tickets submitted yet.</li>
        {% endfor %}
    </ul>
    <hr>
    <footer>CI/CD Pipeline Version 1 - commit {{ commit }}</footer>
</body>
</html>
"""

@app.route("/")
def home():
    pending = sum(1 for t in tickets if t["status"] == "Pending")
    return render_template_string(HTML_TEMPLATE, tickets=tickets, pending=pending, commit=COMMIT)

@app.route("/submit", methods=["POST"])
def submit_ticket():
    student_name = request.form.get("student_name", "").strip()
    lab_number = request.form.get("lab_number", "").strip()
    issue = request.form.get("issue", "").strip()
    if not student_name or not lab_number or not issue:
        return "All fields are required", 400
    tickets.append({"id": len(tickets) + 1, "student_name": student_name, "lab_number": lab_number, "issue": issue, "status": "Pending"})
    return redirect("/")

@app.route("/api/tickets")
def api_tickets():
    return jsonify(tickets)

@app.route("/health")
def health():
    return {"status": "ok", "commit": COMMIT}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
