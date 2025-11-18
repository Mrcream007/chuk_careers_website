from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'London, England',
        'salary': '£33,000'
    },
    {
        'id': 2,
        'title': 'Software Developer',
        'location': 'Aberdeen, Scotland',
        'salary': '£37,600'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'New York, USA',
        'salary': '$55,000'
    }
]

@app.route("/")
def hello_world():
    #return "Hello Chuka!"
    return render_template('home.html', jobs=JOBS, company_name='mrcream007')

#this is to open/establish a local server with if statement 
if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)