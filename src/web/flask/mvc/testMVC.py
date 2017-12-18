# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

from flask import Flask, render_template

# 默认模板，在根目录下的templates文件夹下。也可以通过参数指定到别的文件夹
app = Flask(__name__, template_folder = 'templates')

@app.route("/", methods = ['GET', 'POST'])
def home():
    
    return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_form():
    
    return render_template('form.html')
    
@app.route('/signin', methods = ['POST'])
def signin():
    
    pass

if __name__ == '__main__':
    
    app.run()