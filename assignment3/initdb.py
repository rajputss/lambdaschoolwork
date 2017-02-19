#!/usr/bin/python

from flask import Flask, render_template, request, jsonify
import sqlite3


#connection = sqlite3.connect('database.db')
#print('Opened database successfully.')

#connection.execute('CREATE TABLE foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
#print('Table create successfully')

#connection.close()

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def enternew():
    return render_template('food.html')


@app.route('/addfood', methods=['POST'])
def addfood():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        name=request.form['name']
        calories=request.form['calories']
        cuisine=request.form['cuisine']
        is_vegetarian=request.form['is_vegetarian']
        is_gluten_free=request.form['is_gluten_free']

        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES(?,?,?,?,?)',
                       (name, calories, cuisine, is_vegetarian, is_gluten_free))
        connection.commit()
        message='Record added successfully!'
    except:
        connection.rollback()
        message='Error in insert operation'
    finally:
        return render_template('result.html', message=message)
        connection.close()


@app.route('/favorite')
def favorite():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        cursor.execute('SELECT * FROM foods where name IS "pita bread"')
        results = jsonify(cursor.fetchone())
    except:
        connection.rollback()
        results = 'FAVORITE TRANSACTION FAILED!'
    finally:
        return results
        connection.close()


@app.route('/search', methods=['GET'])
def search():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        name=request.args['name']
        cursor.execute('SELECT * FROM foods where name IS ?', (name,))
        results=jsonify(cursor.fetchone())
    except:
        connection.rollback()
        results = 'Failed to get search results'
    finally:
        return results
        connection.close()


@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute('DROP TABLE foods')
        message = 'dropped'
    except:
        connection.rollback()
        message = 'Drop failed'
    finally:
        return render_template('result.html', message=message)