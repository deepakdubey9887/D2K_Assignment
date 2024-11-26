import os
import time
import requests
# Directory to save the downloaded files
download_dir = "data"
os.makedirs(download_dir, exist_ok=True)

# Function to download a file with retry logic
def download_file(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Raise HTTPError for bad responses
            file_name = os.path.join(download_dir, url.split("/")[-1])
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
            return
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                time.sleep(delay)
            else:
                print(f"Failed to download {url} after {retries} attempts")