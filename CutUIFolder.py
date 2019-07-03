
import cv2
import numpy as np
import random

class CutUI:

    def __init__(self, color_table_image_path):
        self.window = "Color Seperator"
        self.color_picker_window = "Color Picker"
        self.point = []
        self.seed_overlay = None
        self.image_sum = None
        self.color_picker_image = cv2.imread(color_table_image_path)
        self.lower = (100, 200, 200)
        self.upper = (140, 255, 255)
        self.is_first = True

    def load_image(self, filename):
        self.image = cv2.imread(filename)
        self.display_image = np.array(self.color_picker_image)
        self.seed_overlay = np.zeros_like(self.color_picker_image)
        self.add_point(random.randint(0, self.color_picker_image.shape[1]),
                       random.randint(0, self.color_picker_image.shape[0]))
        self.add_point(random.randint(0, self.color_picker_image.shape[1]),
                       random.randint(0, self.color_picker_image.shape[0]))

    def run(self):
        cv2.namedWindow(self.color_picker_window)
        cv2.setMouseCallback(self.color_picker_window, self.mouse_clicked)

        while 1:
            # self.seed_overlay = np.zeros_like(self.color_picker_image)
            if self.is_first:
                self.render_image()
                print("self.lower : " + str(self.lower))
                print("self.upper : " + str(self.upper))
                self.is_first = False

            # self.lower = (100, 200, 200)
            # self.upper = (140, 255, 255)

            # cv2.imshow(self.window, display)
            cv2.imshow(self.color_picker_window, self.display_result)
            cv2.imshow(self.window, cv2.resize(self.image_sum, (int(self.image_sum.shape[1]/2), int(self.image_sum.shape[0]/2))))
        
            key = cv2.waitKey(20) & 0xFF
            if key == 27 or key == ord('q'):
                break
            # elif key == ord('n'):
            # elif key == ord('r'):
            # elif key == ord('c'):

        cv2.destroyAllWindows()

    def render_image(self):
        self.seed_overlay = np.zeros_like(self.color_picker_image)
        for x, y in self.point:
            cv2.rectangle(self.seed_overlay, (x - 1, y - 1), (x + 1, y + 1), (0, 0, 255), -1)
        self.display_result = cv2.addWeighted(self.display_image, 0.9, self.seed_overlay, 0.4, 0.1)

        self.lower = tuple(self.color_picker_image[self.point[0][1]][self.point[0][0]])
        self.upper = tuple(self.color_picker_image[self.point[1][1]][self.point[1][0]])
        self.lower = (int(self.lower[0]), int(self.lower[1]), int(self.lower[2]))
        self.upper = (int(self.upper[0]), int(self.upper[1]), int(self.upper[2]))

        print("rgb lower : " + str(self.lower))
        print("rgb upper : " + str(self.upper))
        lower_hsv = cv2.cvtColor(np.reshape(self.lower, [1, 1, 3]).astype(np.uint8), cv2.COLOR_RGB2HSV)
        upper_hsv = cv2.cvtColor(np.reshape(self.upper, [1, 1, 3]).astype(np.uint8), cv2.COLOR_RGB2HSV)
        self.lower = lower_hsv[0][0]
        self.upper = upper_hsv[0][0]
        print("hsv lower : " + str(self.lower))
        print("hsv upper : " + str(self.upper))

        # BGR to HSV 변환
        img_hsv = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(img_hsv)
        # 색상 범위를 제한하여 mask 생성
        img_mask = cv2.inRange(h, int(self.lower[0]), int(self.upper[0]))
        # 원본 이미지를 가지고 Object 추출 이미지로 생성
        img_result = cv2.bitwise_and(self.image, self.image, mask=img_mask)
        # 결과 이미지 생성
        img_mask = cv2.cvtColor(img_mask, cv2.COLOR_GRAY2BGR)

        # color space
        img_variation = np.zeros_like(self.image)
        h, w, c = img_variation.shape
        x = 0
        split_num = 10
        for idx in range(split_num):
            color = self.lower[0] + int(abs(self.lower[0] - self.upper[0]) * idx / split_num)
            # print("color : " + str(color))
            color = np.array([[[color, 200, 200]]])
            color = cv2.cvtColor(color.astype(np.uint8), cv2.COLOR_HSV2RGB)
            color = color[0][0]
            cv2.rectangle(img_variation,
                          (x + idx * int(w / split_num), 0),
                          (x + (idx + 1) * int(w / split_num), h),
                          (int(color[0]), int(color[1]), int(color[2])), # (idx * (255 / split_num), 100, 100),
                          cv2.FILLED)

        image_sum1 = np.concatenate((self.image, img_result), axis=1)
        image_sum2 = np.concatenate((img_mask, img_variation), axis=1)
        self.image_sum = np.concatenate((image_sum1, image_sum2), axis=0)

    def mouse_clicked(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.add_point(x - 1, y - 1)
            self.render_image()

        # elif event == cv2.EVENT_LBUTTONUP:
        # elif event == cv2.EVENT_MOUSEMOVE:

    def add_point(self, x, y):
        self.point.append((x, y))
        if len(self.point) > 2:
            self.point.pop(0)

        print("point : " + str(self.point))

# import argparse

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(prog="Interactive Graph Cut",
    #                                  description="Interactively segment an image", add_help=True)
    # parser.add_argument('-i', '--INFILE', help='Input image file to segment.', required=True)
    # parser.add_argument('-o', '--OUTFILE', help='Used to save segmented images.', required=True)
    # args = parser.parse_args()

    # ui = CutUI(args.INFILE)
    ui = CutUI("/home/jamin/projects/Code/ColorSeperator/image/hsv_bar.png")
    ui.load_image("/home/jamin/projects/Code/ColorSeperator/image/cUTqm.png")
    ui.run()

# import Color
# import cv2
# import numpy as np

# a = Color.color_string_map["red"]
# b = np.reshape(a, [1, 1, 3]).astype(np.uint8)
#
# c = cv2.cvtColor(b, cv2.COLOR_RGB2HSV)
# image = cv2.imread("/home/jamin/projects/Code/ColorSeperator/image/hsv_bar.png")
# h, w, c = image.shape

# color = np.array([[[100, 100, 100]]])
# color = cv2.cvtColor(color.astype(np.uint8), cv2.COLOR_HSV2RGB)
# color = color[0][0]