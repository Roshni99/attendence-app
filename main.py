from flask import Flask, request, render_template
import pyrebase 
import datetime

config = {
"apiKey": "AIzaSyB7znAsPJawT7jjQW9aIGlJJsIbLdwSDRY",
"authDomain": "attendence-system-8e730.firebaseapp.com",
"databaseURL": "https://attendence-system-8e730.firebaseio.com",
"storageBucket": "attendence-system-8e730.appspot.com",
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

app = Flask(__name__,)





@app.route('/',methods=['POST','GET'])   
def index():

    submit = False
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            x = datetime.datetime.now()
            x = x.strftime("%Y-%m-%d %H:%M:%S")

            name = request.form.get('name')
            email = request.form.get('email')
            number = request.form.get('number')
            regno = request.form.get('regno')

            print(name,email,number,regno)


            payload = {'time': x, 'name' : name,'email': email,'number':number, "rno" : regno}

            db.child('teachbotattendence').push(payload)


            return render_template('index.html', submit=True, name = payload['name'])





    return render_template('index.html', submit = False)



if __name__ =='__main__':  
    app.run(host='0.0.0.0',debug=True, port=8080) 