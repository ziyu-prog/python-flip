import cv2
import matplotlib.pyplot as plt

def flip_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败，请检查路径！")
        return
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    flipped_img = cv2.flip(img_rgb, 1)   # 1 表示水平（左右）翻转
    plt.figure()
    plt.imshow(flipped_img)
    plt.axis('off')
    plt.show()
    return flipped_img

if __name__ == "__main__":
    flip_image('test.jpg')
