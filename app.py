# app.py
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

SCRIPTS = {
    'script1': '/home/taoreed/code1.py',
    'script2': '/home/taoreed/code2.py',
    # Add more scripts as needed
}

@app.route('/')
def index():
    return render_template('index.html', scripts=SCRIPTS.keys())


@app.route('/run_script', methods=['POST'])
def run_script():
    selected_script = request.form['selected_script']

    if selected_script not in SCRIPTS:
        return jsonify({'error': 'Invalid script selected'})

    script_path = SCRIPTS[selected_script]

    try:
        # Run the selected script and capture the output
        result = subprocess.check_output(['python', script_path], stderr=subprocess.STDOUT, text=True)

        return jsonify({'result': result.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output.strip()})

if __name__ == '__main__':
    app.run(debug=True)

    
#Create HTML Template:
#Create an HTML template (e.g., templates/index.html) to display the form and handle the script selection.

<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Script Runner</title>
</head>
<body>
    <h1>Script Runner</h1>
    <form action="/run_script" method="post">
        <label for="selected_script">Select Python Script:</label><br>
        <select id="selected_script" name="selected_script">
            {% for script in scripts %}
                <option value="{{ script }}">{{ script }}</option>
            {% endfor %}
        </select><br>
        <input type="submit" value="Run Script">
    </form>
</body>
</html>
