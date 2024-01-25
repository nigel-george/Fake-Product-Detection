import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from django.http import JsonResponse
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

from PIL import Image
import numpy as np
model = load_model('C:/Users/16473/Downloads/FakeImageDetector/project/FakeImageDetector/vgg19_grayscale.h5')
def model_predict_binary(img_path, model, threshold=0.5):
    img = Image.open(img_path)
    img = img.resize((120, 120))  # Resize the image to (120, 120)

    # Preprocessing the image
    x = np.array(img)
    x = x / 255.0  # Normalize the pixel values
    x = np.expand_dims(x, axis=0)

    # Make prediction
    preds = model.predict(x)
    confidence = preds[0][0]  # Probability of the positive class

    if confidence >= threshold:
        prediction = "Fake"
    else:
        prediction = "Real"

    return prediction, confidence



def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        image_path = os.path.join(settings.MEDIA_ROOT, fs.save(uploaded_image.name, uploaded_image))

        new_image_path = image_path

        prediction, confidence = model_predict_binary(new_image_path, model, threshold=0.5)

        response_data = {
            'prediction': prediction,
            
        }
        
        return JsonResponse(response_data)

    return render(request, 'upload.html')
