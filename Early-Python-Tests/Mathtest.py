
from PIL import Image
import math
from numpy import random

def convert2pixel(a):
    b = math.floor((a)*255)
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    return b

Colorlist = [[255,100,100],
             [100,255,255],
             [100,100,255],
             [200,200,50],
             [50,200,200],
             [200,50,200]]

sidelength = 400
extraInputs = [[.9,.4,.2],[.1,.6,.4],[.5,.4,.6],[.2,.1,.6,.1],[.1,.2,.3,.1],[.9,.8,.99]]
num_possibilities = len(extraInputs)
imglist = []
pixellist = []
possibilities = []
finalRolls = [[0]*sidelength for j in range(sidelength)]
img = Image.new('RGB',(sidelength,sidelength),color='white')
pixels = img.load()
for i in range(len(extraInputs)):
   imglist.append(Image.new('RGB',(sidelength,sidelength),color='white'))
   pixellist.append(imglist[i].load())
   possibilities.append([[0]*sidelength for j in range(sidelength)])


inputFactors=[1/sidelength,1/sidelength] #This code here is entirely just to pick how to scale the inputs from 0 to 1

for a in range(num_possibilities):
    for i in range(sidelength):    # for every col
        for j in range(sidelength):    # For every row
            inputValues=[]
            if a%2 == 0:
                inputValues.append(i*inputFactors[0])
            else:
                inputValues.append(-(i-sidelength)*inputFactors[0])
            if a%4 <=3 and a%4 >= 2:
                inputValues.append(j*inputFactors[1])
            else:
                inputValues.append(-(j-sidelength)*inputFactors[1])

            for k in extraInputs[a]:
                inputValues.append(k)
            outputValue = .5
            outputSum = 0
            for k in inputValues:
                if k == -1:
                    continue
                elif k == 0:
                    if outputValue != 1:
                        outputValue = 0
                        break
                elif k >= 1:
                    if outputValue !=0:
                        outputValue = 1
                        break
                else:
                    outputSum+=k
            possibilities[a][i][j] = (outputSum/(2+len(extraInputs[a])))
            outputValue = convert2pixel(possibilities[a][i][j])
            pixellist[a][i,j] = (outputValue,outputValue,outputValue)
    imglist[a].show()



#for i in range(img2.size[0]):    # for every col
 #   for j in range(img2.size[1]):    # For every row
  #      inputValues2 = [i*inputFactors[0],j*inputFactors[1]]
   #     for k in extraInputs2:
    #        inputValues2.append(k)
     #   outputValue = .5
      #  outputSum = 0
       # for k in inputValues2:
        #    if k == -1:
         #       continue
          #  elif k == 0:
           #     if outputValue != 1:
            #        outputValue = 0
             #   break
#            elif k >= 1:
 #               if outputValue !=0:
  #                  outputValue = 1
   #             break
    #        else:
     #           outputSum+=k
      #  possibility2[i][j] = (outputSum/(2+len(extraInputs2)))
       # outputValue = convert2pixel(possibility2[i][j])
        #pixels[i,j] = (outputValue,outputValue,outputValue)

#img2.show()

finalImage = Image.new('RGB',(sidelength,sidelength),color='white')
finalpixels = finalImage.load()
finalscalefactor = 255//(1+num_possibilities)

for i in range(sidelength):
    for j in range(sidelength):
        chosenRoll=0
        chosenAnswer = -1
        for a in range(num_possibilities):
            roll = (random.rand()*possibilities[a][i][j])
            if roll > chosenRoll:
                chosenRoll = roll
                chosenAnswer = a
        finalRolls[i][j] = chosenAnswer
        finalpixels[i,j] = (Colorlist[chosenAnswer][0],Colorlist[chosenAnswer][1],Colorlist[chosenAnswer][2])
        
finalImage.show()
print(finalRolls)




