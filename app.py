from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/static/<path:filename>')
def static_files(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, 'static')

    return send_from_directory(static_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)

