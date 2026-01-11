import os
import requests
import time
from xml.etree import ElementTree

def fetch_images():
    # Safebooru API URL
    base_url = "https://safebooru.org/index.php"
    
    # Directory to save images
    save_dir = "/Users/linchuan/.gemini/antigravity/brain/4838b3fe-93ca-44a3-ba32-d37f4b912c9b/images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Search tags: school_uniform + thighhighs + safe rating
    # standardizing on 'thighhighs' for over-the-knee socks which is the booru standard
    tags = "school_uniform thighhighs rating:general"
    
    params = {
        "page": "dapi",
        "s": "post",
        "q": "index",
        "tags": tags,
        "limit": 30, # Request 30 images
        "pid": 0 # Page 0
    }

    print(f"Fetching images with tags: {tags}")
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Parse XML response
        root = ElementTree.fromstring(response.content)
        posts = root.findall('post')
        
        print(f"Found {len(posts)} images.")
        
        count = 0
        for post in posts:
            if count >= 30:
                break
                
            image_url = post.get('file_url')
            # Safebooru sometimes gives relative paths or missing protocol
            if not image_url.startswith('http'):
                 # Safebooru usually provides "//safebooru.org/..."
                 if image_url.startswith('//'):
                     image_url = "https:" + image_url
                 else:
                     # Fallback if unknown format, though usually it's fully qualified or //
                     print(f"Skipping malformed URL: {image_url}")
                     continue

            image_id = post.get('id')
            ext = os.path.splitext(image_url)[1]
            filename = f"image_{image_id}{ext}"
            filepath = os.path.join(save_dir, filename)
            
            # Download image
            try:
                print(f"Downloading {count+1}/30: {image_url}")
                img_data = requests.get(image_url, timeout=10).content
                with open(filepath, 'wb') as f:
                    f.write(img_data)
                count += 1
                time.sleep(0.5) # Be nice to the server
            except Exception as e:
                print(f"Failed to download {image_url}: {e}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_images()
