from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/script/extract-youth', methods=['POST'])
def extract_youth():
    data = request.get_json()
    cohort = data.get('cohort')
    export_type = data.get('exportType')

    # Run the Python script with the selected cohort and export type
    try:
        result = subprocess.run(
            ["python", "scripts/extract_youth.py"],  # Use correct path separator for the OS
            input=f"{cohort}\n{export_type}\n", 
            text=True, capture_output=True, check=True
        )
        
        # Handle result.stdout (e.g., send file download link)
        # Here assuming your script prints a download link or success message
        output = result.stdout.strip()
        
        return jsonify({"message": "Data extraction successful", "output": output}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error extracting data: {e.stderr}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
