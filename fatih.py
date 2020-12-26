import cv2
import numpy as np
 
demo = cv2.imread("koala.jpeg")
r, c, t = demo.shape
key = np.random.randint(0, 256, size=(r, c, t ), dtype=np.uint8) # Generate random key image
a = "1 1 1 1 0 0 0 0 1 1 0 1 1 1 0 0 1 1 1 1 1 1 0 1"


#key2 = np.random.choice([1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1],size=(r, c)) # Generate random key image
#key2 = np.random.randint(0, 256, size=(r, c, t), dtype=np.uint8) 
#key2=np.dtype(np.uint8)
#all = np.frombuffer(key, dtype=np.uint8)

all = np.fromstring(a, dtype=np.uint8 , count=3)
#keyxor=key ^ key2
#keyxor = np.dtype(np.uint8)

def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    return matrix

print(all)
#print(keyxor)
#cv2.imshow("demo", demo) # show the original image
#cv2.imshow("key", key) # Display the key image
 
encryption = cv2.bitwise_xor(demo, all) # encryption
decryption = cv2.bitwise_xor(encryption, all) # decryption
 
cv2.imshow("encryption", encryption) # Display ciphertext image
cv2.imshow("decryption", decryption) # Display the decrypted image
 
cv2.waitKey(-1)
cv2.destroyAllWindows()