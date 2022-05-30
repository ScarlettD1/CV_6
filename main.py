from tkinter import *
import cv2 as cv2
from PIL import Image, ImageTk, ImageEnhance
import numpy as np
from skimage import color


class App:
    def __init__(self):
        self.root = Tk()
        self.root['bg'] = "#fafafa"
        self.root.title('Lab 6 CV')
        self.root.geometry('1500x850')

        # создаем рабочую область
        self.frame = Frame(self.root)
        self.frame.grid()
        # pixelVirtual = PhotoImage(width=1, height=1)

        self.newImage = 0
        self.image = cv2.resize(cv2.imread("pictures/gggg.png"), (480, 640))
        cv2.imwrite('pictures/gog.png', self.image)
        # self.image = cv2.imread("pictures/gggg.png")

        # self.image = cv2.imread("pictures/witvh.jpg")
        # cv2.imshow("self.image", self.image)
        # cv2.waitKey(0)
        self.imageOrigin = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.imageOriginColored = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.readypic = Image.fromarray(self.imageOrigin)
        self.original_readypic = Image.fromarray(self.image)

        self.video = cv2.VideoCapture("video/Road.mp4")

        self.original_photo = ImageTk.PhotoImage(self.original_readypic)
        # Добавим метку 1
        self.photo = ImageTk.PhotoImage(self.readypic)

        # Добавим метку 2
        self.photo_2 = ImageTk.PhotoImage(self.readypic)

        # Добавим метку 3
        self.photo_3 = ImageTk.PhotoImage(self.readypic)

        # вставляем кнопки T1
        Button(self.frame, text="Вернуть", command=self.picture_origin).grid(row=0, column=0)

        # # вставляем кнопки T2
        Button(self.frame, text="Вернуть", command=self.picture_origin_2).grid(row=0, column=1)

        # вставляем кнопки T3
        Button(self.frame, text="Вернуть", command=self.picture_origin_3).grid(row=0, column=3, columnspan=2)

        # Buttons for video
        # Button(self.frame, text="watershed_video", command=self.watershed_video).grid(row=4, column=5, columnspan=2)

        # Добавим изображение T1
        self.canvas = Canvas(self.root, height=640, width=480)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=0)

        # Добавим изображение T2
        self.canvas_2 = Canvas(self.root, height=640, width=480)
        self.n_image = self.canvas_2.create_image(0, 0, anchor='nw', image=self.photo_2)
        self.canvas_2.grid(row=2, column=1)

        # Добавим изображение T3
        self.canvas_3 = Canvas(self.root, height=640, width=480)
        self.a_image = self.canvas_3.create_image(0, 0, anchor='nw', image=self.photo_3)
        self.canvas_3.grid(row=2, column=2)

        # # Добавим video
        # self.canvas_4 = Canvas(self.root, height=640, width=480)
        # self.a_image = self.canvas_4.create_image(0, 0, anchor='nw', image=self.photo_3)
        # self.canvas_4.grid(row=2, column=3)

        self.root.mainloop()

    # Функции для 1 картинки
    def picture_origin(self):
        self.newImage = 0
        self.image = cv2.imread('pictures/dora.jpg')
        # self.readypic = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY))
        self.readypic = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        self.photo = ImageTk.PhotoImage(self.readypic)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=0)

    def new_picture(self):
        self.newImage = Image.fromarray(self.newImage)
        self.photo = ImageTk.PhotoImage(self.newImage)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=0)

    # Функции для 2 картинки

    def picture_origin_2(self):
        self.newImage = 0
        self.image_2 = cv2.imread('pictures/money.JPEG')
        self.readypic_2 = Image.fromarray(cv2.cvtColor(self.image_2, cv2.COLOR_BGR2GRAY))
        # print("readypic_2:  ", self.readypic_2)
        self.photo_2 = ImageTk.PhotoImage(self.readypic_2)
        # print("photo_2:  ", self.photo_2)
        # cv2.imshow("self.photo_2", self.photo_2)
        self.n_image = self.canvas_2.create_image(0, 0, anchor='nw', image=self.photo_2)
        self.canvas_2.grid(row=2, column=1)

    def new_picture_2(self):
        self.newImage = Image.fromarray(self.newImage)
        self.photo_2 = ImageTk.PhotoImage(self.newImage)
        self.n_image = self.canvas_2.create_image(0, 0, anchor='nw', image=self.photo_2)
        self.canvas_2.grid(row=2, column=1)

    # Функции для 3 картинки
    def picture_origin_3(self):
        self.newImage = 0
        self.image_3 = cv2.imread('pictures/money.JPEG')
        self.readypic_3 = Image.fromarray(cv2.cvtColor(self.image_3, cv2.COLOR_BGR2GRAY))
        self.photo_3 = ImageTk.PhotoImage(self.readypic_3)
        self.a_image = self.canvas_3.create_image(0, 0, anchor='nw', image=self.photo_3)
        self.canvas_3.grid(row=2, column=2)

    def new_picture_3(self):
        self.newImage = Image.fromarray(self.newImage)
        self.photo_3 = ImageTk.PhotoImage(self.newImage)
        self.a_image = self.canvas_3.create_image(0, 0, anchor='nw', image=self.photo_3)
        self.canvas_3.grid(row=2, column=2)

    # Функции для видео
    def watershed_v(self, img):
        origin = img

        gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # cv2.imshow("thresh", thresh)
        # cv2.waitKey(0)

        # noise removal
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        # cv2.imshow("opening", opening)
        # cv2.waitKey(0)
        # sure background area
        sure_bg = cv2.dilate(opening, kernel, iterations=3)
        # cv2.imshow("sure_bg", sure_bg)
        # cv2.waitKey(0)
        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        # cv2.imshow("dist_transform", dist_transform)
        # cv2.waitKey(0)
        ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
        # cv2.imshow("sure_fg", sure_fg)
        # cv2.waitKey(0)
        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg, sure_fg)

        # Marker labelling
        ret, markers = cv2.connectedComponents(sure_fg)
        # Add one to all labels so that sure background is not 0, but 1
        markers = markers + 1
        # Now, mark the region of unknown with zero
        markers[unknown == 255] = 0
        # cv2.imshow("markers", markers)
        # cv2.waitKey(0)
        markers = cv2.watershed(origin, markers)
        result = (color.label2rgb(markers, bg_label=0) * 255).astype(np.uint8)
        # cv2.imshow("result", result)
        # cv2.waitKey(0)

        # self.newImage = origin
        return result

    def watershed_video(self):
        self.video = cv2.VideoCapture("video/Road.mp4")
        while True:
            succes, img = self.video.read()
            if succes == False:
                break
            img_new = self.watershed_v(img)
            cv2.imshow("Results", img_new)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.video.release()
        cv2.destroyWindow("Results")


app = App()