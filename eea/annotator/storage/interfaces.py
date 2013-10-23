""" Storage interfaces

    >>> portal = layer['portal']
    >>> sandbox = portal['sandbox']

"""
from zope.interface import Interface
from eea.annotator.config import EEAMessageFactory as _
from zope import schema

class IAnnotatorStorage(Interface):
    """ Access/Update annotator configuration

        >>> from eea.annotator.interfaces import IAnnotatorStorage
        >>> storage = IAnnotatorStorage(sandbox)
        >>> storage
        <eea.annotator.storage.handler.Storage object...>

    """
    enabled = schema.Bool(title=_(u"Annotator enabled?"))
    disabled = schema.Bool(title=_(u"Annotator disabled?"))

    def enable():
        """ Enable annotator

            >>> storage.enable()
            >>> storage.enabled
            True

        """

    def disable():
        """ Disable annotator

            >>> storage.disable()
            >>> storage.disabled
            True

        """
