
import threading
import webbrowser
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/greet')
def greet():
    hour_str = request.args.get('hour', '')
    try:
        hour = int(hour_str)
        if hour < 0 or hour > 23:
            raise ValueError
    except ValueError:
        hour = None
    return render_template('greet.html', hour=hour)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/greet?hour=9')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
