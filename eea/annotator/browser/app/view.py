""" Browser controllers
"""
import json
from zope.interface import implements
from Products.Five.browser import BrowserView
from zope.publisher.interfaces import IPublishTraverse

def jsonify(obj, response=None, status=None):
    """ Convert obj to JSON
    """
    if response:
        response.setHeader("Content-type", "application/json")
        if status:
            response.setStatus(status)
    return json.dumps(obj)

class AnnotationsVerify(BrowserView):
    """ Verify
    """
    def __call__(self, **kwargs):
        print kwargs
        return True

class Annotations(BrowserView):
    """ Read
    """
    implements(IPublishTraverse)

    def __init__(self, context, request):
        super(Annotations, self).__init__(context, request)
        if not hasattr(self.context.__class__, "_verifyObjectPaste"):
            self.context.__class__._verifyObjectPaste = (
                lambda self, object, validate_src=1: True)

    def publishTraverse(self, REQUEST, name):
        """ Custom traverser
        """
        return self.read

    def read(self, **kwargs):
        """ Read
        """
        return jsonify({'name': 'a', 'text': 'A'}, self.request.response)

    def index(self, **kwargs):
        """ Index
        """
        return jsonify([], self.request.response)

    def create(self, **kwargs):
        """ Create
        """
        return self.request.response.redirect(
            '/'.join((self.context.absolute_url(), self.__name__, 'a'))
        )

    def update(self, **kwargs):
        """ Update
        """
        return self.request.response.redirect(
            '/'.join((self.context.absolute_url(), self.__name__, 'a'))
        )

    def delete(self, **kwargs):
        """ Delete
        """
        return jsonify(None, self.request.response, 204)

    def __call__(self, **kwargs):
        method = self.request.method
        if method == 'GET':
            return self.index()
        elif method == 'POST':
            return self.create()
        elif method == 'PUT':
            return self.update()
        elif method == 'DELETE':
            return self.delete()
        return jsonify("Bad request", self.request.response, 400)

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
