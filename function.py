# อ่านภาพ
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

# เปิดกล้องด้วย OpenCV
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

# เปิดวิดีโอด้วย OpenCV
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

# บันทึกวิดีโอด้วย OpenCV <.mp4>
def record_vi(name:str):
    import cv2
    cap = cv2.VideoCapture(0)
    # ต้องกำหนด FourCC
    # ? FourCC: กำหนดนามสกุลของไฟล์วิดีโอ
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # บันทึกวิดีโอ
    # VideoWriter(ชื่อไฟล์, FourCC, frame rate, ขนาดของวิดีโอ (x, y))
    out = cv2.VideoWriter(name +'.mp4', fourcc, 20.0, (640,480))
    while True:
        check, frame = cap.read()
        if check == True:
            cv2.imshow('Video', frame)
            # บันทึกแต่ละ frame ของกล้อง
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
    
    out.release()
    cap.release()
    cv2.destroyAllWindows()

# วาดเส้นตรง
def draw_line(path: str):
    import cv2
    img = cv2.imread(path)
    img_resize = cv2.resize(img, (700,700))
    # วาดเส้นตรง
    # line(ภาพ, start (x, y), stop (x, y), สี (BGR), ความหนา)
    #cv2.line(img_resize, (0, 248), (700, 248), (255, 0, 0), 10)
    cv2.line(img_resize, (0, 629), (700, 629), (255, 0, 0), 10)
    # วาดลูกศร
    # arrowedLine(ภาพ, start (x, y), stop (x, y), สี (BGR), ความหนา)
    cv2.arrowedLine(img_resize, (500,100), (500, 270), (0, 0, 255), 5)
    cv2.imshow('Line', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# วาดสี่เหลี่ยม
def draw_squ(path: str):
    import cv2
    img = cv2.imread(path)
    img_resize = cv2.resize(img, (700, 700))
    # วาดสี่เหลี่ยม
    # rectangle(ภาพ, มุมบนซ้าย (x, y), มุมล่างขวา (x, y), สี (BGR), ความหนา)
    # ? ความหนา = -1 ทำให้กลายเป็นสี่เหลี่ยมทึบ
    cv2.rectangle(img_resize, (0, 248), (700, 629), (0, 0, 255), 10)
    cv2.imshow('Rectangle', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# วาดวงกลม
def draw_cir(path: str):
    import cv2
    img = cv2.imread(path)
    img_resize = cv2.resize(img, (700, 700))
    # วาดวงกลม
    # circle(ภาพ, position of center (x, y), radis, สี (BGR), ความหนา)
    cv2.circle(img_resize, (480, 380), 180, (0, 100, 255), 10)
    cv2.imshow('Circle', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

# เขียนข้อความบนภาพ
def write_text(path: str):
    import cv2
    img = cv2.imread(path)
    img_resize = cv2.resize(img, (700, 700))
    # เขียนข้อความ
    # putText(ภาพ, text, position (x,y), font, size of text, สี (BGR), ความหนา)
    cv2.putText(img_resize, 'Cat', (440, 130), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), cv2.LINE_8)
    cv2.arrowedLine(img_resize, (500,150), (500, 270), (255, 0, 255), 5)
    cv2.imshow('Text', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
