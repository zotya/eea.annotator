""" Schema extender for Disable Autolinks for context/page
"""
from zope.interface import implements
from zope.component import queryAdapter
from zope.component.hooks import getSite
from Products.Archetypes.public import BooleanField, BooleanWidget
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField
from eea.annotator.config import EEAMessageFactory as _
from eea.annotator.interfaces import ILayer
from eea.annotator.controlpanel.interfaces import ISettings

class EEABooleanField(ExtensionField, BooleanField):
    """ BooleanField for schema extender
    """

class EEASchemaExtender(object):
    """ Schema extender for content types with data provenance
    """
    implements(ISchemaExtender, IBrowserLayerAwareExtender)
    layer = ILayer

    fields = (
        EEABooleanField(
            name='disableAnnotator',
            schemata='settings',
            default=False,
            searchable=False,
            widget=BooleanWidget(
                label=_('Disable inline comments'),
                description=_("Do not allow editors to add inline comments on"
                              'this context/page'),
            )
        ),
    )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        """ Returns provenance list field
        """
        settings = queryAdapter(getSite(), ISettings)
        ctype = getattr(self.context, 'portal_type', '')
        allowed = settings.portalTypes or []
        if ctype in allowed:
            return self.fields
        return ()
