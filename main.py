import subprocess

def get_chrome_version():
    try:
        version = subprocess.check_output(
            [r'C:\Program Files\Google\Chrome\Application\chrome.exe', '--version'],
            stderr=subprocess.STDOUT
        )
    except FileNotFoundError:
        try:
            version = subprocess.check_output(
                [r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', '--version'],
                stderr=subprocess.STDOUT
            )
        except FileNotFoundError:
            return "Google Chrome is not installed."
    return version.decode('utf-8').strip()

if __name__ == "__main__":
    print(f"Google Chrome version: {get_chrome_version()}")
