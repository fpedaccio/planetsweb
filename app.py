  
from flask import Flask, render_template, request
from web3 import Web3
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        Addres = request.form['addres']
        from web3 import Web3

        node = "https://mainnet.infura.io/v3/7cad44d68f7e4c5fa5935f78d354e696"

        connect = Web3(Web3.HTTPProvider(node))

        balance = connect.eth.get_balance(Addres)
        balance = connect.fromWei(balance, "ether")


            
        sum = "The balance of your ethereum addres is:, " + str(balance) + " ether"
        return render_template('app.html', sum=sum)

        

if __name__ == ' __main__':
    app.debug = True
    app.run()
