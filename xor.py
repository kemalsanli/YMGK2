
import cv2
import numpy as np
 
demo = cv2.imread("koala.jpeg")
data = "01010100 01110010 10101110 01110001 10110000 01100001 01010010 10110001 10110011 10110011 10000000 01011100 01010010 01011100 11010011 00011000 10100100"
r, c, t = demo.shape

key = np.fromstring(data, dtype=np.uint8,count=3)

print(data)
 
encryption = cv2.bitwise_xor(demo, key) # encryption
decryption = cv2.bitwise_xor(encryption, key) # decryption
 
cv2.imshow("encryption", encryption) # Display ciphertext image
cv2.imshow("decryption", decryption) # Display the decrypted image
 
cv2.waitKey(-1)
cv2.destroyAllWindows()