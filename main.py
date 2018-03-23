from flask import Flask
app = Flask(__name__)

@app.route('/')
    return redirect('https://fragforce.org', code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 443))
    app.run(host='0.0.0.0', port=port)
