import cv2
import os
import numpy as np

def seperate_image_color(input_path, output_path, upper, lower):
    assert os.path.isdir(input_path)

    output_dir = output_path
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    result_mask = os.path.join(output_dir, 'mask')
    if not os.path.isdir(result_mask):
        os.mkdir(result_mask)
    result = os.path.join(output_dir, 'result')
    if not os.path.isdir(result):
        os.mkdir(result)

    image_list = os.listdir(input_path)
    
    for idx, name in enumerate(image_list):
        image_path = os.path.join(input_path, name)
        # 이미지 파일을 읽어온다
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
        # BGR to HSV 변환
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img_hsv)

        # h = np.array(h).astype(np.int32)

        # 색상 범위를 제한하여 mask 생성
        img_mask = cv2.inRange(h, 10, 100)
        # 원본 이미지를 가지고 Object 추출 이미지로 생성
        img_result = cv2.bitwise_and(img, img, mask=img_mask)
        # 결과 이미지 저장
        img_mask_gray = cv2.cvtColor(img_mask, cv2.COLOR_GRAY2BGR)
        cv2.imwrite(os.path.join(result_mask, name), img_mask_gray)
        cv2.imwrite(os.path.join(result, name), img_result)


import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Coloer Seperator",
                                     description="extract color parts", add_help=True)
    parser.add_argument('-i', '--INPUTDIR', help='target image diractory.', required=True)
    parser.add_argument('-o', '--OUTPUTDIR', help='output diractory', required=True)
    parser.add_argument('-u', '--UPPER', help='upper h(hsv) value.', required=True)
    parser.add_argument('-l', '--LOWER', help='lower h(hsv) value', required=True)
    args = parser.parse_args()

    seperate_image_color(args.INPUTDIR, args.OUTPUTDIR, args.UPPER, args.LOWER)
