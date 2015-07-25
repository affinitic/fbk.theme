# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.multilingual.interfaces import IPloneAppMultilingualInstalled


class IFbkThemeLayer(IPloneAppMultilingualInstalled, IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
