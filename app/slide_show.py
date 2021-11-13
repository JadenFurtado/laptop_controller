from app import app
from flask import render_template
from flask import request,session
from flask import jsonify
from flaskext.mysql import MySQL
#session['current_command_number']=1
#get current slide number
"""
@app.route("/current_command_no/")
def change_slide():
    #global session['current_command_number']    
    return session['current_command_number']

#change slide
@app.route("/command/right_arrow")
def change_slide_action():
    pass
# go ahead one slide
@app.route("/command/left_arrow")
def change_slide_increment():
    #global session['current_command_number']    
    if session.get("current_command_number")==True:
        session['current_command_number'] = session['current_command_number'] + 1
    else:
        session['current_command_number'] = 1
    return '{"command_number":"'+str(session['current_command_number'])+'"}'
# go back one slide
@app.route("/command/esc")
def decrement_slide_decrement():
    #global session['current_command_number']    
    session['current_command_number'] = session['current_command_number'] - 1
    return session['current_command_number']
"""
@app.route("/command/insert/<command_name>")
def insert_command(command_name):
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cur = conn.cursor()
    
    try:
        sql = """INSERT INTO command(command_name) 
        VALUES(%s)"""
    
#        start_dates = request.form['start_date']
#        end_date = request.form['end_date']
#        users_id = request.form['users_id']
        house_data=(command_name)
        print(command_name)
        cur.execute(sql,house_data)
        print(cur)
        conn.commit()
        rv = cur.fetchall()
        print(rv)
    finally:
        cur.close()
    return jsonify(rv)

#to search for a house
@app.route("/command/last_command")
def last_command_display():
    mysql = MySQL()
    mysql.init_app(app)
    mycursor = mysql.connect().cursor()
    try:
        sql = """SELECT * FROM command WHERE command_id IN (SELECT MAX(command_id) FROM command)"""
        mycursor.execute(sql)
        rv = mycursor.fetchall()
        command_num = str(rv[0][0])
        command_nm = str(rv[0][1])
    finally:
        mycursor.close()
    return """{"command_id":"""+command_num+""","command_nm":"""+command_nm+"""}"""