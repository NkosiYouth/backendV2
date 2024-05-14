from flask import Flask, request, jsonify
import subprocess  # For running the Python script

app = Flask(__name__)

@app.route('/api/extract-youth', methods=['POST'])
def extract_youth():
    data = request.get_json()
    cohort = data.get('cohort')
    export_type = data.get('exportType')

    # Run the Python script with the selected cohort and export type
    try:
        result = subprocess.run(
            ["python", "scripts\extract_youth.py"],  # Replace with the actual path to your script
            input=f"{cohort}\n{export_type}\n", 
            text=True, capture_output=True
        )
        
        # Handle result.stdout (e.g., send file download link)
        # ...
        
        return jsonify({"message": "Data extraction successful"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error extracting data: {e.stderr}"}), 500

if __name__ == '__main__':
    app.run()
