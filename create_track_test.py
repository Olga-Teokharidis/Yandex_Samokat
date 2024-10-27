import sender_stand_request


def test_response_code():
    track_response = sender_stand_request.get_order()
    assert track_response.status_code == 200


# Ольга Теохаридис, 22-я когорта — Финальный проект. Инженер по тестированию плюс