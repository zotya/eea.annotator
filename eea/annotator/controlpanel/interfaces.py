""" Control Panel Interfaces

   >>> portal = layer['portal']
   >>> sandbox = portal['sandbox']

"""
from zope.interface import Interface
from zope import schema
from eea.annotator.config import EEAMessageFactory as _

class ISettings(Interface):
    """ Settings

        >>> from eea.annotator.interfaces import ISettings
        >>> ISettings(portal).portalTypes = [u'Document', u'News Item']
        >>> ISettings(portal).portalTypes
        [u'Document', u'News Item']

    """
    portalTypes = schema.List(
        title=_(u"Enable inline comments"),
        description=_(u"Annotator inline comments are enabled for the "
                      "following content-types"),
        required=False,
        default=[u"Document"],
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.ReallyUserFriendlyTypes")
    )
