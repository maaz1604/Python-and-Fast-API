from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test home api
def test_home():
    response = client.get('/')
    #status code check
    assert response.status_code == 200
    # checking data
    assert response.json()== {'message':'Hello bhai!'}
    
#test add api
def test_add():
    response=client.get("/add?a=5&b=8")
    assert response.status_code == 200
    assert response.json()=={'result':13}