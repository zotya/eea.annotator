""" Storage
"""
import json
import hashlib
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

    @property
    def _comments(self):
        """ Editable comments
        """
        comments = self._storage.get('comments')
        if not comments:
            comments = self._storage['comments'] = PersistentDict()
        return comments

    @property
    def comments(self):
        """ Read-only comments
        """
        return self.storage.get('comments', {})

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
    #
    # Inline comments
    #
    def get(self, name, default=None):
        """ Get item by name
        """
        return self.comments.get(name, default)

    def add(self, comment):
        """ Add inline comment
        """
        oid = hashlib.md5(u"%s" % comment).hexdigest()
        if isinstance(comment, (str, unicode)):
            comment = json.loads(comment)
        comment['id'] = oid
        self._comments[oid] = PersistentDict(comment)
        return comment

    def edit(self, comment):
        """ Update existing comment
        """
        if isinstance(comment, (str, unicode)):
            comment = json.loads(comment)
        oid = comment.get('id')
        self._comments[oid] = PersistentDict(comment)
        return comment

    def delete(self, comment):
        """ Delete comment
        """
        if isinstance(comment, (str, unicode)):
            comment = json.loads(comment)
        oid = comment.get('id')
        return self._comments.pop(oid)
