""" Inline comments
"""

from zope.component import queryAdapter
from Products.Five.browser import BrowserView
from eea.annotator.interfaces import IAnnotatorStorage


class InlineComments(BrowserView):
    """ Display all inline comments
    """
    @property
    def comments(self):
        """ All comments sorted by date
        """
        def compare(a, b):
            """ Custom sorting cmp
            """
            return cmp(a, b)

        storage = queryAdapter(self.context, IAnnotatorStorage)
        for comment in sorted(storage.comments.values(), cmp=compare):
            yield comment
