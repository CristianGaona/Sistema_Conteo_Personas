import numpy as np
import cv2
import datetime
import time


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


def video1():
   try:
    log = open('Store/video1.txt', "w")
   except:
    print("No se puede abrir el archivo log")
   cap = cv2.VideoCapture('Videos/video1.mp4')
   print(cap)

   fgbg = cv2.createBackgroundSubtractorMOG2()

   detects = []

   #Separación de lineas
   posL = 165  # 165 165
   offset = 20  # 20 50

   xy1 = (5, posL)  # 10 5
   xy2 = (600, posL)  # 400 600

   total = 0

   final = 0

   up = 0
   down = 0
   while 1:
       ret, frame = cap.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

       fgmask = fgbg.apply(gray)

       retval, th = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

       kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))  # 4 4

       opening = cv2.morphologyEx(
           th, cv2.MORPH_OPEN, kernel, iterations=2)  # 2

       dilation = cv2.dilate(opening, kernel, iterations=1)  # 1

       closing = cv2.morphologyEx(
           dilation, cv2.MORPH_CLOSE, kernel, iterations=1)  # 1
       cv2.imshow("closing", closing)

       cv2.line(frame, xy1, xy2, (0, 0, 0), 3)

       cv2.line(frame, (xy1[0], posL-offset),
                (xy2[0], posL-offset), (255, 255, 0), 2)

       cv2.line(frame, (xy1[0], posL+offset),
                (xy2[0], posL+offset), (255, 255, 0), 2)

       contours, hierarchy = cv2.findContours(
           dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       i = 0
       for cnt in contours:
           (x, y, w, h) = cv2.boundingRect(cnt)

           area = cv2.contourArea(cnt)

           if int(area) > 2100:  # 3000 #2700
               centro = center(x, y, w, h)

               cv2.putText(frame, str(i), (x+5, y+15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
               cv2.circle(frame, centro, 4, (0, 0, 255), -1)
               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
               if len(detects) <= i:
                   detects.append([])
               if centro[1] > posL-offset and centro[1] < posL+offset:
                   detects[i].append(centro)
               else:
                   detects[i].clear()
               i += 1

       if i == 0:
           detects.clear()

       i = 0

       if len(contours) == 0:
           detects.clear()

       else:

          for detect in detects:
              for (c, l) in enumerate(detect):

                   if detect[c-1][1] < posL and l[1] > posL:
                       detect.clear()
                       up += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 255, 0), 5)
                       continue
               # log.write(str(up)+' Persona Subiendo' + time.strftime("%c") + '\n')

                   if detect[c-1][1] > posL and l[1] < posL:
                       detect.clear()
                       down += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 0, 255), 5)
                       continue
               # log.write(str(down)+' Persona bajando' + time.strftime("%c") + '\n')

                   if c > 0:
                       cv2.line(frame, detect[c-1], l, (0, 0, 255), 1)
       log.write('Suben' + str(up)+' Persona Subiendo' +
                 time.strftime("%c") + '\n')
       log.write('Bajan' + str(down)+' Persona bajando' +
                 time.strftime("%c") + '\n')
       log.write('Total' + str(total)+' Persona total' +
                 time.strftime("%c") + '\n')
       cv2.putText(frame, "TOTAL: "+str(total), (10, 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

       cv2.putText(frame, "SUBEN: "+str(up), (10, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       cv2.putText(frame, "BAJAN: "+str(down), (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
       cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

       cv2.imshow("IA Avanzada Luis - Cristian", frame)

       if cv2.waitKey(30) & 0xFF == ord('q'):
          break
       #print(total)

   cap.release()

   cv2.destroyAllWindows()

 #  return a


def video2():
   try:
    log = open('Store/video2.txt', "w")
   except:
    print("No se puede abrir el archivo log")
   cap = cv2.VideoCapture('Videos/video2.mp4')
   print(cap)

   fgbg = cv2.createBackgroundSubtractorMOG2()

   detects = []

   #Separación de lineas
   posL = 165  # 165 165
   offset = 20  # 20 50

   xy1 = (5, posL)  # 10 5
   xy2 = (600, posL)  # 400 600

   total = 0

   final = 0

   up = 0
   down = 0
   while 1:
       ret, frame = cap.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

       fgmask = fgbg.apply(gray)

       retval, th = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

       kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 4 4

       opening = cv2.morphologyEx(
           th, cv2.MORPH_OPEN, kernel, iterations=2)  # 2

       dilation = cv2.dilate(opening, kernel, iterations=4)  # 1

       closing = cv2.morphologyEx(
           dilation, cv2.MORPH_CLOSE, kernel, iterations=12)  # 1
       cv2.imshow("closing", closing)

       cv2.line(frame, xy1, xy2, (0, 0, 0), 3)

       cv2.line(frame, (xy1[0], posL-offset),
                (xy2[0], posL-offset), (255, 255, 0), 2)

       cv2.line(frame, (xy1[0], posL+offset),
                (xy2[0], posL+offset), (255, 255, 0), 2)

       contours, hierarchy = cv2.findContours(
           dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       i = 0
       for cnt in contours:
           (x, y, w, h) = cv2.boundingRect(cnt)

           area = cv2.contourArea(cnt)

           if int(area) > 3150:  # 3000 #2700
               centro = center(x, y, w, h)

               cv2.putText(frame, str(i), (x+5, y+15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
               cv2.circle(frame, centro, 4, (0, 0, 255), -1)
               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
               if len(detects) <= i:
                   detects.append([])
               if centro[1] > posL-offset and centro[1] < posL+offset:
                   detects[i].append(centro)
               else:
                   detects[i].clear()
               i += 1

       if i == 0:
           detects.clear()

       i = 0

       if len(contours) == 0:
           detects.clear()

       else:

          for detect in detects:
              for (c, l) in enumerate(detect):

                   if detect[c-1][1] < posL and l[1] > posL:
                       detect.clear()
                       up += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 255, 0), 5)
                       continue
               # log.write(str(up)+' Persona Subiendo' + time.strftime("%c") + '\n')

                   if detect[c-1][1] > posL and l[1] < posL:
                       detect.clear()
                       down += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 0, 255), 5)
                       continue
               # log.write(str(down)+' Persona bajando' + time.strftime("%c") + '\n')

                   if c > 0:
                       cv2.line(frame, detect[c-1], l, (0, 0, 255), 1)
       log.write('Suben' + str(up)+' Persona Subiendo' +
                 time.strftime("%c") + '\n')
       log.write('Bajan' + str(down)+' Persona bajando' +
                 time.strftime("%c") + '\n')
       log.write('Total' + str(total)+' Persona total' +
                 time.strftime("%c") + '\n')
       cv2.putText(frame, "TOTAL: "+str(total), (10, 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

       cv2.putText(frame, "SUBEN: "+str(up), (10, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       cv2.putText(frame, "BAJAN: "+str(down), (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
       cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

       cv2.imshow("IA Avanzada Luis - Cristian", frame)

       if cv2.waitKey(30) & 0xFF == ord('q'):
          break
       #print(total)

   cap.release()

   cv2.destroyAllWindows()


def video3():
   try:
    log = open('Store/video3.txt', "w")
   except:
    print("No se puede abrir el archivo log")
   cap = cv2.VideoCapture('Videos/video3.mp4')
   print(cap)

   fgbg = cv2.createBackgroundSubtractorMOG2()

   detects = []

   #Separación de lineas
   posL = 165  # 165 165
   offset = 50  # 20 50

   xy1 = (5, posL)  # 10 5
   xy2 = (600, posL)  # 400 600

   total = 0

   final = 0

   up = 0
   down = 0
   while 1:
       ret, frame = cap.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

       fgmask = fgbg.apply(gray)

       retval, th = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

       kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))  # 4 4

       opening = cv2.morphologyEx(
           th, cv2.MORPH_OPEN, kernel, iterations=2)  # 2

       dilation = cv2.dilate(opening, kernel, iterations=1)  # 1

       closing = cv2.morphologyEx(
           dilation, cv2.MORPH_CLOSE, kernel, iterations=1)  # 1
       cv2.imshow("closing", closing)

       cv2.line(frame, xy1, xy2, (0, 0, 0), 3)

       cv2.line(frame, (xy1[0], posL-offset),
                (xy2[0], posL-offset), (255, 255, 0), 2)

       cv2.line(frame, (xy1[0], posL+offset),
                (xy2[0], posL+offset), (255, 255, 0), 2)

       contours, hierarchy = cv2.findContours(
           dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       i = 0
       for cnt in contours:
           (x, y, w, h) = cv2.boundingRect(cnt)

           area = cv2.contourArea(cnt)

           if int(area) > 2700:  # 3000 #2700
               centro = center(x, y, w, h)

               cv2.putText(frame, str(i), (x+5, y+15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
               cv2.circle(frame, centro, 4, (0, 0, 255), -1)
               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
               if len(detects) <= i:
                   detects.append([])
               if centro[1] > posL-offset and centro[1] < posL+offset:
                   detects[i].append(centro)
               else:
                   detects[i].clear()
               i += 1

       if i == 0:
           detects.clear()

       i = 0

       if len(contours) == 0:
           detects.clear()

       else:

          for detect in detects:
              for (c, l) in enumerate(detect):

                   if detect[c-1][1] < posL and l[1] > posL:
                       detect.clear()
                       up += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 255, 0), 5)
                       continue
               # log.write(str(up)+' Persona Subiendo' + time.strftime("%c") + '\n')

                   if detect[c-1][1] > posL and l[1] < posL:
                       detect.clear()
                       down += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 0, 255), 5)
                       continue
               # log.write(str(down)+' Persona bajando' + time.strftime("%c") + '\n')

                   if c > 0:
                       cv2.line(frame, detect[c-1], l, (0, 0, 255), 1)
       log.write('Suben' + str(up)+' Persona Subiendo' +
                 time.strftime("%c") + '\n')
       log.write('Bajan' + str(down)+' Persona bajando' +
                 time.strftime("%c") + '\n')
       log.write('Total' + str(total)+' Persona total' +
                 time.strftime("%c") + '\n')
       cv2.putText(frame, "TOTAL: "+str(total), (10, 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

       cv2.putText(frame, "SUBEN: "+str(up), (10, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       cv2.putText(frame, "BAJAN: "+str(down), (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
       cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

       cv2.imshow("IA Avanzada Luis - Cristian", frame)

       if cv2.waitKey(30) & 0xFF == ord('q'):
          break
       #print(total)

   cap.release()

   cv2.destroyAllWindows()

  # return a


def video4():
   try:
    log = open('Store/video4.txt', "w")
   except:
    print("No se puede abrir el archivo log")
   cap = cv2.VideoCapture('Videos/video4.mp4')
   print(cap)

   fgbg = cv2.createBackgroundSubtractorMOG2()

   detects = []

   #Separación de lineas
   posL = 165  # 165 165
   offset = 40  # 20 50

   xy1 = (5, posL)  # 10 5
   xy2 = (600, posL)  # 400 600

   total = 0

   final = 0

   up = 0
   down = 0
   while 1:
       ret, frame = cap.read()

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

       fgmask = fgbg.apply(gray)

       retval, th = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

       kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))  # 4 4

       opening = cv2.morphologyEx(
           th, cv2.MORPH_OPEN, kernel, iterations=2)  # 2

       dilation = cv2.dilate(opening, kernel, iterations=1)  # 1

       closing = cv2.morphologyEx(
           dilation, cv2.MORPH_CLOSE, kernel, iterations=1)  # 1
       cv2.imshow("closing", closing)

       cv2.line(frame, xy1, xy2, (0, 0, 0), 3)

       cv2.line(frame, (xy1[0], posL-offset),
                (xy2[0], posL-offset), (255, 255, 0), 2)

       cv2.line(frame, (xy1[0], posL+offset),
                (xy2[0], posL+offset), (255, 255, 0), 2)

       contours, hierarchy = cv2.findContours(
           dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       i = 0
       for cnt in contours:
           (x, y, w, h) = cv2.boundingRect(cnt)

           area = cv2.contourArea(cnt)

           if int(area) > 2100:  # 3000 #2700
               centro = center(x, y, w, h)

               cv2.putText(frame, str(i), (x+5, y+15),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
               cv2.circle(frame, centro, 4, (0, 0, 255), -1)
               cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
               if len(detects) <= i:
                   detects.append([])
               if centro[1] > posL-offset and centro[1] < posL+offset:
                   detects[i].append(centro)
               else:
                   detects[i].clear()
               i += 1

       if i == 0:
           detects.clear()

       i = 0

       if len(contours) == 0:
           detects.clear()

       else:

          for detect in detects:
              for (c, l) in enumerate(detect):

                   if detect[c-1][1] < posL and l[1] > posL:
                       detect.clear()
                       up += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 255, 0), 5)
                       continue
               # log.write(str(up)+' Persona Subiendo' + time.strftime("%c") + '\n')

                   if detect[c-1][1] > posL and l[1] < posL:
                       detect.clear()
                       down += 1
                       total += 1
                       cv2.line(frame, xy1, xy2, (0, 0, 255), 5)
                       continue
               # log.write(str(down)+' Persona bajando' + time.strftime("%c") + '\n')

                   if c > 0:
                       cv2.line(frame, detect[c-1], l, (0, 0, 255), 1)
       log.write('Suben' + str(up)+' Persona Subiendo' +
                 time.strftime("%c") + '\n')
       log.write('Bajan' + str(down)+' Persona bajando' +
                 time.strftime("%c") + '\n')
       log.write('Total' + str(total)+' Persona total' +
                 time.strftime("%c") + '\n')
       cv2.putText(frame, "TOTAL: "+str(total), (10, 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

       cv2.putText(frame, "SUBEN: "+str(up), (10, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
       cv2.putText(frame, "BAJAN: "+str(down), (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
       cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

       cv2.imshow("IA Avanzada Luis - Cristian", frame)

       if cv2.waitKey(30) & 0xFF == ord('q'):
          break
       #print(total)

   cap.release()

   cv2.destroyAllWindows()

   #return a


def default():
   return "Opcion Invalida"


def switch(case):
   sw = {
       1: video1(),
       2: video2(),
       3: video3(),
       4: video4(),
   }
   return sw.get(case, default())


def menu():
   print("----------- Vídeos de prueba -----------")
   print("1. Prueba video 1")
   print("2. Prueba video 2")
   print("3. Prueba video 3")
   print("4. Prueba video 4")
   print("-----------------------------------")


#a = int(input("Valor de a: "))
#b = int(input("Valor de b: "))
menu()
case = int(input("Seleccione una opcion: "))
#print(switch(case, a, b))
#print(switch(case))
if case is 1:
    video1()
elif case is 2:
    video2()
elif case is 3:
    video3()
elif case is 4:
    video4()
else:
    print("Opcion Invalida")
