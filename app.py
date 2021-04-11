  
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        weight = request.form['weight']
        operation = request.form['operation']

        if operation == 'Jupiter':
            sum = "Your weight in that planet will be: " + str(int((int(weight)*24.79)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Moon':
            sum = "Your weight in that planet will be: " + str(int((int(weight)*1.62)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Mars':
            sum = "Your weight in that planet will be: " + str(int((int(weight)*3.7)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Saturn':
            sum = "Your weight in that planet will be: " + str(int((int(weight)*10.44)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
