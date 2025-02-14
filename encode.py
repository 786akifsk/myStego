import cv2
import string
import os

d = {}
c = {}


for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)

x = cv2.imread("mypic.jpg")


if x is None:
    print("Error: Image file not found or unable to load.")
    exit()


text = input("Enter text to hide: ")
key = input("Enter key to edit (Security Key): ")

l = len(text)
z = 0  
n, m = 0, 0  

for i in range(l):
    x[n, m, z] = d[text[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encrypted_img.png", x) 


print("Data Hiding in Image completed successfully.")


with open("data.sys", "w") as f:
    f.write(f"{key}\n{l}") 
