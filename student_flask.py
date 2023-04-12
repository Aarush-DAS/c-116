from flask import Flask, render_template

app = Flask(__name__)

@app.route("/student_Index")

def student_webpage():

    name = 'Aarush'

    return render_template('student_Index.html', student_name = name)

app.run(debug=True)