import cv2

img = cv2.imread("unknown.jpeg")

with open("my-file.txt", "a") as f:
  for row in img:
    for pixel in row:
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      sum = int(r) + int(g) + int(b)
      
      if sum == 765:
        print(" ", end="")
        f.write("#")
      elif sum >= 700 and sum <= 764:
        print(".", end="")
        f.write(".")
      elif sum >= 600 and sum <= 700:
        print("-", end="")
        f.write("-")
      elif sum >= 500 and sum <= 600:
        print("+", end="")
        f.write("+")
      elif sum >= 400 and sum <= 500:
        print("*", end="")
        f.write("*")
      elif sum >= 300 and sum <= 400:
        print("=", end="")
        f.write("=")
      elif sum >= 200 and sum <= 300:
        print("&", end="")
        f.write("&")
      elif sum >= 100 and sum <= 200:
        print("@", end="")
        f.write("@")
      elif sum >= 1 and sum <= 100:
        print("X", end="")
        f.write("X")
      elif sum == 0:
        print("#", end="")
        f.write("#")
    
    print()
    f.write("\n")
f.close()