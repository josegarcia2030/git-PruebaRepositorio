
from flask import Flask, flash, render_template, redirect, request
from flaskext.mysql import MySQL




app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Empresa'
mysql.init_app(app)



@app.route('/ingresarDato')
def ingresarDato():

    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'rasek', 'rasek2030.2010@gmail.com', 'foto2.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return "se ingresaron los datos"


@app.route("/")
def home():
    return render_template('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)