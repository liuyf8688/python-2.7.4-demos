# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    
    return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])
def signin_form():
    
    return '''
            <p>姓名：<input /></p>
            <p>密码：<input /></p>
            '''
    
@app.route('/signin', methods = ['POST'])
def signin():
    
    pass

if __name__ == '__main__':
    
    app.run()