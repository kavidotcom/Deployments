from hello import app
import pytest

@pytest.fixture
def run():
    return app.test_client()


def test_home(run):
    response = run.get('/home')
    assert response.status_code == 200
    assert response.json == {'message': 'Welcome to the Loan Prediction API!'}

def test_predict(run):
    payload = { "Gender": "Male", "Married": "Unmarried",   "LoanAmount": 500000000, "ApplicantIncome": 50000, "Credit_History": "Cleared Debts" }    
    response = run.post('/predict', json=payload)
    assert response.status_code == 200