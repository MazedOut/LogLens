# LogLens Pro

LogLens Pro is a beginner-friendly web-based log analyzer that detects anomalies in log files and categorizes them by severity: High, Medium, Low. It provides a **color-coded web GUI** using Flask for easy visualization and reporting.



## Features

- Upload log files through a browser interface
- Detect anomalies such as failed logins, errors, or suspicious patterns
- Categorize anomalies by severity: High / Medium / Low
- Color-coded results for quick visual analysis
- Summary statistics for total logs, total anomalies, and severity counts
- Option to upload new logs and view updated results



## Requirements

- Python 3.8+
- Flask (`pip install flask`)

**Optional**:

- Any web browser (Chrome, Firefox, Edge)



## Installation

1. **Clone the repository**:
git clone https://github.com/yourusername/LogLens.git
cd LogLens
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Usage
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000/
On the homepage, upload a log file (e.g., system.log, access.log).

After uploading, you will see the results page:

Summary: total logs, total anomalies, severity counts

High / Medium / Low Severity Anomalies: listed in separate color-coded sections

Link to upload another log

#How It Works:
User uploads a log file through the web form.

app.py saves the file in uploads/ folder.

analyzer.py reads each line and detects anomalies based on patterns.

Results are categorized into High, Medium, and Low severity.

Flask renders results.html with summary statistics and color-coded anomaly lists.
