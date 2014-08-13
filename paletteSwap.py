from PIL import Image
import datetime
import random
import copy

def paletteChange(src, dest, time):
	print "Start"
	imSrc = Image.open(src)
	imDest = Image.open(dest)
	pixSrc = imSrc.load()
	pixDest = imDest.load()
	(srcWidth, srcHeight) = imSrc.size
	(destWidth, destHeight) = imDest.size
	numPixels = destWidth * destHeight
	newImage = Image.new("RGB", (destWidth, destHeight))
	pixPallet = newImage.load()
	for i in xrange(numPixels):
		try:
			pixPallet[i % destWidth, i / destWidth] = pixSrc[i % srcWidth, i / srcWidth]
		except:
			red = random.randint(0,255)
			green = random.randint(0,255)
			blue = random.randint(0,255)
			pixPallet[i % destWidth, i / destWidth] = (red, green, blue)
	startTime = datetime.datetime.now()
	while (datetime.datetime.now() - startTime).total_seconds() < time:
		for x in xrange(destWidth):
			for y in xrange(destHeight):
				sPix = pixPallet[x,y]
				dPix = pixDest[x,y]
				curDelta = getDelta(sPix, dPix)
				newX = x
				newY = y
				for i in xrange(5):
					randX = random.randint(0, destWidth-1)
					randY = random.randint(0, destHeight-1)
					sPixRand = pixPallet[randX,randY]
					dPixRand = pixDest[randX, randY]
					delta = getDelta(sPixRand, dPix)
					if getDelta(sPix, dPixRand) + delta < curDelta + getDelta(sPixRand, dPixRand):
						curDelta = delta
						sPix = sPixRand
						newX = randX
						newY = randY
				pixPallet[newX, newY] = pixPallet[x,y]
				pixPallet[x,y] = sPix
	newFile = src.split(".")[0] + " to " + dest.split(".") + src.split(".")[1]
	newImage.save(newFile)
	check(src, newFile)
	print "Done"


def getDelta(color1, color2):
	luma = [0.299, 0.587, 0.144]
	diff = 0
	sum1 = 0
	sum2 = 0
	for i in xrange(len(color1)):
		sum1 += color1[i]*luma[i]
		sum2 += color2[i]*luma[i]
		d = (color1[i] - color2[i])*luma[i]
		diff += d*d
	rawDiff = sum1 - sum2
	return diff + rawDiff * rawDiff * 10

def check(palette, copy):
    palette = sorted(Image.open(palette).convert('RGB').getdata())
    copy = sorted(Image.open(copy).convert('RGB').getdata())
    print 'Success' if copy == palette else 'Failed'

paletteChange("Sunset.jpg","Ben Brancucci.jpg", 150)
