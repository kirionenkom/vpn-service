from flask import Flask

app = Flask(__name__)
app.secret_key = 'pJsxYoycJvUpmYkOLBfmEbcO7Zds5Tnaf5OviEw1SIAew2XgEy'
import routes


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443)
