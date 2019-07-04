# Color Seperator

![결과 이미지](./image/Result.png)

## 결과 설명
 1. 왼쪽 위 사진이 원본 데이터이고 필요한 범위를 color picker 창에서 지정.  
 2. 오른 쪽 위와 같이 원하는 색상이 추출.
 3. 왼쪽 아래는 추출된 mask 이미지.
 4. 오른쪽 아래는 추출된 hsv에서 h(색상) 채널의 범위를 나타내고 있음.
 
## 파일 설명
 * ColorPickerAndSeperator.sh
   * 두 개의 창이 나타나고 color picker 에서 색을 두 가지 선책함.
   * 선택하여 클릭하면 클릭 이벤트와 함께 화면에 결과나 나타남.
   * 이미지 변경 시 스크립트 안에서 경로 설정을 해 줘야 함.
   * Parameter
    * -p, --PICKERFILE : 색을 선택할 이미지
    * -l, --LOADFILE : 색을 추출할 target image
   
```bash 
ColorPickerAndSeperator.sh
```
    
## keyboard event
 * q : quit