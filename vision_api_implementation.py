import requests
%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
subscription_key = "57cb082c23104931a21990b593e2aa06"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

image_path = "E:/Siddharth/sdcard1/jesus52.jpg"

# Reading the image
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params     = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(image_caption)
## Displaying the image and overlaying it with the caption.
#image = Image.open(BytesIO(image_data))
#plt.imshow(image)
#plt.axis("off")
#_ = plt.title(image_caption, size="x-large", y=-0.1)