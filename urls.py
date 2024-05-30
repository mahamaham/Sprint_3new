class BaseURLs:
    SERVER_URL = 'https://stellarburgers.nomoreparties.site/'

class URLS(BaseURLs):
    MAIN_PAGE_URL = f'{BaseURLs.SERVER_URL}'
    AUTH_PAGE_URL = f'{BaseURLs.SERVER_URL}login'
    REG_PAGE_URL = f'{BaseURLs.SERVER_URL}register'
    RECOVER_PAGE_URL = f'{BaseURLs.SERVER_URL}forgot-password'
    PROFILE_PAGE_URL = f'{BaseURLs.SERVER_URL}account/profile'
