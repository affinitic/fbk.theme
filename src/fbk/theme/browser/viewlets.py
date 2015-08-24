# -*- coding: utf-8 -*-
"""
fbk.theme
---------

Created by mpeeters
:copyright: (c) 2015 by Affinitic SPRL
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility

from fbk.theme.interfaces import IFBKSettings


class BaseViewlet(object):

    @property
    def root_url(self):
        return api.portal.get_navigation_root(self.context).absolute_url()

    @property
    def links(self):
        values = getUtility(IRegistry).forInterface(IFBKSettings)
        portal_state = getMultiAdapter((self.context.aq_inner, self.request),
                                       name=u'plone_portal_state')
        lang = portal_state.language()
        keys = (
            'link_about',
            'link_find',
            'link_become',
        )
        return {k: getattr(values, '{0}_{1}'.format(k, lang)) for k in keys}


class FooterViewlet(BaseViewlet, common.FooterViewlet):

    def on_homepage(self):
        """Verifiy if we are on the homepage"""
        context_helper = getMultiAdapter((self.context, self.request),
                                         name="plone_context_state")
        if INavigationRoot.providedBy(context_helper.canonical_object()):
            return True
        return False


class HomepageButtonsViewlet(BaseViewlet, common.ViewletBase):

    def on_homepage(self):
        """Verifiy if we are on the homepage"""
        context_helper = getMultiAdapter((self.context, self.request),
                                         name="plone_context_state")
        if INavigationRoot.providedBy(context_helper.canonical_object()):
            return True
        return False
