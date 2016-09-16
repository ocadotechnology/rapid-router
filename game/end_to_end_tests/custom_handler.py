import socket

from django.test import testcases


class RequestHandler(testcases.QuietWSGIRequestHandler):
    def handle(self):
        try:
            super(RequestHandler, self).handle()
        except socket.timeout:
            print('timed out')
            self.requestline = ''
            self.request_version = ''
            self.command = ''
            self.send_error(408)
            return


def monkey_patch():
    testcases.QuietWSGIRequestHandler = RequestHandler
