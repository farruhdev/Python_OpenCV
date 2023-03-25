# Cartoon

## Installation

### Application tested on:

- python 3.7
- tensorflow 2.1.0 
- tf_slim 1.1.0
- ffmpeg 3.4.8
- Cuda version 10.1
- OS: Linux (Ubuntu 18.04)



    # 이미지를 축소합니다.
    
    # 그레이 스케일 이미지를 얻습니다.
    
    # 블러를 적용합니다.
    
    
    # 엣지 검출을 수행합니다.
    
    # 컬러 이미지를 얻습니다.
    
    
    # 컬러 이미지와 엣지 이미지를 합칩니다.
    

# 이미지 파일을 읽어옵니다.


# 만화 스타일로 변환합니다.

# 결과 이미지를 출력합니다.
cv2.imshow('Cartoonized Image', img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
