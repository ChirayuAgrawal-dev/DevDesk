from app import app, tickets

def client():
    app.config["TESTING"] = True
    tickets.clear()
    return app.test_client()

def test_health_check():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_submit_valid_ticket():
    c = client()
    response = c.post("/submit", data={"student_name": "Chirayu", "lab_number": "Lab 501", "issue": "Monitor power issue"})
    assert response.status_code == 302
    assert len(c.get("/api/tickets").json) == 1

def test_submit_invalid_ticket_rejected():
    res = client().post("/submit", data={"student_name": "", "lab_number": "Lab 501", "issue": ""})
    assert res.status_code == 400
