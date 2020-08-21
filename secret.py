from flask import Flask

app = Flask(__name__)

@app.route('/')
  return "Hello ! Hosted with Netlfix "

app.run(debug=true)
