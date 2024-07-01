class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = '159.89.107.90'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'chatbot'

config = {
    'development': DevelopmentConfig
}
