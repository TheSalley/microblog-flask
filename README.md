# The Flask Mega-Tutorial Note

## 1、简介

此项目学习 https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh

## 2、准备条件

虚拟环境

```shell
python -m venv cenv
venv\Scripts\activate
```

安装

```shell
pip install flask
```

flask 环境变量

```shell
set FLASK_APP=microblog
set FLASK_DEBUG=1
```

flask 运行

```shell
flask run
```

## 3、视图

+ 视图函数的书写

  + `@app.route()`

+ 模板

  + `render_template()`
  + 条件语句
  + 循环语句
  + 宏(macro)
  + 模板的继承

## 4、Web表单

Flask-WTF 插件来处理表单

```shell
pip install flask-wtf
```

+ `flash` 闪现消息