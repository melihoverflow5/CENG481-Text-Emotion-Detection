import subprocess
import sys

def run_flask():
    # Run your Flask app (adjust filename if needed)
    return subprocess.Popen([sys.executable, "app.py"])

def run_streamlit():
    # Run your Streamlit app (adjust filename if needed)
    return subprocess.Popen([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])

if __name__ == "__main__":
    print("Starting Flask API and Streamlit app...")
    flask_proc = run_flask()
    streamlit_proc = run_streamlit()

    try:
        flask_proc.wait()
        streamlit_proc.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
        flask_proc.terminate()
        streamlit_proc.terminate()
