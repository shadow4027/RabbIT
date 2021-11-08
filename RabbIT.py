import requests
import bs4


class Pando:

    def __init__(self, username='', password=''):
        self.WebSession = requests.Session()
        self.WebSession.get("")


PanSesh = Pando("hello", "world")