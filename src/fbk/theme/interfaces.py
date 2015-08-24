# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.app.multilingual.interfaces import IPloneAppMultilingualInstalled
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IFbkThemeLayer(IPloneAppMultilingualInstalled, IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFBKSettings(Interface):

    link_about_fr = schema.TextLine(
        title=u'About Kinesiology link (FR)',
        required=True,
    )

    link_about_en = schema.TextLine(
        title=u'About Kinesiology link (EN)',
        required=True,
    )

    link_about_nl = schema.TextLine(
        title=u'About Kinesiology link (NL)',
        required=True,
    )

    link_find_fr = schema.TextLine(
        title=u'Find Kinesiologist link (FR)',
        required=True,
    )

    link_find_en = schema.TextLine(
        title=u'Find Kinesiologist link (EN)',
        required=True,
    )

    link_find_nl = schema.TextLine(
        title=u'Find Kinesiologist link (NL)',
        required=True,
    )

    link_become_fr = schema.TextLine(
        title=u'Become Kinesiologist link (FR)',
        required=True,
    )

    link_become_en = schema.TextLine(
        title=u'Become Kinesiologist link (EN)',
        required=True,
    )

    link_become_nl = schema.TextLine(
        title=u'Become Kinesiologist link (NL)',
        required=True,
    )
