from flask import Flask, session, request, render_template
from flask.ext.bootstrap import Bootstrap
import zz

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def signin_form():
	#session['hello']='ehll'
	print 'hello'
	result=zz.test('{"type":"score","id":"1208010110","pw":"892515"}')
	#print result
	return render_template('grade.html',result=result)

if __name__ == '__main__':
    app.run()