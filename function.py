# อ่านภาพ
from importlib.resources import path
from tabnanny import check


def read_img(path: str):
    import cv2
    # อ่านภาพ
    img = cv2.imread(path)
    # เช็คมิติ
    print(img.ndim)
    # ปริ้น array ภาพ
    print(img)

# แสดงผลภาพ
def imshow_img(path: str):
    import cv2
    img = cv2.imread(path)
    # แสดงผลภาพ
    cv2.imshow('Output', img)
    # delay = เวลาที่ปิดภาพ หน่วย ms ถ้า delay = 0 จะเปิดค้างไว้
    cv2.waitKey(delay=0)
    # คืนทรัพย์กรให้เครื่อง
    cv2.destroyAllWindows()

# ปรับขนาดภาพ
def rescale_img(path: str):
    import cv2
    # imread(ภาพ, โหมด) 
    # ? โหมด 0 = ภาพเทา
    # ? โหมด 1 = ภาพสี
    img = cv2.imread(path, 0)
    # ปรับขนาดภาพ
    img_resize = cv2.resize(img, (400, 400))
    # แสดงผลภาพที่ปรับขนาดแล้ว
    cv2.imshow('Resize', img_resize)
    # แสดงผลภาพต้นแบบ
    #cv2.imshow('Og', img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

# ส่งออกภาพ
def export_img(path: str):
    import cv2
    img = cv2.imread(path, 0)
    img_resize = cv2.resize(img, (400, 400))
    # ส่งออกภาพ
    cv2.imwrite('Output.jpg', img_resize)
    cv2.imshow('Cat', img_resize)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

# เปิดกล้องด้วย opencv
def vi_cap():
    import cv2
    # อ่านวิดีโอจากกล้อง
    # ? 0 = กล้องตัวที่ 1
    # ? 1 = กล้องตัวที่ 2
    cap = cv2.VideoCapture(0)
    while True:
        # รับภาพจากกล้อง frame / frame
        # ? check เป็น bool อ่านค่าได้เป็น True ไม่ได้เป็น False
        # ? frame ภาพที่ได้จาก VideoCapture
        check , frame = cap.read()
        cv2.imshow('Camera', frame)
        
        # กดปุ่ม e เพื่อปิด
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
    # เคลียร์ RAM
    cap.release()
    cv2.destroyAllWindows()

# เปิดวิดีโอด้วย opencv
def read_vi(path: str):
    import cv2
    # อ่านวิดีโอจากไฟล์ mp4
    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        check, frame = cap.read()
        # check ว่ามี frame ให้อ่านอยู่รึเปล่า
        # ? ถ้า True แสดง Video
        # ? ถ้า False ก็ไม่แสดง Video / ปิด Video
        if check == True:
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        if check == False:
            break
    cap.release()
    cv2.destroyAllWindows()

# Video GrayScale Mode
def gray_vi(path: str):
    import cv2
    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        check, frame = cap.read()
        if check == True:
            # แปลงจากวิดีโอต้นแบบเป็น วิดีโอสีต่างๆ ในที่นี้เปลี่ยนเป็นสีเทา
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # แสดงวิดีโอ GrayScale
            cv2.imshow('Gray', gray)
            # แสดงวิดีโอต้นแบบ
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        if check == False:
            break
    cap.release()
    cv2.destroyAllWindows()