
class Locators(object):
    """

    Class representing locators for the Trello web application.

    Attributes:
        URL_LOGIN (str): The URL for the Trello login page.
        HOME_URL (str): The URL for the Trello home page.
        HREF (str): XPath locator for the "boards" href element.

    Classes:
        - LoginPage: Locators for the Trello login page elements.
        - HomePage: Locators for elements on the Trello home page.
        - Board: Locators for elements on a Trello board page.
        - List: Locators for elements on a Trello list within a board.
        - Search: Locators for elements related to search functionality.
        - Account: Locators for account-related elements.

    This class organizes the locators used within the Trello web application for easy management and access during test automation.
    """
    URL_LOGIN = 'https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D'
    HOME_URL = 'https://trello.com/u/vkqapro/boards'
    HREF = "//*[@href='/u/vkqapro/boards']"

    class LoginPage:
        USER_NAME_FIELD = "//input[@id='username']"
        ERROR_MESSAGE = "//div[@id='otpCode-uid2-error']"
        CONTINUE_BUTTON = "//span[contains(text(), 'Continue')]"
        PASSWORD_FIELD = "//input[@id='password']"
        LOGIN = "//div[2]/a[1][contains(text(), 'Log in')]"
        LOGIN_BUTTON = "//button[@id='login-submit']"
        CONTINUE_WITHOUT_2STEP_BUTTON = "//span[contains(text(), 'Continue without two-step verification')]"
        CANT_USE_LINK = "//span[contains(text(),'use your security key?')]"
        RECOVERY_CODE = "//input[@id='recoveryCode-uid2']"
        SIX_OTP_CODE_FIELD = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"

    class HomePage:
        CREATE_BUTTON = "//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[3]/button[1]"
        CREATE_BOARD_BUTTON = "//span[contains(text(), 'Create board')]"
        BLUE_BKG_BUTTON = "//li[@class='weB1QxFqJjPDxm'][1]"
        NEW_BOARD_NAME_FIELD = "//input[@data-testid='create-board-title-input']"
        CREATE_SUBMIT_BUTTON = "//*[@data-testid='create-board-submit-button']"
        CHECK_ACTIVE_BOARDS = "//div[3]/div/ul[@class='boards-page-board-section-list']/li"
        YOUR_BOARDS_TILE = "//h3[contains(text(), 'Your boards')]"
        BOARDS_BUTTON = "//nav/div[3]/div/ul/li/ul/li[1]"

    class Board:
        BOARD_TITLE_DELETED = "//*/div[@title='new_board_playwright']"
        BOARD_TITLE = "//*/div[@title='new_board_playwright']"
        NEW_BOARD_CREATED = "//h1[contains(text(),'new_board_playwright')]"
        # BOARD_TITLE = "//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/ul[1]/li[1]/a[1]"
        ADD_A_LIST_BUTTON = "//button[contains(text(), 'Add a list')]"
        ENTER_LIST_NAME_FIELD = "//textarea[@name='Enter list name…']"
        ADD_LIST_SUBMIT_BUTTON = "//button[@data-testid='list-composer-add-list-button']"
        LIST_TITLE = "//*[contains(text(), 'new_list_playwright')][1]"
        ADD_ANOTHER_LIST_BUTTON = "//button[@data-testid='list-composer-button']"

    class List:
        # ADD_A_CARD_BUTTON = "//button[contains(text(), 'Add a card')]"
        ADD_A_CARD_BUTTON = "//*[@data-testid='list']/div[3]/button[1]"
        CARD_NAME_FIELD = "//*[@placeholder='Enter a title or paste a link']"
        ADD_CARD_SUBMIT_BUTTOMN = "//button[contains(text(), 'Add card')]"
        NEW_CARD_TITLE = "//*[contains(text(), 'new_card_playwright')]"
        DROP_LOCATION_LIST = "//ol/li[2][@data-testid='list-wrapper']"
        CARD_LOCATION_ON_ANOTHER_LIST = "//div/ol/li[2]/div/ol/li[1]"
        CARD_TO_ARCHIVE = "//*[contains(text(), 'new_card_playwright')]"
        ARCHIVE_BUTTON = "//button[@data-testid='card-back-archive-button']"
        DELETE_BUTTON = "//button[contains(text(), 'Delete')]"
        DELETE_CONFIRM_BUTTON = "//button[@data-testid='popover-confirm-button' and contains(text(), 'Delete')]"
        ALL_CARDS_ON_FIRST_LIST = "//div[@class='board-canvas']/ol/li[1]/div/ol/li[@data-testid='list-card']"
        LABELS_BUTTON = "//button[contains(text(), 'Labels')]"
        LABEL_GREEN = "//*[@data-color='green']"
        LABEL_GREEN_APPLIED = "//div/div/div/span[@data-color='green']"
        X_BUTTON = "//button[@aria-label='Close popover']"
        X_DIALOG_BUTTON = "//button[@aria-label='Close dialog']"
        SHOW_MENU = "//button[@aria-label='Show menu']"
        IN_MENU_CLOSE_BOARD = "//*[contains(text(), 'Close board')]"
        IN_MENU_PROVE_CLOSE_BOARD = "//button[@data-testid='popover-close-board-confirm']"
        IN_MENU_PERMANENT_DELETE = "//button[@data-testid='close-board-delete-board-button']"
        IN_MENU_CONFIRM_PERMANENT_DELETE ="//button[@data-testid='close-board-delete-board-confirm-button']"

    class Search:
        SEARCH_FIELD = "//*[@placeholder='Search']"
        ADVANCE_SEARCH_BUTTON = "//*[contains(text(), 'Advanced search')]"
        ADVANCE_SEARCH_FIELD = "//div/input[@data-testid='advanced-search-input']"
        # BOARD_FOUND_IN_SEARCH = "//div/div/div/a[1]/span/span[2]/span[1]/span[1]/span[1]/div/span[contains(text(), 'new_board_playwright')]"
        BOARD_FOUND_IN_SEARCH = "//body/div[@id='trello-root']/div[@id='chrome-container']/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]"

    class Account:
        ACCOUNT_MENU = "//div/button[@aria-label='Open member menu']"
        LOG_OUT_BUTTON = "//span[contains(text(), 'Log out')]"
        URL_HOME = 'https://trello.com/home'



