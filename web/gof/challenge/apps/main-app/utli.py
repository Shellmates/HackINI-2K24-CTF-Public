import subprocess

def run_curl(url):
    try:
        result = subprocess.run(['curl', url], capture_output=True, text=True, check=True,timeout=2)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running curl with url: {url}"

