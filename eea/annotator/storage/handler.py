""" Storage
"""
from zope.interface import implements
from zope.annotation.interfaces import IAnnotations
from eea.annotator.interfaces import IAnnotatorStorage
from eea.annotator.config import PROJECTNAME
from persistent.dict import PersistentDict

class Storage(object):
    """ Annotator storage adapter
    """
    implements(IAnnotatorStorage)

    def __init__(self, context):
        self.context = context

    @property
    def _storage(self):
        """ Editable storage
        """
        anno = IAnnotations(self.context)
        storage = anno.get(PROJECTNAME, None)
        if not storage:
            storage = anno[PROJECTNAME] = PersistentDict()
        return storage

    @property
    def storage(self):
        """ Read-only storage
        """
        anno = IAnnotations(self.context)
        return anno.get(PROJECTNAME, {})
    #
    # Public interface
    #
    @property
    def disabled(self):
        """ Annotator disabled?
        """
        return getattr(self.context, 'disableAnnotator', False)

    @disabled.setter
    def disabled(self, value):
        """ Disable inline comments
        """
        setattr(self.context, 'disableAnnotator', value)

    @property
    def readOnly(self):
        """ Read-only inline comments
        """
        return getattr(self.context, 'readOnlyAnnotator', False)

    @readOnly.setter
    def readOnly(self, value):
        """ Make inline comments read-only
        """
        setattr(self.context, 'readOnlyAnnotator', value)
