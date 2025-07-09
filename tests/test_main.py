import time

import pytest

from pages.Navigation_cmd_page import Navigation_Actions
from pages.Table_page import TableActions
from pages.alert_options_page import Alert_options
from pages.broken_links_page import Broken_links
from pages.droup_down_options_page import DropDownList
from pages.mouse_over_actions_page import Mouse_action
from pages.open_browser_page import openinit
from config_test import *
from pages.send_text_page import Provide_input
from pages.window_operations_page import WindowOptions


class Test_Practice_demo:

    def test_start_testing(self, init_browser):
        openbrowser = openinit(init_browser)
        openbrowser.pass_URL_to_browser()
        nava = Navigation_Actions(init_browser)
        nava.navigation_BF()

        time.sleep(10)

    # def tables_static_dynamic(self):
    #     tables = TableActions(init_browser)
    #     tables.normaltable()
    #
    # def send_data_field(self):
    #     pass_text = Provide_input(init_browser)
    #     pass_text.send_data()
    #
    # def droupdown_list(self):
    #     ddl = DropDownList(init_browser)
    #     ddl.dropdownlist()
    #
    # def mousoveractions(self):
    #     moa = Mouse_action(init_browser)
    #     moa.mouse_actions()
    #
    # def aleractions(self):
    #     alert_message = Alert_options(init_browser)
    #     alert_message.alertoptions()
    #
    # def brokenlinks(self):
    #     link = Broken_links(init_browser)
    #     link.brokenlinks()
    #
    # def multi_win_handle(self):
    #     winoptions = WindowOptions(init_browser)
    #     winoptions.multiwin()

