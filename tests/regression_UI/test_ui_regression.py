import time

import allure

from tests.BaseTest import BaseTest

import pytest
import logging as log
import re
import pyotp
from playwright.sync_api import Page, expect, sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')

class TestUiRegression(BaseTest):

    def otp_auth(self):
        totp = pyotp.TOTP(SECRET_KEY)
        return totp.now()

    @pytest.mark.TC000
    @pytest.mark.TC001
    @allure.title('Log in to Trello account')
    def test_log_in_functionality(self, page: Page):
        with allure.step('Log in to Trello account'):
            while True:
                try:
                    page.goto(self.locator.URL_LOGIN)
                    page.locator(self.locator.LoginPage.USER_NAME_FIELD).fill(USER_EMAIL)
                    page.locator(self.locator.LoginPage.CONTINUE_BUTTON).click()
                    page.locator(self.locator.LoginPage.PASSWORD_FIELD).fill(USER_PASSWORD)
                    page.locator(self.locator.LoginPage.LOGIN_BUTTON).click()
                    log.info("+++++" * 20)
                    log.info(self.otp_auth())
                    time.sleep(10)
                    page.locator(self.locator.LoginPage.SIX_OTP_CODE_FIELD).clear()
                    page.locator(self.locator.LoginPage.SIX_OTP_CODE_FIELD).fill(self.otp_auth())
                    time.sleep(3)
                    if page.locator(self.locator.LoginPage.ERROR_MESSAGE).is_visible():
                        continue
                    else:
                        expect(page).to_have_url(self.locator.HOME_URL)
                        log.info(page.url)
                        break
                except AssertionError:
                    pass

    @pytest.mark.TC000
    @pytest.mark.TC002
    @allure.title('Board Creation')
    def test_board_creation(self, page:Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)
        with allure.step('Create a new board'):
            time.sleep(3)
            page.locator(self.locator.HomePage.CREATE_BUTTON).click()
            page.locator(self.locator.HomePage.CREATE_BOARD_BUTTON).click()
            page.locator(self.locator.HomePage.BLUE_BKG_BUTTON).click()
            page.locator(self.locator.HomePage.NEW_BOARD_NAME_FIELD).fill('new_board_playwright')
            page.locator(self.locator.HomePage.CREATE_SUBMIT_BUTTON).click()

        with allure.step('Verifying the board creation'):
            expect(page.locator(self.locator.Board.NEW_BOARD_CREATED)).to_have_text('new_board_playwright')
            new_board_title = page.locator(self.locator.Board.NEW_BOARD_CREATED).inner_text()
            log.info('===' * 50)
            log.info(new_board_title)

    @pytest.mark.TC000
    @pytest.mark.TC003
    @allure.title('List creation')
    def test_list_creation(self, page:Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Opening the board and creating a new list'):
            time.sleep(3)
            page.locator(self.locator.Board.BOARD_TITLE).click()
            page.get_by_role('button', name='Add a list').click()
            # page.locator(self.locator.Board.ADD_A_LIST_BUTTON).click()
            page.locator(self.locator.Board.ENTER_LIST_NAME_FIELD).fill('new_list_playwright')
            page.locator(self.locator.Board.ADD_LIST_SUBMIT_BUTTON).click()

        with allure.step('Verifying that the new list is created'):
            expect(page.locator(self.locator.Board.LIST_TITLE)).to_have_text('new_list_playwright')
            log.info(f'The list was created: {page.locator(self.locator.Board.LIST_TITLE).inner_text()}')


    @pytest.mark.TC000
    @allure.title('Card Creation')
    @pytest.mark.TC004
    def test_card_creation(self, page:Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Open the board and the list'):
            time.sleep(3)
            page.locator(self.locator.Board.BOARD_TITLE).click()

        with allure.step('Create a new card'):
            time.sleep(3)
            page.locator(self.locator.List.ADD_A_CARD_BUTTON).click()
            page.locator(self.locator.List.CARD_NAME_FIELD).fill("new_card_playwright")
            page.locator(self.locator.List.ADD_CARD_SUBMIT_BUTTOMN).click()

        with allure.step('Verifying the new card creation'):
            time.sleep(2)
            expect(page.locator(self.locator.List.NEW_CARD_TITLE)).to_have_text('new_card_playwright')

    @pytest.mark.TC000
    @pytest.mark.TC005
    @allure.title('Drag and drop card')
    def test_drag_n_drop_card(self, page: Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Open the board and the list'):
            time.sleep(3)
            page.locator(self.locator.Board.BOARD_TITLE).click()

        with allure.step('Drag and drop card'):
            page.locator(self.locator.Board.ADD_ANOTHER_LIST_BUTTON).click()
            page.locator(self.locator.Board.ENTER_LIST_NAME_FIELD).fill('new_list_playwright_2')
            page.locator(self.locator.Board.ADD_LIST_SUBMIT_BUTTON).click()
            time.sleep(3)
            page.locator(self.locator.List.NEW_CARD_TITLE).drag_to(page.locator(self.locator.List.DROP_LOCATION_LIST))

        with allure.step('Verifying that the card is dropped to another list'):
            expect(page.locator(self.locator.List.CARD_LOCATION_ON_ANOTHER_LIST)).to_have_text('new_card_playwright')

    @pytest.mark.TC000
    @pytest.mark.TC006
    @allure.title('Label a card')
    def test_label_card(self, page: Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)
        with allure.step('Label a card'):
            page.locator(self.locator.Board.BOARD_TITLE).click()
            page.locator(self.locator.List.CARD_TO_ARCHIVE).click()
            page.locator(self.locator.List.LABELS_BUTTON).click()
            page.locator(self.locator.List.LABEL_GREEN).click()
            page.locator(self.locator.List.X_BUTTON).click()
        with allure.step('Verifying that the card is labeled'):
            expect(page.locator(self.locator.List.LABEL_GREEN_APPLIED)).to_be_visible()

    @pytest.mark.TC000
    @pytest.mark.TC007
    @allure.title('Archive a card')
    def test_archive_card(self, page:Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Archive a card'):
            page.locator(self.locator.Board.BOARD_TITLE).click()
            time.sleep(2)
            page.locator(self.locator.List.CARD_TO_ARCHIVE).click()
            page.locator(self.locator.List.ARCHIVE_BUTTON).click()
            page.locator(self.locator.List.DELETE_BUTTON).click()
            page.locator(self.locator.List.DELETE_CONFIRM_BUTTON).click()

        with allure.step('Verifying that the card is deleted'):
            expect(page.locator(self.locator.List.CARD_TO_ARCHIVE)).not_to_be_visible()

    @pytest.mark.TC000
    @pytest.mark.TC008
    @allure.title('Search functionality')
    def test_search_functionality(self, page: Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Search a board'):
            page.locator(self.locator.Search.SEARCH_FIELD).click()
            page.locator(self.locator.Search.ADVANCE_SEARCH_BUTTON).click()
            page.locator(self.locator.Search.ADVANCE_SEARCH_FIELD).fill('new_board_playwright')

        with allure.step('Verifying the search result'):
            page.wait_for_selector(self.locator.Search.BOARD_FOUND_IN_SEARCH).is_visible()
            expect(page.locator(self.locator.Search.BOARD_FOUND_IN_SEARCH)).to_have_text('new_board_playwright')
            log.info(f"The found board's name is: {page.locator(self.locator.Search.BOARD_FOUND_IN_SEARCH).inner_text()}")

    @pytest.mark.TC000
    @pytest.mark.TC009
    @allure.title('Delete a board')
    def test_delete_board(self, page: Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Board deletion'):
            page.locator(self.locator.Board.BOARD_TITLE).click()
            page.locator(self.locator.List.SHOW_MENU).click()
            page.locator(self.locator.List.IN_MENU_CLOSE_BOARD).click()
            page.locator(self.locator.List.IN_MENU_PROVE_CLOSE_BOARD).click()
            page.locator(self.locator.List.IN_MENU_PERMANENT_DELETE).click()
            page.locator(self.locator.List.IN_MENU_CONFIRM_PERMANENT_DELETE).click()

        with allure.step('Verifying that the board is deleted'):
            expect(page.locator(self.locator.Board.BOARD_TITLE_DELETED)).not_to_be_visible()

    @pytest.mark.TC000
    @pytest.mark.TC010
    @allure.title('Log out functionality')
    def test_logged_out(self, page: Page):
        with allure.step('Log in to Trello account'):
            self.test_log_in_functionality(page)

        with allure.step('Board deletion'):
            page.locator(self.locator.Account.ACCOUNT_MENU).click()
            page.locator(self.locator.Account.LOG_OUT_BUTTON).click()
            time.sleep(2)
            page.locator(self.locator.Account.LOG_OUT_BUTTON).click()

        with allure.step('Verifying that the user is logged out and is landed on Trello starting page'):
            page.wait_for_selector(self.locator.LoginPage.LOGIN)
            expect(page.locator(self.locator.LoginPage.LOGIN)).to_be_visible()