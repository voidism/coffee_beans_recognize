from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry
from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint
from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

projectid = '############'
# Replace with a valid key
training_key = "###########"
prediction_key = "##################"
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
