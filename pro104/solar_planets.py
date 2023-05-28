import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))

cv2.putText(img,"Mercurio", (110,190), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

cv2.putText(img,"Venus", (190,270), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0))

cv2.putText(img,"Terra", (280,270), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0))

cv2.putText(img,"Marte", (360,180), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0))

cv2.putText(img,"Jupiter", (500,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0))

cv2.putText(img,"Saturno", (780,150), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))

cv2.putText(img,"Uranus", (950,300), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))

cv2.putText(img,"Netuno", (1090,150), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))

cv2.imshow("resultado",img)
           
cv2.imwrite("sistemaSolarComNome.jpg",img)

cv2.waitKey(0)