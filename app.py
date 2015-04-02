from flask import Flask, make_response, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
  return make_response(open('templates/index.html').read())

@app.route('/getTweets')
def getTweets():
  data = {
      'username' : 'jeffreythewang',
      'name' : 'Jeff'
  }

  return jsonify(**data)

if __name__ == '__main__':
  app.run()
