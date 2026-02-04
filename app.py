from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Kenzz Kaneki System - Siber Veri Havuzu
data_store = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KENZZ KANEKI | SIBER PANEL</title>
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #000a12; /* Derin Siber Siyah */
            color: #bc13fe; /* Ana yazılar Mor */
            font-family: 'Courier Prime', monospace; /* O eski terminal tipi yazı */
            margin: 0;
            padding: 20px;
            line-height: 1.2;
        }
        .header {
            color: #00f2ff; /* Başlık Neon Mavi */
            text-align: center;
            border-bottom: 1px solid #00f2ff;
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #00f2ff;
        }
        .log {
            margin-bottom: 5px;
            word-wrap: break-word;
            white-space: pre-wrap;
        }
        .prefix {
            color: #00f2ff; /* [+] işareti Mavi */
            font-weight: bold;
            margin-right: 10px;
        }
        .status {
            color: #00f2ff;
            text-align: center;
            margin-top: 20px;
            border-top: 1px solid #333;
            padding-top: 10px;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <div class="header">
        === KENZZ KANEKI SYSTEM - SIBER KONTROL MERKEZI ===
    </div>
    
    <div id="log-container">
        {% if data %}
            {% for item in data %}
                <div class="log">
                    <span class="prefix">[+]</span>{{ item }}
                </div>
            {% endfor %}
        {% else %}
            <div style="color: #00f2ff; text-align: center;">[!] SISTEM AKTIF - VERI AKISI BEKLENIYOR...</div>
        {% endif %}
    </div>

    <div class="status">
        KENZZ KANEKI V14 | CONNECTION: SECURE | THEME: NEON-V2
    </div>
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
    app.run(host='0.0.0
