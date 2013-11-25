""" Portlets
"""
from zope import schema
from zope.formlib import form
from zope.interface import implements
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from eea.annotator.config import EEAMessageFactory as _

class IAnnotatorPortlet(IPortletDataProvider):
    """ Annotator portlet
    """
    label = schema.TextLine(
        title=_(u"Porlet title"),
        description=_(u"Title of the portlet. Leave empty if you don't want "
                      u"to display a title for this portlet"),
        default=u"Inline comments",
        required=False
    )

class Assignment(base.Assignment):
    """ Assignment
    """
    implements(IAnnotatorPortlet)

    def __init__(self, label=u"Inline comments"):
        self.label = label

    @property
    def title(self):
        """ Get portlet title
        """
        return self.label or u'Inline comments'

class AddForm(base.AddForm):
    """ Add portlet
    """
    form_fields = form.Fields(IAnnotatorPortlet)
    label = _(u"Add Inline comments (Annotator) portlet")
    description = _(
        u"This portlet traces all inline comments for this document")

    def create(self, data):
        """ Create
        """
        return Assignment(label=data.get('label', u'Inline comments'))

class EditForm(base.EditForm):
    """ Portlet edit
    """
    form_fields = form.Fields(IAnnotatorPortlet)
    label = _(u"Edit Inline comments (Annotator) portlet")
    description = _(
        u"This portlet traces all inline comments for this document")

class Renderer(base.Renderer):
    """ portlet renderer
    """
    render = ViewPageTemplateFile('annotator.pt')

    @property
    def available(self):
        """By default, portlets are available
        """
        return getToolByName(
            self.context, 'portal_membership').checkPermission(
                'Review portal content', self.context)
