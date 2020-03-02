# Color Seperator

![결과 이미지](./image/Result.png)


## Color Picker and Seperator
### 결과 설명
 1. 왼쪽 위 사진이 원본 데이터이고 필요한 범위를 color picker 창에서 지정.  
 2. 오른 쪽 위와 같이 원하는 색상이 추출.
 3. 왼쪽 아래는 추출된 mask 이미지.
 4. 오른쪽 아래는 추출된 hsv에서 h(색상) 채널의 범위를 나타내고 있음.
 
### 파일 설명
 - ColorPickerAndSeperator.sh
   - 두 개의 창이 나타나고 color picker 에서 색을 두 가지 선책함.
   - 선택하여 클릭하면 클릭 이벤트와 함께 화면에 결과나 나타남.
   - 이미지 변경 시 스크립트 안에서 경로 설정을 해 줘야 함.
   - Parameter
    - -p, --PICKERFILE : 색을 선택할 이미지
    - -l, --LOADFILE : 색을 추출할 target image
   
```bash 
bash ColorPickerAndSeperator.sh
```
    
### keyboard event
 * q : quit

## Color Seperator
 - 입력 폴더에 들어 있는 파일등을 정해진 범위 (lower ~ upper)의 색상 값을 추출하여 저장함.
    - lower과 upper 은 hsv 채널에서 H(Hue; 색조) 만을 사용함.
    - ColorSeperator.sh

```bash
python3 ColorSeperator.py \
    -i "입력 파일 경로" \
    -o "./output" \
    -u 100 \ # upper
    -l 10 \ #lower

```

# Color Seperator

![image of result](./image/Result.png)


## Color Picker and Seperator
### Explaination of result
 1. left up. a original image
 2. right up. a seperated image which you want color ranges.
 3. left down. a mask image.
 4. right down. color range which is choosed in h(hue) space.
 
### Explainatino of files
 - ColorPickerAndSeperator.sh
   - it is appeared two windows. and you have to choice two colors in color picker.
   - if you change the image, change a image path in script files. 
   - Parameter
    - -p, --PICKERFILE : image for color picker
    - -l, --LOADFILE : target image
   
```bash 
bash ColorPickerAndSeperator.sh
```
    
### keyboard event
 * q : quit

## Color Seperator
 - lower and upper values only use H(Hue) in hsv channel space.
 - ColorSeperator.sh

```bash
python3 ColorSeperator.py \
    -i "/your/path/input/image" \
    -o "./output" \
    -u 100 \ # upper color
    -l 10 \ #lower color

```



