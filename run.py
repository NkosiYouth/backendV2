from app import app
from flask_cors import CORS  # Import CORS

if __name__ == '__main__':
    CORS(app)
    app.run()
