graduation :blush: project :blush: ing... :blush:
========
<br>

### 基于《Flask web Development：Development Web Application with Python》一书
### Python3.x
<br>

### FlaskApp框架结构
![](https://github.com/Zhang21/graduation/blob/master/Graduation/flaskapp.png)
<br>

### 利用Linux+uWSGI+Nginx+Flask部署应用
[uWSGI文档](http://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/WSGIquickstart.html#uwsgipython)<br>
[Nginx官方文档](http://www.nginx.cn/doc/)<br>
[Flask官方文档](http://docs.jinkan.org/docs/flask/)<br>

`/home/zhang/Graduation/uwsgi.ini文件`
```
[uwsgi]
socket = 127.0.0.1:5678
chdir = /home/zhang/Graduation
wsgi-file = manage.py
callable = app
process = 2
threads = 2
status = 127.0.0.1:8765
```
<br>

`/etc/nginx/conf.d/flaskapp.conf文件`
```
server {
    listen 80;
    server_name www.zhang21.com;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:5678;
    }
}
```
<br>

`启动Nginx、uwsgi`
```
service nginx start
uwsgi uwsgi.ini
```
<br>

### 关于数据库
可以选择把数据库更换为 `MongoDB` 或者 `MySQL`<br>
```
Python 连接 MongoDB 的库 `pymongo`<br>
Python 连接 MySQL 的库 `pymysql`<br>
Python 连接 Redis 的库 `redis`<br>
```
