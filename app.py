from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            # محاولة جلب كود الموقع
            response = requests.get(url)
            code = response.text
        except Exception as e:
            code = f"خطأ: تعذر جلب الموقع - {str(e)}"
    return render_template('index.html', code=code)

if __name__ == '__main__':
    app.run(debug=True)
