import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np


src = r"C:\Users\lim98\PycharmProjects\face_recog\knn_examples\train\lee\1.jpg"

# Load the image
img = cv2.imread(src)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



# Define the function to update the image
def update_image(value):
    # 스크롤 막대의 현재 값을 가져옵니다
    r, g, b = r_var.get(), g_var.get(), b_var.get()

    # 원본 이미지의 복사본 만들기
    new_img = np.copy(img)

    # 스크롤 막대 값에 따라 이미지의 색상 채널 수정
    new_img[:,:,0] = np.multiply(new_img[:,:,0], r/255.0).astype(np.uint8)  # Red channel
    new_img[:,:,1] = np.multiply(new_img[:,:,1], g/255.0).astype(np.uint8)  # Green channel
    new_img[:,:,2] = np.multiply(new_img[:,:,2], b/255.0).astype(np.uint8)  # Blue channel

    # Numpy 배열을 PIL 이미지로 변환한 다음 Tkinter 사진 이미지로 변환
    tk_img = ImageTk.PhotoImage(Image.fromarray(new_img))

    # 캔버스 항목을 새 이미지로 업데이트
    canvas.itemconfig(image_item, image=tk_img)
    canvas.image = tk_img



# Create the GUI
root = tk.Tk()

# Create the scrollbars and labels
r_var = tk.IntVar()
r_scrollbar = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                       variable=r_var, label='Red', command=update_image)
r_scrollbar.pack(fill=tk.X)

g_var = tk.IntVar()
g_scrollbar = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                       variable=g_var, label='Green', command=update_image)
g_scrollbar.pack(fill=tk.X)

b_var = tk.IntVar()
b_scrollbar = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL,
                       variable=b_var, label='Blue', command=update_image)
b_scrollbar.pack(fill=tk.X)

# Create the canvas to display the image
canvas = tk.Canvas(root, width=img.shape[1], height=img.shape[0])
canvas.pack()
tk_img = ImageTk.PhotoImage(Image.fromarray(img))
image_item = canvas.create_image(0, 0, image=tk_img, anchor='nw')

# Start the event loop
root.mainloop()