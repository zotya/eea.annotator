""" Browser controllers
"""
import json
import logging
from zope.interface import implements, implementer
from zope.component import queryMultiAdapter
from Products.Five.browser import BrowserView
from zope.publisher.interfaces import IPublishTraverse
from eea.annotator.browser.interfaces import IAnnotatorAPI
from eea.annotator.browser.interfaces import IAnnotatorAnnotations

logger = logging.getLogger('eea.annotator')


def jsonify(obj, response=None, status=None):
    """ Convert obj to JSON
    """
    if response:
        response.setHeader("Content-type", "application/json")
        if status:
            response.setStatus(status)
    return json.dumps(obj)


class API(BrowserView):
    """ EEA Annotator API
    """
    implements(IAnnotatorAPI)

    def __getattr__(self, name):
        """ Override get annotations attr
        """
        if name == 'annotations' and self.request.method in ('PUT', 'DELETE'):
            return queryMultiAdapter((self, self.request), name=u'annotations')
        return super(API, self).__getattr__(name)

    def absolute_url(self, *args, **kwargs):
        """ Absolute url
        """
        return u'/'.join((
            self.context.absolute_url(*args, **kwargs), self.__name__
        ))

    def PUT(self, REQUEST, RESPONSE):
        """ do nothing
        """
        return

    def __call__(self, **kwargs):
        return jsonify({
            "name": "EEA Annotator Store API",
            "version": "1.0"
            }, self.request.response)

@implementer(IPublishTraverse)
class Annotations(BrowserView):
    """ Annotator Storage
    """
    implements(IAnnotatorAnnotations)

    def PUT(self, REQUEST, RESPONSE):
        """ Do nothing
        """
        return

    def read(self, **kwargs):
        """ Read
        """
        logger.debug('read')
        return jsonify({'name': 'a', 'text': 'A'}, self.request.response)

    def index(self, **kwargs):
        """ Index
        """
        logger.debug("index")
        return jsonify([], self.request.response)

    def create(self, **kwargs):
        """ Create
        """
        logger.debug("create")
        return self.read()

    def update(self, **kwargs):
        """ Update
        """
        logger.debug("update")
        return self.read()

    def delete(self, **kwargs):
        """ Delete
        """
        logger.debug("delete")
        return jsonify(None, self.request.response, 204)

    def publishTraverse(self, REQUEST, name):
        """ Override traverser
        """
        if name == 'PUT' and self.request.method == 'PUT':
            return self.update
        return self.read

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
