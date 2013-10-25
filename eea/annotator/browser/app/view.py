""" Browser controllers
"""
import json
from zope.interface import Interface
from Products.Five.browser import BrowserView

class Storage(BrowserView):
    """ Annotator storage
    """
    def jsonify(self, obj, status=None):
        """ JSON
        """
        self.request.response.setHeader("Content-type", "application/json")
        if status:
            self.request.response.setStatus(status)
        return json.dumps(obj)

    def create(self, **kwargs):
        """ Add inline comment
        """
        kwargs.update(self.request.form)
        return self.jsonify("create: not implemented yet", 501)

    def read(self, **kwargs):
        """ Read inline comments
        """
        kwargs.update(self.request.form)
        return self.jsonify("read: not implemented yet", 501)

    def update(self, **kwargs):
        """ Update inline comment
        """
        kwargs.update(self.request.form)
        return self.jsonify("update: not implemented yet", 501)

    def delete(self, **kwargs):
        """ Delete inline comment
        """
        kwargs.update(self.request.form)
        return self.jsonify("delete: not implemented yet", 501)

    def search(self, **kwargs):
        """ Search
        """
        kwargs.update(self.request.form)
        return self.jsonify("search: not implemented yet", 501)
