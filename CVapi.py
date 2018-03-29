from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

projectid = '91c2afcb-d86e-470b-a884-4a8e0238590c'
# Replace with a valid key
training_key = "a1d72f86f97d42578ca75f7f7320f686"
prediction_key = "82d2bd2e2c4444c590bc80e242800c58"
trainer = training_api.TrainingApi(training_key)

predictor = prediction_endpoint.PredictionEndpoint(prediction_key)
iteration = trainer.train_project(projectid)
results = predictor.predict_image(projectid, open("m.jpg", mode="rb").read(), iteration.id)

# Alternatively, if the images were on disk in a folder called Images alongside the sample.py, then
# they can be added by using the following.
#
# Open the sample image and get back the prediction results.
# with open("Images\\test\\test_image.jpg", mode="rb") as test_data:
#     results = predictor.predict_image(project.id, test_data.read(), iteration.id)

# Display the results.
for prediction in results.predictions:
    print ("\t" + prediction.tag + ": {0:.2f}%".format(prediction.probability * 100))