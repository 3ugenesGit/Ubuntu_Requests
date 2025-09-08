import requests
import os
import hashlib
from urllib.parse import urlparse

def safe_filename(url, content):
    """
    Generate a safe, unique filename for the image.
    Uses URL path or a hash of content if not available.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    
    if not filename or "." not in filename:  
        # Fall back to hash-based filename if none is available
        file_hash = hashlib.sha256(content).hexdigest()[:12]
        filename = f"image_{file_hash}.jpg"
    
    return filename

def download_image(url, save_dir, downloaded_hashes):
    """
    Download a single image with precautions.
    """
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()
        
        # Check Content-Type header to ensure it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (Not an image): {url}")
            return
        
        # Read content safely
        content = response.content
        
        # Prevent duplicate downloads using hash
        file_hash = hashlib.sha256(content).hexdigest()
        if file_hash in downloaded_hashes:
            print(f"⚠ Skipped duplicate: {url}")
            return
        downloaded_hashes.add(file_hash)
        
        # Generate safe filename
        filename = safe_filename(url, content)
        filepath = os.path.join(save_dir, filename)
        
        # Save image
        with open(filepath, 'wb') as f:
            f.write(content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Saved to: {filepath}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for collecting images from the web\n")
    
    # Ask user for multiple URLs
    urls_input = input("Enter one or more image URLs (comma separated): ").strip()
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]
    
    if not urls:
        print("✗ No URLs provided. Exiting.")
        return
    
    # Create directory for fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    
    # Track downloaded files by hash to avoid duplicates
    downloaded_hashes = set()
    
    for url in urls:
        download_image(url, save_dir, downloaded_hashes)
    
    print("\n✅ Process completed.")
    print("🤝 Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
