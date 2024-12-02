from PIL import Image, ImageDraw

# Load the image 
image = Image.open("./me.jpg").convert("RGBA") 

#Create circular mask
mask = Image.new("L",image.size,0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,image.size[0],image.size[1]),fill=255)

#Apply the mask
result = Image.new("RGBA",image.size)
result.paste(image,(0,0),mask)


#save Thecircular cropped image
result.save("c_me.png")