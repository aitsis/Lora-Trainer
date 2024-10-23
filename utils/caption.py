import os
import base64
from ollama import Client
from config import ConfigHandler
from concurrent.futures import ThreadPoolExecutor, wait

USER_PROMPT = """
Give me a text-to-image prompt for this image, separated by commas. 
Make it simple and suitable for AI training. 
I want a long sentence formatted as keywords, not a story. 
My model needs clarity.
Separate the prompt as keywords, with a minimum of 10 and a maximum of 30 words. 
Make it ultra-detailed and Keywords must be maximum 4 words long.
Inspect every pixel of the image and generate the best result. 
Highlight intricate details of the [IMAGE_STYLE] design.
The primary style of the image is "[IMAGE_STYLE]".
Ensure accuracy and exclusivity to "[IMAGE_STYLE]" without mixing in other styles.
Provide refined output separated by commas and without quotes or prefixes.
Don't put "Create a " in front of the prompt. Just give keywords seperated by commas without quotes.
"""

config = ConfigHandler("config/appconfig.json")
client = Client(host=config.get_key("ollama_url"))

def caption_images(source_dir, save_folder):
    image_style = input("Enter the image style (Paisley, Abstract, etc.): ")
    replaced_prompt = USER_PROMPT.replace("[IMAGE_STYLE]", image_style)

    # Get all image files
    image_files = [f for f in os.listdir(source_dir) if f.endswith('.png')]
    
    # Split images into batches of 15
    batches = [image_files[i:i+15] for i in range(0, len(image_files), 15)]
    total_batches = len(batches)

    # Process each batch sequentially
    for idx, batch in enumerate(batches, 1):
        print(f"Processing batch {idx}/{total_batches}")  # Log batch progress
        with ThreadPoolExecutor(max_workers=15) as executor:  # Limit to 15 requests at a time
            futures = [executor.submit(process_image, image_file, source_dir, replaced_prompt, save_folder) for image_file in batch]
            wait(futures)  # Wait for all 15 requests in the batch to finish before moving to the next batch

def process_image(image_file, source_dir, prompt, save_folder):
    # Encode image as base64
    image_path = os.path.join(source_dir, image_file)
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')
    
    # Get the caption for the image
    caption = get_caption(base64_image, prompt)
    
    # Save caption to file (same name as image, but with .txt)
    save_path = os.path.join(save_folder, image_file.replace('.png', '.txt'))
    with open(save_path, "w") as f:
        f.write(caption)

def get_caption(base64_image, prompt):
    res = client.chat(
        model="llava:34b",
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [base64_image]
            }
        ]
    )
    return res['message']['content']
