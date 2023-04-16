from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bangkok, Thailand',
  'salary': 'THB. 80,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Samui, Thailand',
  'salary': 'THB. 50,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$3,200'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Suvijak')


@app.route("/api/jobs")
def list_fobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
