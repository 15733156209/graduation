#创建蓝本
"""
    在单脚本程序中，程序实例存在于全局作用域中，路由可以直接使用app.route修饰器定义。但现在程序在运行时创建，只有调用create_app()之后
    才能使用app.route修饰器，这时定义路由就太晚了。Flask蓝本提供了更好的解决方法。
    在蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分。
"""
from flask import Blueprint


#实例蓝本对象创建蓝本，这个构造函数的第一个参数为蓝本名'main'
main =Blueprint('main', __name__)


#把路由和错误处理程序与蓝本联系起来
#末尾导入避免循环导入依赖
from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)