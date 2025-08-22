# CodSoft AI Internship – Task 3
# Basic Image Captioning Simulator
# Created by Payal Sonwaniya

def generate_caption(image_name):
    captions = {
        "dog.jpg": "A cute brown dog sitting on grass.",
        "mountain.jpg": "Snow-covered mountain under a blue sky.",
        "beach.jpg": "A peaceful beach with clear blue water.",
        "car.jpg": "A red sports car parked in front of a building.",
    }

    caption = captions.get(image_name.lower(), "No caption available for this image.")
    return caption

# Example usage
image = input("Enter image file name (e.g., dog.jpg): ")
caption = generate_caption(image)
print("\n🖼️ Image Caption:")
print(caption)
