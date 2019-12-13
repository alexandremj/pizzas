from flask import Flask, redirect, request, render_template, Response
import psycopg2
import requests

app = Flask(__name__, template_folder=("./"))

@app.route('/pizza', methods=['GET'])
def get_all_pizza_places():
    connection = psycopg2.connect("dbname=pizza user=alexandremj")
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM Pizza;""")
    connection.commit()

    return cursor.fetchall()


@app.route('/', methods=['POST'])
def receive_pizza_form():
    place = request.form['place']
    grade = request.form['grade']
    details = request.form['details']

    connection = psycopg2.connect("dbname=pizza user=alexandremj")
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO Pizza(name, grade, details)
                    VALUES (%s, %s, %s);""", (place, grade, details))
    connection.commit()

    return Response(status=201)


@app.route('/', methods=['GET'])
def render_homepage():
    return render_template('pizzaForm.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
