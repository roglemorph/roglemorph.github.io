from flask import Flask, render_template, request, redirect, url_for
import time
import threading

app = Flask(__name__)

# Global variable to store the timer duration and status
timer_duration = 0
is_running = False

def run_timer(duration):
    global is_running
    is_running = True
    time.sleep(duration)
    is_running = False

@app.route('/')
def index():
    return render_template('index.html', is_running=is_running)

@app.route('/start', methods=['POST'])
def start_timer():
    global timer_duration
    timer_duration = int(request.form['duration']) * 60  # Convert minutes to seconds
    threading.Thread(target=run_timer, args=(timer_duration,)).start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)