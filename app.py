  
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
            sum = "Your weight in Jupiter will be: " + str(int((int(weight)*24.79)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Moon':
            sum = "Your weight in the Moon will be: " + str(int((int(weight)*1.62)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Mars':
            sum = "Your weight in Mars will be: " + str(int((int(weight)*3.72)/9.8)) + " KG"
            return render_template('app.html', sum=sum)

        elif operation == 'Saturn':
            sum = "Your weight in Saturn will be: " + str(int((int(weight)*10.44)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        
        elif operation == 'Venus':
            sum = "Your weight in Venus will be: " + str(int((int(weight)*8.87)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Mercury':
            sum = "Your weight in Mercury will be: " + str(int((int(weight)*3.70)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Uranus':
            sum = "Your weight in Uranus will be: " + str(int((int(weight)*8.87)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Neptune':
            sum = "Your weight in Neptune will be: " + str(int((int(weight)*11.15)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Europa':
            sum = "Your weight in the Europa Moon will be: " + str(int((int(weight)*1.31)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Sun':
            sum = "You will be hot as fuck. But your weight in the sun will be: " + str(int((int(weight)*274)/9.8)) + " KG"
            return render_template('app.html', sum=sum)
        elif operation == 'Black hole':
            sum = "You probably won't be in one piece. But your weight would be ∞"
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
