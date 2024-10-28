import configuration

import requests

import data

def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))