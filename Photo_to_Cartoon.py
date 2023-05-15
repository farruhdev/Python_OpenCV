import cv2

def cartoonize_image(img, ds_factor=4, sketch_mode=False):
    # 이미지를 축소합니다.
    img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_LINEAR)
    
    # 그레이 스케일 이미지를 얻습니다.
    img_gray = cv2.cvtColor(img_small, cv2.COLOR_RGB2GRAY)
    
    # 블러를 적용합니다.
    img_gray_blur = cv2.medianBlur(img_gray, 3)
    
    # 엣지 검출을 수행합니다.
    edges = cv2.Laplacian(img_gray_blur, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    
    # 컬러 이미지를 얻습니다.
    if sketch_mode:
        img_sketch = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        img_sketch = cv2.dilate(img_sketch, kernel, iterations=1)
        img_sketch = cv2.medianBlur(img_sketch, 5)
        img_edge = cv2.bitwise_not(cv2.cvtColor(img_sketch, cv2.COLOR_RGB2GRAY))
    else:
        img_edge = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    
    # 컬러 이미지와 엣지 이미지를 합칩니다.
    img_edge = cv2.resize(img_edge, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)
    img_cartoon = cv2.bitwise_and(img, img_edge)
    
    return img_cartoon


# 이미지 파일을 읽어옵니다.
img = cv2.imread("C:/rasim1.jpg")

# 만화 스타일로 변환합니다.
img_cartoon = cartoonize_image(img, ds_factor=4, sketch_mode=False)

# 결과 이미지를 출력합니다.
cv2.imshow('Cartoonized Image', img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
