class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevlopmentConnfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'chatbot'
    MYSQL_DB = 'chatbot'

config = {
    'development': DevlopmentConnfig
}