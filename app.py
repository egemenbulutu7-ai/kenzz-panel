from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Kenzz Kaneki System - Siber Üs Veri Deposu
data_store = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KENZZ KANEKI | SIBER PANEL</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            /* Arka planı tamamen dolgulu siber mavi yapıyoruz */
            background: radial-gradient(circle, #001220 0%, #000a12 100%);
            color: #bc13fe; /* Yazılar mor */
            font-family: 'Orbitron', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            overflow-x: hidden;
        }
        .container {
            background: rgba(0, 20, 40, 0.8); /* Panelin arkası hafif şeffaf lacivert */
            padding: 30px;
            border-radius: 15px;
            border: 2px solid #00f2ff; /* Kenarlar neon mavi */
            box-shadow: 0 0 25px #00f2ff, inset 0 0 15px #00f2ff;
            width: 80%;
            max-width: 900px;
        }
        h1 {
            text-align: center;
            color: #bc13fe; /* Başlık Mor */
            text-shadow: 0 0 15px #bc13fe, 0 0 30px #bc13fe;
            letter-spacing: 5px;
            font-size: 2.5rem;
            margin-bottom: 30px;
        }
        .data-card {
            background: rgba(0, 0, 0, 0.5);
            border-left: 5px solid #bc13fe; /* Kartların kenarı mor */
            margin: 15px 0;
            padding: 15px;
            border-radius: 5px;
            transition: 0.3s;
            box-shadow: 0 0 10px rgba(188, 19, 254, 0.2);
        }
        .data-card:hover {
            transform: scale(1.02);
            background: rgba(188, 19, 254, 0.1);
        }
        .footer {
            margin-top: 20px;
            font-size: 0.8rem;
            color: #00f2ff;
            text-shadow: 0 0 5px #00f2ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>KENZZ KANEKI SYSTEM</h1>
        <div id="data-container">
            {% if data %}
                {% for item in data %}
                    <div class="data-card">
                        <strong>LOG:</strong> {{ item }}
                    </div>
                {% endfor %}
            {% else %}
                <p style="text-align:center; color:#00f2ff;">Sistem Aktif. Veri bekleniyor...</p>
            {% endif %}
        </div>
    </div>
    <div class="footer">KENZZ KANEKI | DARK WEB ACCESS GRANTED</div>
</body>
</html>
'''

@app.route('/kenzz-kontrol')
def control_panel():
    return render_template_string(HTML_TEMPLATE, data=data_store)

@app.route('/api/data', methods=['POST'])
def receive_data():
    content = request.json
    if content:
        data_store.append(content)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)