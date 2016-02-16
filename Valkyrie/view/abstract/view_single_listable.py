from abc import ABCMeta


class SingleListableView:
    __metaclass__ = ABCMeta

    image = []
    id = []
    info = []
    id_pool = []
    widget = []
    listable = []

    def __init__(self, image, id, info, id_pool, widget, listable):
        self.image = image
        self.id = id
        self.info = info
        self.id_pool = id_pool
        self.widget = widget
        self.listable = listable

    def get_elements(self):
        return {
            'image': self.image,
            'id': self.id,
            'info': self.info,
            'id_pool': self.id_pool,
            'widget': self.widget,
            'listable': self.listable,
        }
