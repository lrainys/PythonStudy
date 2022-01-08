import urge
import os
os.environ["YOUDAO_AI_KEY"] = "607a6dd02974695e"
os.environ["YOUDAO_AI_SECRET"] = "bvyx347AUiKlMQRgReK80oZKWH7oXZmZ"
sentence = 'scissor'
words = sentence.split()
for w in words:
    result = urge.translate(w,full=True).once()
    print(w,result['simple_translation'][0])
    for i in result['wfs']:
        print(i)
