from django.shortcuts import render
import requests
#%matplotlib inline    # If you are using a Jupyter notebook, uncomment the following line.
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from gtts import gTTS
from playsound import playsound
import datetime
import cv2
from django.http import HttpResponse


def index(request):
    if request.method=="POST":
        username=request.POST.get('command')
        
        if username=="capture":
            
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                ifcap,frame = cap.read() 
                cap.release()
                if ifcap and frame is not None:
                    now=datetime.datetime.now()                    
                    image_path=now.strftime("C:\\Users\\shubham\\Desktop\\ArtificialVision_project\\static\\project_log\\images\\%Y_%m_%d_%H_%M_%S.jpg")
                    
                    cv2.imwrite(image_path, frame)
                    response="Captured"
        
#         subscription_key = "a5d335b6092f4f88afd056dc594f756c"
#         assert subscription_key        
#         vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
#         analyze_url = vision_base_url + "analyze"
#         # Read the image into a byte array
#         image_data = open(image_path, "rb").read()
#         headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
#                       'Content-Type': 'application/octet-stream'}
#         params     = {'visualFeatures': 'Categories,Description,Color'}
#         response = requests.post(
#             analyze_url, headers=headers, params=params, data=image_data)
#         response.raise_for_status()
        
#         analysis = response.json()
#         print(analysis)
#         try:
#             image_caption = analysis["description"]["captions"][0]["text"].capitalize()
#         except:
#              image_caption = "Sorry, I am not able to understand! Please try again."
#         # Display the image and overlay it with the caption.
#         image = Image.open(BytesIO(image_data))
#         plt.imshow(image)
#         plt.axis("off")
#         _ = plt.title(image_caption, size="x-large", y=-0.1)


#         language = "en"
#         resultobj = gTTS(text=image_caption, lang=language, slow=False)

#         now1=datetime.datetime.now()
#         audio_path=now1.strftime("C:/Users/shubham/Desktop/project_log/audio/%Y_%m_%d_%H_%M_%S.mp3")
#         resultobj.save(audio_path)
#         playsound(audio_path)
#         response=image_caption
#         return render(request,'index.html',{'response':response,'image_url':image_path[-23:]})
#     return render(request,'index.html')

