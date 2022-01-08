import urge
import os
os.environ["YOUDAO_AI_KEY"] = "607a6dd02974695e"
os.environ["YOUDAO_AI_SECRET"] = "bvyx347AUiKlMQRgReK80oZKWH7oXZmZ"
path = "C:\\Users\\LR\\Nutstore\\1\\Python\\word\\1.jpg"
result = urge.easy_ocr(path).once()
for i in result:
    translates = urge.translate(i).once()
    print(translates)
    