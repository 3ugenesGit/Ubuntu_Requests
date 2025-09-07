# Ubuntu Image Fetcher

A Python tool for **mindfully collecting images from the web**, inspired by the Ubuntu principles of **Community, Respect, Sharing, and Practicality**.  

This script allows you to fetch one or more images from URLs, organize them in a dedicated folder, and avoid duplicates while handling errors gracefully.

---

## Features

- **Multiple URL support** → Input comma-separated image URLs.  
- **Error handling** → Gracefully manages network failures and invalid URLs.  
- **Content-Type validation** → Ensures only images are downloaded.  
- **Duplicate prevention** → Skips files already downloaded by comparing image hashes.  
- **Organized storage** → Saves images in a `Fetched_Images/` folder.  
- **Safe filenames** → Extracts from URL or generates unique names if missing.  

---

## 🛠 Requirements

- Python 3.7+
- `requests` library  

Install dependencies:

```bash
pip install requests

Usage

Clone or download this repository.

Run the script:
python ubuntu_image_fetcher.py


Enter one or more image URLs when prompted. Example:

Enter one or more image URLs (comma separated): 
https://example.com/image1.jpg, https://example.com/photo.png


Images will be saved in the Fetched_Images/ directory.

Precautions

The program checks the HTTP Content-Type header to ensure files are images.

Images are hashed using SHA-256 to prevent duplicate downloads.

Handles timeouts, connection issues, and invalid responses respectfully.



Ubuntu Principles in Action

Community → Connects to the wider web, fetching from multiple sources.

Respect → Handles errors gracefully without crashing.

Sharing → Organizes images for easy reuse or collaboration.

Practicality → Provides a real tool for mindful content collection.

Example Output
Welcome to the Ubuntu Image Fetcher
A mindful tool for collecting images from the web

Enter one or more image URLs (comma separated): 
https://www.example.com/cat.jpg, https://www.example.com/dog.png

✓ Successfully fetched: cat.jpg
✓ Saved to: Fetched_Images/cat.jpg
✓ Successfully fetched: dog.png
✓ Saved to: Fetched_Images/dog.png

Connection strengthened. Community enriched.

