import cv2

image = cv2.imread("solar-system.jpg")

cv2.putText(image,  
           "Sun",
           (80, 100),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=2,  
           color=(0,0,255)
           )

cv2.putText(image,  
           "Mercury",
           (115, 190),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )

cv2.putText(image,  
           "Venus",
           (190, 255),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )          

cv2.putText(image,  
           "Earth",
           (280, 170),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )  

cv2.putText(image,  
           "Mars",
           (380, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           ) 

cv2.putText(image,  
           "Jupiter",
           (570, 60),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           ) 

cv2.putText(image,  
           "Saturn",
           (750, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           ) 

cv2.putText(image,  
           "Uranus",
           (970, 140),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           ) 

cv2.putText(image,  
           "Neptune",
           (1110, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           ) 

cv2.imshow("Solar-systemWithName.jpg",image)

cv2.waitKey(0)