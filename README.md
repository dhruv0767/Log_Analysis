# Log File Analysis Tool

This repository contains a Python script designed for analyzing log files to extract sensitive information such as Aadhar numbers, PAN card details, account numbers, credit card details, CVV, passport numbers, and dates of birth. The tool scans text files within a specified directory, extracts information matching predefined patterns, and logs the results into a separate file.

## Features

- **Directory Navigation:** Automatically navigates to the specified log file directory.
- **Sensitive Data Identification:** Uses regular expressions to identify and extract various types of sensitive information.
- **Result Logging:** Outputs the findings into a log file, appending new results if the log file already exists.

## Requirements

- Python 3.x
- OS module (standard library)
- re module (standard library)

## Setup

1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the script directly.
3. Modify the `path` variable in the script to the directory containing your log files.

## Usage

Run the script in your Python environment:

```bash
python log_analysis.py
```

Make sure to execute the script in a directory that has permissions to read and write files, especially if you are navigating to system directories or modifying the `path` variable.

## Script Overview

- **Directory Setting:** Initially, the script sets the working directory to where the log files are stored.
- **File Processing:** Each `.txt` file in the directory is processed to find matches for predefined patterns representing different types of sensitive information.
- **Result Compilation:** Results are compiled and written to `result1.log`. If the file exists and already contains data, new results are appended.
- **Regular Expressions Used:**
  - **Aadhar:** Matches Aadhar card numbers.
  - **PAN Card:** Matches PAN card numbers.
  - **Account Numbers:** Matches various bank account numbers.
  - **Credit Cards:** Matches credit card numbers.
  - **CVV:** Identifies strings related to CVV.
  - **Passport:** Matches passport numbers.
  - **DOB:** Identifies date of birth entries.

## License

This project is open-source and available under the MIT License.
