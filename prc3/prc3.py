# کتابخانه های لازم را بارگیری کنید
import os
import urllib.request
from PIL import Image
import torch
from torchvision import transforms, models
import locale  # ماژول locale را بارگیری کنید
import re

# مسیر پوشه تصاویر را تنظیم کنید
image_folder = "car"

# برچسب های کلاس ImageNet را دانلود کنید
url = "https://raw.githubusercontent.com/joe-papa/pytorch-book/main/files/imagenet_class_labels.txt"
fpath = 'imagenet_class_labels.txt'
urllib.request.urlretrieve(url, fpath)

# برچسب های کلاس ImageNet را بارگیری کنید
with open('imagenet_class_labels.txt') as f:
    classes = [line.strip() for line in f.readlines()]

# تبدیلات تصویر را تعریف کنید
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])])

# مدل AlexNet را با آرگومان صحیح بارگیری کنید
model = models.alexnet(weights=models.AlexNet_Weights.DEFAULT)

# تابع پیش‌بینی را تعریف کنید
def predict(img_path):
    # تصویر را بارگیری کنید
    img = Image.open(img_path)

    # تصویر را پیش پردازش کنید
    img_tensor = transform(img)

    # یک دسته با اندازه 1 ایجاد کنید
    batch = torch.unsqueeze(img_tensor, 0)

    # مدل را در حالت ارزیابی تنظیم کنید
    model.eval()

    # کلاس تصویر را پیش‌بینی کنید
    y = model(batch)

    # شاخص کلاس پیش‌بینی‌شده را برگردانید
    return torch.argmax(y, dim=1).item()

# مدل را روی تصاویر ماشین ارزیابی کنید
correct = 0
total = 0
for filename in os.listdir(image_folder):
    # مسیر تصویر را دریافت کنید
    img_path = os.path.join(image_folder, filename)

    # کلاس تصویر را پیش‌بینی کنید
    prediction = predict(img_path)

    # برچسب واقعی تصویر را دریافت کنید
    true_label = classes[prediction]

    # اگر پیش‌بینی صحیح بود، تعداد صحیح را افزایش دهید
    if re.search("car", true_label):
        correct += 1

    # تعداد کل را افزایش دهید
    total += 1

# دقت را محاسبه کنید
accuracy = (correct / total) * 100

# دقت را چاپ کنید
print(f"accuracy: {accuracy:.2f}%")
