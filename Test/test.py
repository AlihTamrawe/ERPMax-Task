from pathlib import Path

resources = Path(__file__).parent / "resources"

def test_add_product(client):
    response = client.post("/create_product/", data={
        "p_name": "t-shirt",
        "loca_id": 5,
    })
    assert response.status_code == 200

test_add_product()