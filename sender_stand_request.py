import configuration

import requests

import data

def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

response = new_order(data.order_body)
new_track = str(response.json()['track'])

def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + new_track)