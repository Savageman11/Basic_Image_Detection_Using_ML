# %%

# importing new libraries for better prediction of the images.
from imageai.Prediction import ImagePrediction
import os

# Changing the execution path to the direcotry
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsDenseNet()
prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
prediction.loadModel()
predictions, probabilities = prediction.predictImage(
    os.path.join(execution_path, "giraffe.jpg"), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)

# %%
