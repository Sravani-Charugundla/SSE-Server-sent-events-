# Flask Server-Sent Events Example

This project demonstrates a simple Flask application that uses Server-Sent Events (SSE) to send real-time updates to a web page. The application serves an HTML page that connects to a Flask backend, which streams messages to the client.

## Features

- Real-time updates using Server-Sent Events
- Simple Flask backend
- Clean separation of HTML and Python code

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/yourusername/flask-sse-example.git
   cd flask-sse-example
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Flask**:
   ```bash
   pip install Flask
   ```


## Usage

1. **Run the Flask application**:
   ```bash
   python flask_app.py
   ```

2. **Open your web browser** and navigate to:
   [http://127.0.0.1:5500/](http://127.0.0.1:5500/)

3. You should see the "Server-Sent Events Example" page, which will display messages sent from the server every second.

## Customization

- You can modify the `event_stream` function in `flask_app.py` to change the messages sent to the client or the frequency of updates.
- Update the HTML in `templates/index.html` to customize the appearance or functionality of the web page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask documentation: [Flask](https://flask.palletsprojects.com/)
- Jinja2 documentation: [Jinja2](https://jinja.palletsprojects.com/)


