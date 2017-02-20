#!/usr/bin/python


from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/movie', methods=['POST'])
def movie():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        title=request.form['title']
        year=request.form['year']
        # genre=request.form['genre']
        # director=request.form['director']
        cursor.execute('INSERT INTO movies (title, year) VALUES(?,?)',
                   (title, year))
        connection.commit()
        message = 'Movie added successfully!'
    except:
        connection.rollback()
        message = 'Error in insert operation'

    finally:
        return render_template('result.html', message=message)
        connection.close()


@app.route('/movies')
def movies():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    try:
        cursor.execute('SELECT * FROM movies')
        result=cursor.fetchall()
    except:
        connection.rollback()
        result="Error in getting data."
    finally:
        connection.close()
        return jsonify(result)


@app.route('/search', methods=['GET'])
def search():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	term = request.args.get('name').upper()

	try:
		cursor.execute('SELECT * FROM movies where name = ?', (term,))
		result = cursor.fetchone()
	except:
		connection.rollback()
		result = ["Oh no...something has happened, could not search at all"]
	finally:
		connection.close()
		if result is None:
			result = ["Sorry...that movie is not in the database"]
		return jsonify(result)


app.run(debug=True)