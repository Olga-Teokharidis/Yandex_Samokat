import sender_stand_request

import data

def new_track():
    response_track = sender_stand_request.new_order(data.order_body)
    track = response_track.json()['track']
    return track

def positive_assert():
    track = new_track()
    status_response = sender_stand_request.get_order(track)
    assert status_response.status_code == 200

def test_get_order_by_track():
    positive_assert()


# Ольга Теохаридис, 22-я когорта — Финальный проект. Инженер по тестированию плюс