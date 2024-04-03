from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)


@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coming Soon</title>
        <style>
            body {
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
            }
            h1 {
                font-size: 50px;
                margin-bottom: 0;
            }
            p {
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1 id="countdown">10</h1>
            <p>Seconds until launch</p>
        </div>
        <script>
            var countdown = document.getElementById('countdown');
            var seconds = 10;
            function updateCountdown() {
                seconds--;
                countdown.innerText = seconds;
                if (seconds <= 0) {
                    clearInterval(intervalId);
                    countdown.innerText = 'Launched!';
                }
            }
            var intervalId = setInterval(updateCountdown, 1000);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
