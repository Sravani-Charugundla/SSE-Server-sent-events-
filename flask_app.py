from flask import Flask, Response,render_template
import time

app = Flask(__name__)



def event_stream():
    """Generator that yields data every second."""
    for i in range(1, 6):  # Send 5 updates
        # Yield a message to the client and pause execution until the next iteration
        yield f"data: Message {i}\n\n"
        time.sleep(1)


@app.route('/')
def index():  # Renamed to index for clarity
    return render_template('index.html')  # Serve the HTML file

@app.route('/stream')
def stream():
    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True, threaded=True,port = 5500)  # Allows the server to handle multiple requests simultaneously
