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


