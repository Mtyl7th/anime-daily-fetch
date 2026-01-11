import os
import requests
import time
import random
from xml.etree import ElementTree

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
GALLERY_PATH = os.path.join(IMAGE_DIR, "gallery.html")

def get_existing_ids():
    if not os.path.exists(IMAGE_DIR):
        return set()
    files = os.listdir(IMAGE_DIR)
    ids = set()
    for f in files:
        # Expected format: image_ID.ext
        if f.startswith("image_") and "_" in f:
            try:
                # remove extension and prefix
                base = os.path.splitext(f)[0]
                image_id = base.split("_")[1]
                ids.add(image_id)
            except IndexError:
                pass
    return ids

def generate_gallery():
    if not os.path.exists(IMAGE_DIR):
        print("Image directory not found.")
        return

    images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    images.sort(key=lambda x: os.path.getmtime(os.path.join(IMAGE_DIR, x)), reverse=True) # Newest first
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anime Image Gallery</title>
    <style>
        body { font-family: sans-serif; background-color: #f0f0f0; margin: 0; padding: 20px; }
        h1 { text-align: center; color: #333; }
        .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; }
        .gallery-item { background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
        .gallery-item img { max-width: 100%; height: auto; border-radius: 4px; display: block; }
        .caption { margin-top: 5px; font-size: 0.8em; color: #666; word-break: break-all; }
        .timestamp { font-size: 0.7em; color: #999; margin-top: 2px; }
    </style>
</head>
<body>
    <h1>JK & Thighhighs Collection</h1>
    <p style="text-align:center">Updated: """ + time.ctime() + """</p>
    <div class="gallery">
"""
    
    for img in images:
        html_content += f"""        <div class="gallery-item">
            <a href="{img}" target="_blank"><img src="{img}" alt="{img}" loading="lazy"></a>
            <div class="caption">{img}</div>
        </div>
"""

    html_content += """    </div>
</body>
</html>"""

    with open(GALLERY_PATH, 'w') as f:
        f.write(html_content)
    print("Gallery updated.")

def fetch_one_new_image():
    existing = get_existing_ids()
    print(f"Found {len(existing)} existing images.")
    
    base_url = "https://safebooru.org/index.php"
    tags = "school_uniform thighhighs rating:general"
    
    # Try a few pages to find a new image
    for _ in range(5):
        page = random.randint(0, 100) # Random page to ensure variety
        params = {
            "page": "dapi",
            "s": "post",
            "q": "index",
            "tags": tags,
            "limit": 20,
            "pid": page
        }
        
        try:
            print(f"Checking page {page}...")
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            root = ElementTree.fromstring(response.content)
            posts = root.findall('post')
            
            for post in posts:
                image_id = post.get('id')
                if image_id not in existing:
                    # Found a new one!
                    image_url = post.get('file_url')
                    if not image_url.startswith('http'):
                         if image_url.startswith('//'):
                             image_url = "https:" + image_url
                         else:
                             continue

                    ext = os.path.splitext(image_url)[1]
                    filename = f"image_{image_id}{ext}"
                    filepath = os.path.join(IMAGE_DIR, filename)
                    
                    print(f"Downloading new image: {filename}")
                    img_data = requests.get(image_url, timeout=10).content
                    with open(filepath, 'wb') as f:
                        f.write(img_data)
                    
                    return True # Success
                    
        except Exception as e:
            print(f"Error: {e}")
            
    print("Could not find a new image after 5 attempts.")
    return False

if __name__ == "__main__":
    if fetch_one_new_image():
        generate_gallery()
    else:
        print("No new image added.")
