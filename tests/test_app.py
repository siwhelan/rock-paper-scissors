from app import app


#  test route '/' returns 200
def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200

