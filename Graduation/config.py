#程序的配置
import os

basedir = os.path.abspath(os.path.dirname(__file__))


#基类Config
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'zhang21'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_ADMIN = 'zhangxx5678@gmail.com'
    FLASKY_POSTS_PER_PAGE = 20
    #email功能暂时未写

    @staticmethod
    def init_app(app):
        pass

#子类Config
class DevelopmentConfig(Config):
    DEBUG =True
    #email服务器及登录等若干信息暂时未写
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING =True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development' : DevelopmentConfig,
    'testin' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}