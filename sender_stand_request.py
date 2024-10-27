import configuration

import requests

import data

def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

order_response = new_order(data.order_body)

def get_order(track_order):
    return requests.get(configuration.URL_SERVICE+configuration.ORDERS_TRACK,
                        params=track_order)
