import os
import random
import shutil

img_dir = "dataset/images"
label_dir = "dataset/labels"

train_img = "dataset/images/train"
val_img = "dataset/images/val"

train_lbl = "dataset/labels/train"
val_lbl = "dataset/labels/val"

os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)
os.makedirs(train_lbl, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

images = []

for file in os.listdir(img_dir):
    if file.lower().endswith(".png"):
        images.append(file)

print("Found images:", len(images))

random.shuffle(images)

split_index = int(len(images) * 0.8)

train_files = images[:split_index]
val_files = images[split_index:]

for img in train_files:

    shutil.copy2(
        os.path.join(img_dir, img),
        os.path.join(train_img, img)
    )

    txt = img.replace(".png", ".txt")

    if os.path.exists(os.path.join(label_dir, txt)):
        shutil.copy2(
            os.path.join(label_dir, txt),
            os.path.join(train_lbl, txt)
        )

for img in val_files:

    shutil.copy2(
        os.path.join(img_dir, img),
        os.path.join(val_img, img)
    )

    txt = img.replace(".png", ".txt")

    if os.path.exists(os.path.join(label_dir, txt)):
        shutil.copy2(
            os.path.join(label_dir, txt),
            os.path.join(val_lbl, txt)
        )

print("Train Images:", len(train_files))
print("Val Images:", len(val_files))