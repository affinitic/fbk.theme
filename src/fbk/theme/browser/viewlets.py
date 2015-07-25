# -*- coding: utf-8 -*-
"""
fbk.theme
---------

Created by mpeeters
:copyright: (c) 2015 by Affinitic SPRL
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.layout.viewlets import common
from plone.app.layout.navigation.interfaces import INavigationRoot


class FooterViewlet(common.FooterViewlet):

    def on_homepage(self):
        """Verifiy if we are on the homepage"""
        if INavigationRoot.providedBy(self.context):
            return True
        return False


class HomepageButtonsViewlet(common.ViewletBase):

    def on_homepage(self):
        """Verifiy if we are on the homepage"""
        if INavigationRoot.providedBy(self.context):
            return True
        return False
