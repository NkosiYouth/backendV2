from flask import Flask, request, jsonify
import subprocess  # For running the Python script

def extract_youth():
    data = request.get_json()
    cohort = data.get('cohort')
    export_type = data.get('exportType')

    # Run the Python script with the selected cohort and export type
    try:
        result = subprocess.run(
            ["python", "scripts\extract_youth.py", cohort, export_type],
            text=True, 
            capture_output=True,
            check=True 
        )
        
        # Handle result.stdout (e.g., send file download link)
        # ...
        
        return jsonify({"message": "Data extraction successful"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error extracting data: {e.stderr}"}), 500