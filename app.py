from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Your Solana wallet address
SOLANA_ADDRESS = '9tF5acx2XK2P3Rh3WGt8PhazhjNeZMtSxrBdVUvDPq4k'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/verify_payment', methods=['POST'])
def verify_payment():
    # This is where you would implement logic to verify payment on the Solana blockchain.
    # For now, this is a mock implementation.
    data = request.json
    sol_amount = data.get('solAmount')
    print(f"Received payment verification request for {sol_amount} SOL.")
    
    # Simulate verification delay
    time.sleep(2)
    
    # Simulate a successful payment verification response
    return jsonify({'status': 'success', 'message': 'Payment verified successfully!'})

if __name__ == '__main__':
    app.run(debug=True)

