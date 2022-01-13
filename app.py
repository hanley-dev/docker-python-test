import os
import logging

from flask import Flask

# Change the format of logged messages
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
	html = """
<html>
 <head>
  <title>
   GitHub - Sample Python Flask Example
  </title>
 </head>
 <body>
  <p>Hello GitHub World!</p>
  <a href="https://github.com/" target="_blank">GitHub Website</a>
 </body>
</html>
"""
	return html

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
