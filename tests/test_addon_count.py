#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home_page import HomePage
from unittestzero import Assert
import pytest


class TestAddonCount:

    @pytest.mark.nondestructive
    def test_addon_count(self, mozwebqa):
        #This test is to assert that the count of the addons on dashboard is equal to the number of addons present on the page.
        #Create page objects
        homepage_obj = HomePage(mozwebqa)

        homepage_obj.go_to_home_page()
        loginpage_obj = homepage_obj.header.click_signin()
        dashboard_obj = loginpage_obj.login()
        Assert.true(dashboard_obj.is_the_current_page)

        dashboard_obj.click_public_addons_link()

        #Get the total count of the number of add-ons that are displayed on the dashboard.
        addon_count = dashboard_obj.addons_element_count()

        #Get the number of addons that are displayed on the left hand side of the page.(Something like your add-ons(20))
        counter = dashboard_obj.addons_count_label

        #Assert that the total addons on the page matches the counter on the left hand side.
        Assert.equal(str(addon_count), str(counter))
