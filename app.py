from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Laundry Analyst',
  'location': 'Manila, Philippines',
  'salary': 'Php 80,000'
}, {
  'id': 2,
  'title': 'Meal R&D',
  'location': 'Remote',
  'salary': 'Php 40,000'
}, {
  'id': 3,
  'title': 'House Cleaning Expert',
  'location': 'Manila, Philippines',
  'salary': 'Php 100,000'
}, {
  'id': 4,
  'title': 'Massage Specialist',
  'location': 'Manila, Philippines',
  'salary': 'Php 160,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='PhenLC Enterprise')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
