import flash

from flash import download_data
from flash.vision import ImageClassificationData, ImageClassifier


# 1. Download the data
download_data("https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip", 'data/')

# 2. Load the data
datamodule = ImageClassificationData.from_folders(
    backbone="resnet34",
    num_workers=8,
    train_folder="data/hymenoptera_data/train/",
    valid_folder="data/hymenoptera_data/val/",
    test_folder="data/hymenoptera_data/test/",
)

# 3. Build the model
model = ImageClassifier(num_classes=datamodule.num_classes, backbone="resnet18")

# 4. Create the trainer. Run once on data
trainer = flash.Trainer(max_epochs=4)

# 5. Finetune the model
trainer.finetune(model, datamodule=datamodule, strategy="freeze_unfreeze")

# 7. Save it!
trainer.save_checkpoint("image_classification_model.pt")
