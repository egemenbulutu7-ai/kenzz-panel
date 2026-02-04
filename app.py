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
            /* Arka plan dolgulu siber mavi */
            background: radial-gradient(circle, #001220 0%, #000a12 100%);
            color: #bc13fe; 
            font-family: 'Orbitron', sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            color: #00f2ff; /* Başlık Neon Mavi */
            text-shadow: 0 0 15px #00f2ff;
            letter-spacing: 5px;
            margin-bottom: 40px;
        }
        #data-container {
            width: 100%;
            max-width: 1200px; /* Daha geniş alan */
        }
        .data-log {
            /* Eski tarzdaki gibi geniş ve sade ama neon renkli */
            background: rgba(188, 19, 254, 0.05); 
            border-bottom: 1px solid rgba(0, 242, 255, 0.3);
            padding: 15px;
            margin-bottom: 10px;
            word-wrap: break-word; /* Uzun loglar taşmasın */
            font-size: 0.9rem;
            line-height: 1.6;
            color: #bc13fe; /* Yazılar Mor */
            text-shadow: 0 0 5px rgba(188, 19, 254, 0.5);
        }
        .footer {
            margin-top: 50px;
            color: #00f2ff;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <h1>KENZZ KANEKI SYSTEM</h1>
    <div id="data-container">
        {% if data %}
            {% for item in data %}
                <div class="data-log">
                    [SYSTEM_LOG] > {{ item }}
                </div>
            {% endfor %}
        {% else %}
            <p style="color:#00f2ff;">Sistem Aktif... Veri bekleniyor...</p>
        {% endif %}
    </div>
    <div class="footer">KENZZ KANEKI | ACCESS GRANTED</div>
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

