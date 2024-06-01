This script will set up a virtual environment, activate it, install the necessary requirements, run a Python application, and then access specific endpoints of the application.

1. python -m venv venv (Create a virtual environment)
2. .\venv\Scripts\activate (Activate the virtual environment)
3. pip install -r requirements.txt (Install the necessary requirements)
4. python app.py (Run the Python application)
5. http://127.0.0.1:5000/api/driving_licenses (Access the 'driving_licenses' endpoint)
6. http://127.0.0.1:5000/api/driving_licenses/DL2233445566 (Access a specific 'driving_license' with licenseNumber DL2233445566)
