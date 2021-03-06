import logging

class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request url={} body={}".format(response.request.url, response.request.body))
        logging.info("Request status_code={} body={}".format(response.status_code, response.text))
        self._response = response

    def status_code(self, code):
        logging.info(f"Status code should be {code}")
        return self._response.status_code == code

    def field(self, name):
        return self._response.json()[name]