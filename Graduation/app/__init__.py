#程序包的构造文件
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config#配置文件中的config配置环境
from flask_login import LoginManager
from flask_moment import Moment
from flask_pagedown import PageDown
#PageDown使用JS实现客户端的 MarkDown 到 HTML 的转换程序
#MarkDown使用Python实现服务器端的 MarkDown 到 HTLML 的程序转换


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'#提供不同的安全等级防止用户会话遭篡改
login_manager.login_view = 'auth.login'#设置登录页面的端点

#工厂函数
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])#从配置对象中导入程序
    config[config_name].init_app(app)#程序创建并配置

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)#初始化
    login_manager.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)#将蓝本注册到程序上

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')#注册后蓝本中定义的所有路由都会加上指定的前缀'/auth'

    return app#工厂函数返回创建的程序实例