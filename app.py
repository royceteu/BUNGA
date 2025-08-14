from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def home():
    """
    Renders the index.html template when the root URL is accessed.
    Flask automatically looks for templates in the 'templates' folder.
    """
    return render_template('index.html')

# Route to serve static files (like CSS) from the 'static' folder
# This is explicitly defined to make it clear, though Flask handles 'static' by default
@app.route('/static/<path:filename>')
def static_files(filename):
    """
    Serves static files (CSS, JS, images, etc.) from the 'static' directory.
    The path:filename part captures the path after /static/
    """
    # Get the directory where this script (app.py) is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the static directory
    static_dir = os.path.join(current_dir, 'static')
    
    # Send the requested file from the static directory
    return send_from_directory(static_dir, filename)

if __name__ == '__main__':
    # Run the Flask application in debug mode.
    # Debug mode provides useful error messages and reloads the server
    # automatically when code changes are detected.
    app.run(debug=True)
