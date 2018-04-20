import os
import csv
import sys
import numpy as np
import pandas as pan
from PIL import Image



def MakeCopyOfanImage(imagepath):
    im=Image.open(imagepath,'r')
    copied=im.copy()
    return copied,im

def saveImage(image): ## saving image
    image.save('mask.jpg')                         ##################################OUTPUT FILE

def makeImage(image2,probabilities):
    width, height = image2.size

    pix = image2.load()

    for i in range(width):
        for j in range(height):
            r, g, b = image2.getpixel((i, j))
            #row_num = (r * 256 * 256) + (g * 256) + b
            if (probabilities[r][g][b] < 0.00055):
                pix[i, j] = (255, 255, 255)
            else:
                pix[i, j] = (0, 0, 0)

                #

    # Return new image
    saveImage(image2)



def openDirectory():
    colorDIR=os.listdir('./image/')
    maskDIR=os.listdir('./mask/')
    return colorDIR,maskDIR

def openImageAndConvertToRGB(source):
    imageList = Image.open(source,'r')
    colorOpen = imageList.convert('RGB')
    colorImage = list(colorOpen.getdata())
    return colorImage

def check(maskImage):
        R=maskImage[0]
        G=maskImage[1]
        B=maskImage[2]
        if(R<120 and G<120 and B<120):
            return 0
        else:
            return 1

def readImage(whitecount,blackcount):
    totalBlack=0
    totalWhite=0
    colorDIR,maskDIR=openDirectory()
    for i in range(0,len(colorDIR),1):
        colorOpen = openImageAndConvertToRGB('./image//' + colorDIR[i])
        maskOpen = openImageAndConvertToRGB('./mask//' + maskDIR[i])

        for j in range(0,len(colorOpen),1):
            R=colorOpen[j][0]
            G=colorOpen[j][1]
            B=colorOpen[j][2]
            x=check(maskOpen[j])
            if(x==0):
                blackcount[R][G][B]+=1
                totalBlack+=1
            if(x==1):
                whitecount[R][G][B]+=1
                totalWhite+=1

    return totalBlack,totalWhite,whitecount , blackcount



def getProbability(tb,tw,probabilities,whitecount,blackcount):
    csvFormatted=[]
    totalPixel=tw/(tb+tw)
    for R in range(0,256,1):
        for G in range(0, 256, 1):
            for B in range(0, 256, 1):
                #if((blackcount[R][G][B]+whitecount[R][G][B])!=0):
                if(whitecount[R][G][B]>blackcount[R][G][B]):
                    #probabilities[R][G][B]=float(((whitecount[R][G][B])*totalPixel)/(blackcount[R][G][B]+whitecount[R][G][B]))
                    probabilities[R][G][B] =1
                    csvFormatted.append([R,G,B,probabilities[R][G][B]])
                else:
                    probabilities[R][G][B]=float(0)
                    csvFormatted.append([R, G, B, probabilities[R][G][B]])
    return csvFormatted,probabilities

def writeINCSV(csvFormatted):
    myFile = open('test2.csv', 'w', newline = '')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(["Red", "Green", "Blue", "Probability"])
        writer.writerows(csvFormatted)
    print('done')



def main():
    whitecount = np.zeros((256, 256, 256))
    blackcount = np.zeros((256, 256, 256))
    probabilities = np.zeros((256, 256, 256))
    tb,tw,whitecount,blackcount=readImage(whitecount,blackcount)
    csvFormatted,probabilities=getProbability(tb,tw,probabilities,whitecount,blackcount)
    imagePath = 'test5.jpg'                                 ####################################The file name which is input
    image2, actualImage = MakeCopyOfanImage(imagePath)
    makeImage(image2, probabilities)


    writeINCSV(csvFormatted)

    #whitecount,blackcount=measurePixels(allColorImage,allMaskImage,whitecount,blackcount)
    #probabilities=getProbability(whitecount,blackcount)
    #print(probabilities)

if __name__ == "__main__":
    main()