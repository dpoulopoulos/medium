from flash import Trainer
from flash import download_data
from flash.vision import ImageClassificationData, ImageClassifier


# 1. Download the data
download_data("https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip", 'data/')

# 2. Load the model from a checkpoint
model = ImageClassifier.load_from_checkpoint("image_classification_model.pt")

# 3a. Predict what's on a few images! ants or bees?
predictions = model.predict([
    "data/hymenoptera_data/test/ants/8124241_36b290d372.jpg",
    "data/hymenoptera_data/test/ants/147542264_79506478c2.jpg",
    "data/hymenoptera_data/test/ants/212100470_b485e7b7b9.jpg",
])
print(predictions)

# 3b. Generate predictions with a whole folder
datamodule = ImageClassificationData.from_folder(folder="data/hymenoptera_data/test/ants/")
predictions = Trainer().predict(model, datamodule=datamodule)
print(predictions)
