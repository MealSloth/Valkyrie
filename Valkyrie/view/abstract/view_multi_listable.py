from abc import ABCMeta


class MultiListableView:
    __metaclass__ = ABCMeta

    header = []
    entry = []

    def __init__(self, **kwargs):
        if kwargs.get('header'):
            self.header = kwargs['header']
        if kwargs.get('entry'):
            self.entry = kwargs['entry']

    def get_elements(self):
        response = {}
        if self.header:
            response['header'] = self.header
        if self.entry:
            response['entry'] = self.entry
        return response
