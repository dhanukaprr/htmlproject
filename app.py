from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (for simplicity, using dictionaries)
trucks = {}  # {serial_no: {'weight': ..., 'approved': ..., 'tank': ..., 'separator': ..., 'bulk_tank': ...}}
next_serial_no = 1

@app.route('/')
def index():
    return render_template('index.html', trucks=trucks)

# Weigh Bridge Route
@app.route('/weigh_bridge', methods=['GET', 'POST'])
def weigh_bridge():
    global next_serial_no
    if request.method == 'POST':
        weight = request.form['weight']
        serial_no = next_serial_no
        next_serial_no += 1
        trucks[serial_no] = {'weight': weight, 'approved': None, 'tank': None, 'separator': None, 'bulk_tank': None}
        return redirect(url_for('index'))
    return render_template('weigh_bridge.html')

# Lab Testing Route
@app.route('/lab_testing/<int:serial_no>', methods=['GET', 'POST'])
def lab_testing(serial_no):
    if request.method == 'POST':
        approved = request.form['approved'] == 'yes'
        trucks[serial_no]['approved'] = approved
        return redirect(url_for('index'))
    return render_template('lab_testing.html', serial_no=serial_no)

# Latex Tank Route
@app.route('/latex_tank/<int:serial_no>', methods=['GET', 'POST'])
def latex_tank(serial_no):
    if request.method == 'POST':
        tank = request.form['tank']
        trucks[serial_no]['tank'] = tank
        return redirect(url_for('index'))
    return render_template('latex_tank.html', serial_no=serial_no)

# Separator Route
@app.route('/separator/<int:serial_no>', methods=['GET', 'POST'])
def separator(serial_no):
    if request.method == 'POST':
        separator = request.form['separator']
        trucks[serial_no]['separator'] = separator
        return redirect(url_for('index'))
    return render_template('separator.html', serial_no=serial_no)

# Bulk Tank Route
@app.route('/bulk_tank/<int:serial_no>', methods=['GET', 'POST'])
def bulk_tank(serial_no):
    if request.method == 'POST':
        bulk_tank = request.form['bulk_tank']
        trucks[serial_no]['bulk_tank'] = bulk_tank
        return redirect(url_for('index'))
    return render_template('bulk_tank.html', serial_no=serial_no)

if __name__ == '__main__':
    app.run(debug=True)
