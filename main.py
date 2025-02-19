from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("forms.html")

@app.route('/', methods=['POST'])
def gerar_qrcode():
    base_qr_url = request.form.get("url")
    try:
        qr = qrcode.make(base_qr_url)
        qr.save("qrcode.png")
        success = True
        error_message = None
        return send_file("qrcode.png", as_attachment=True)
    except Exception as e:
        success = False
        error_message = str(e)
    return render_template('forms.html', success=success, error_message=error_message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500, debug=True)
