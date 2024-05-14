from app import app

if __name__ == '__main__':
    CORS(app)
    app.run()
