from flask import Flask, render_template, request, send_file
import elabreport

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form:
        username = request.form['name']
        password = request.form['password']
        elabx = request.form['elab']

        print(username + password + elabx)

        elabreport.gen_report(username, password, elabx)

        filename = username + '-' + elabx.upper() + '.pdf'

        return send_file('./' + filename, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)