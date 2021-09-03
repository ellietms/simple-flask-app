from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure the database
stream = open('db.yaml', 'r')
database = yaml.load(stream,  Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = database['mysql_host']
app.config['MYSQL_USER'] = database['mysql_user']
app.config['MYSQL_PASSWORD'] = database['mysql_password']
app.config['MYSQL_DB'] = database['mysql_db']

mysql = MySQL(app)

print("MYSQL",mysql)


@app.route('/', methods = ['GET','POST'])
def index():
    print("METHOD",request.method)
    if request.method == 'POST':
        # fetch the form data
        user_info = request.form
        print("USER INFO", user_info)
        name = user_info['name']
        email = user_info['email']
        cur = mysql.connection.cursor()
        print("CUR",cur)
        result = cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        print("RESULT",result)
        mysql.connection.commit()
        cur.close()
        return "WELL DONE ELLIEEEEEEEE"
    return render_template('index.html')


if __name__ == '__main__':
     app.run(debug = True)   