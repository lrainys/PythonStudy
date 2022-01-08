import cv2
cap = cv2.VideoCapture(r"1.mp4")
num = 1
while 1:
    # 逐帧读取视频  按顺序保存到本地文件夹
    ret,frame = cap.read()
    if ret:
        cv2.imwrite(f".\pictures\img_{num}.jpg",frame)   
    else:
        break
cap.release() 