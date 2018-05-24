from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'm2m'
app.config['MYSQL_DATABASE_PASSWORD'] = 'm2m'
app.config['MYSQL_DATABASE_DB'] = '5GRobotDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn=mysql.connect()
cursor= conn.cursor()


@app.route("/")
def index():
	conn=mysql.connect()
	cursor= conn.cursor()
	cursor.execute ("SELECT* FROM 5GRobotDB WHERE robotId='robot1'")
	robot1=cursor.fetchall()
	cursor.execute ("SELECT* FROM 5GRobotDB WHERE robotId='robot2'")
	robot2=cursor.fetchall()
	cursor.execute ("SELECT* FROM 5GRobotDB WHERE robotId='robot3'")
	robot3=cursor.fetchall()
	cursor.close() 
	conn.close()
	return render_template('index.html',robot1=robot1,robot2= robot2,robot3= robot3)
	
	 

@app.route("/<robot_Id>")	
def detail(robot_Id):
	conn=mysql.connect()
	cursor= conn.cursor()
	cursor.execute ('SELECT * FROM 5GRobotDB WHERE robotId="{}"'. format(robot_Id))
	robot=cursor.fetchall()
	cursor.close() 
	conn.close()

    return render_template('detail.html',messages=robot)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()   # data is a dictionary
        conn=mysql.connect()
		cursor= conn.cursor()
		cursor.execute ('UPDATE 5GRobotDB SET WHERE robotId="{}"'. format())
		UPDATE cowstatus SET GpsAcqPeriod={}, AccelPattern={}	WHERE Device_ID = "{}" '.format(gps_acq_period,accel_pattern,device)
		cursor.close() 
		conn.close()
        return 'ADD'
    else:
		return 'NO JSON'	

	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)