from flask import Flask, render_template, request
import os
from analyzer import analyze_logs  # Make sure analyzer.py is in the same folder

# Folder to store uploaded log files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route: shows upload form on GET,
    analyzes logs and shows results on POST.
    """

    # Initialize empty result to avoid template errors
    result = {
        "summary": {},
        "anomalies": [],
        "severity_report": {"High": [], "Medium": [], "Low": []}
    }

    if request.method == "POST":
        file = request.files.get("logfile")  # Get uploaded file
        if file:
            # Save file to uploads folder
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            # Read file lines and analyze
            with open(path, "r") as f:
                log_lines = f.read().splitlines()
            result = analyze_logs(log_lines)

            # Render results page after POST
            return render_template("results.html", result=result)

    # Render upload form on GET
    return render_template("index.html")


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)

