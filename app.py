  
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
            sum = (float(weight)*24.79)/9.8
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
