from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'HOST-NAME'
app.config['MYSQL_USER'] = 'USERNAME'
app.config['MYSQL_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_DB'] = 'DATABASE_NAME'

mysql = MySQL(app)

@app.route('/', methods= ['GET'])
def home():
    return render_template("home.html")


@app.route('/api', methods=['GET'])
def get_word():
    try:
        # Connect to MySQL and fetch the word from the database
        conn = mysql.connection
        print("Connected to Mysql DB")
        cursor = conn.cursor()
        print("Cursor Created")
        cursor.execute('SELECT word FROM words')
        print('Query Executed!')
        result = cursor.fetchone()
        # cursor.close()
        # conn.close()

        if result:
            word = result[0]
            print(word)
        else:
            word = 'Test'

        return jsonify({'word': word})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/admin', methods=['GET', 'POST'])
def admin_portal():
    if request.method == 'POST':
        new_word = request.form.get('word')

        try:
            # Connect to MySQL and update the word in the database
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute('UPDATE words SET word=%s', (new_word,))
            conn.commit()
            # cursor.close()
            # conn.close()

            return render_template('admin.html', message='Word updated successfully.')

        except Exception as e:
            return render_template('admin.html', message='Error: ' + str(e))

    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
