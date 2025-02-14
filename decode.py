
import cv2
import os

d = {}
c = {}


for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)

x = cv2.imread("encrypted_img.png") 

if x is None:
    print("Error: Encrypted image not found.")
    exit()

with open("data.sys", "r") as f:
    key = f.readline().strip()
    l = int(f.readline().strip())


key1 = input("\nEnter key to extract text --> ")
decrypt = ""

if key == key1:
    kl = 0
    z = 0  
    n, m = 0, 0  
    for i in range(l):
        decrypt = decrypt + c[x[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    print("Encrypted text was:", decrypt)
else:
    print("Key doesn't match.")