
__all__ = [
    'MySpaceError',
    ]

class MySpaceError(Exception):
    def __init__(self, message, http_response=None):
        Exception.__init__(self, message)
        self.http_response = http_response