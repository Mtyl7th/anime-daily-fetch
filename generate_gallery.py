import os

def generate_gallery():
    image_dir = "/Users/linchuan/.gemini/antigravity/brain/4838b3fe-93ca-44a3-ba32-d37f4b912c9b/images"
    gallery_path = "/Users/linchuan/.gemini/antigravity/brain/4838b3fe-93ca-44a3-ba32-d37f4b912c9b/images/gallery.html"
    
    if not os.path.exists(image_dir):
        print("Image directory not found.")
        return

    images = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    images.sort()
    
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
    </style>
</head>
<body>
    <h1>JK & Thighhighs Collection</h1>
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

    with open(gallery_path, 'w') as f:
        f.write(html_content)
    
    print(f"Gallery created at {gallery_path} with {len(images)} images.")

if __name__ == "__main__":
    generate_gallery()
