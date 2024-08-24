from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Ajastimen loppuaika (24 tuntia nykyisestä ajasta)
end_time = datetime.now() + timedelta(days=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    sol_amount = float(request.json['solAmount'])
    pepe_amount = sol_amount * 1200
    return jsonify(pepeAmount=pepe_amount)

@app.route('/timer')
def timer():
    remaining_time = end_time - datetime.now()
    seconds_left = remaining_time.total_seconds()
    if seconds_left <= 0:
        # Jos aika on loppunut, aloita uusi ajastin
        global end_time
        end_time = datetime.now() + timedelta(days=1)
        seconds_left = 86400  # 24 tuntia sekunteina
    return jsonify(seconds_left=seconds_left)

if __name__ == '__main__':
    app.run(debug=True)
