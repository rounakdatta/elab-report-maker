from flask import Flask, render_template, request, send_file
import os
import elabreport

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	if request.method == 'POST' and 'name' in request.form and 'password' in request.form:
		username = request.form['name']
		password = request.form['password']
		elabx = request.form['elab']
		level = request.form['level']

		global dummy

		print('old record to remove: ' + dummy)

		for img in os.listdir('.'):
			if img.startswith(dummy):
				os.remove(img)

		dummy = username

		if level=="all":
			filename = elabreport.gen_report_all(username, password, elabx)
		else:
			filename = elabreport.gen_report(username, password, elabx, level)

		return send_file('./' + filename, as_attachment=True)

	return render_template('index.html')

if __name__ == '__main__':

	dummy = "dummy"

	app.run(debug=True)