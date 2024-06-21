class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'chatbot'
    MYSQL_DB = 'chatbot'

config = {
    'development': DevelopmentConfig
}
