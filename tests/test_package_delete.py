#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from unittestzero import Assert


class TestPackageDelete:

    def test_addon_delete(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        homepage_obj = dashboard_obj.go_to_home_page()
        addonpage_obj = homepage_obj.click_create_addon_btn()

        #Get the name of the addon on the editor page.
        addon_name = addonpage_obj.addon_name

        #Go the the dashboard and delete the addon that you just created. Then check that the addon at the top of the list is not the same as the one you just deleted.
        dashboard_obj = homepage_obj.header.click_dashboard()
        dashboard_obj.addon(addon_name).click_delete()
        dashboard_obj.addon(addon_name).confirm_delete()
        Assert.false(dashboard_obj.addon(addon_name).is_displayed, "Addon %s found" % addon_name)

    def test_library_delete(self, mozwebqa):
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()

        homepage_obj = dashboard_obj.go_to_home_page()
        libpage_obj = homepage_obj.click_create_lib_btn()
        library_name = libpage_obj.library_name

        dashboard_obj = homepage_obj.header.click_dashboard()
        dashboard_obj.library(library_name).click_delete()
        dashboard_obj.library(library_name).confirm_delete()
        Assert.false(dashboard_obj.library(library_name).is_displayed, "Library %s found" % library_name)
