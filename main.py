from PIL import Image

def crop_to_coordinates(input_image_path, output_image_path, left, top, right, bottom):
    # Open the image using Pillow
    image = Image.open(input_image_path)
    
    # Crop the image based on the specified coordinates
    cropped_image = image.crop((left, top, right, bottom))
    
    # Save the cropped image to the output path
    cropped_image.save(output_image_path)

input_path= input("Enter path of Input Images Folder: ")
output_path= input("Enter path of Output Images Folder: ")

left = 10  # Replace with the left edge coordinate
top = 380  # Replace with the top edge coordinate
right = 400 # Replace with the right edge coordinate
bottom = 1039-200  # Replace with the bottom edge coordinate

for i in range(1,6):
    input_image_path= input_path+str(i)+".png"
    output_image_path= output_path+str(i)+"(i).png"
    crop_to_coordinates(input_image_path, output_image_path, left, top, right, bottom)
  
left = 790  # Replace with the left edge coordinate
top = 50  # Replace with the top edge coordinate
right = 1920 # Replace with the right edge coordinate
bottom = 1039-600  # Replace with the bottom edge coordinate

for i in range(1,6):
    input_image_path= input_path+str(i)+".png"
    output_image_path= output_path+str(i)+"(ii).png"
    crop_to_coordinates(input_image_path, output_image_path, left, top, right, bottom)
