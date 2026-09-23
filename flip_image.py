import cv2
import matplotlib.pyplot as plt

def flip_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败，请检查路径！")
        return
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    flipped_img = cv2.flip(img_rgb, 1)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title("Flipped Image")
    plt.imshow(flipped_img)
    plt.axis('off')
    plt.show()
    return flipped_img

if __name__ == "__main__":
    flip_image('test.jpg')