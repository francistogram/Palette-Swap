from PIL import Image
import datetime
import random
import os
import copy

def paletteChange(src, dest, time):
	if os.sep in src:
		srcSplit = src.split(os.sep)
		srcName = srcSplit[len(srcSplit) - 1]
	else:
		srcName = src
	if os.sep in dest:
		destSplit = dest.split(os.sep)
		destName = destSplit[len(destSplit) - 1]
	else:
		destname = dest
	print "Converting " + srcName + " to " + destName
	imSrc = Image.open(src)
	imDest = Image.open(dest)
	pixSrc = imSrc.load()
	pixDest = imDest.load()
	(srcWidth, srcHeight) = imSrc.size
	(destWidth, destHeight) = imDest.size
	numPixels = destWidth * destHeight
	newImage = Image.new("RGB", (destWidth, destHeight))
	pixPallet = newImage.load()
	reusedPixels = False
	srcPixels = srcWidth * srcHeight
	
	# Copies the pixels from the source to a new image that has the same
	# dimensions as the destination image
	for i in xrange(numPixels):
		# If there are more pixels in the target image then we iterate through
		# the source image again
		if i >= srcPixels:
			reusedPixels = True
			i = i % srcPixels 
		pixPallet[i % destWidth, i / destWidth] = pixSrc[i % srcWidth, i / srcWidth]
	startTime = datetime.datetime.now()

	# Run the algorithm for the alloted amount of time
	while (datetime.datetime.now() - startTime).total_seconds() < time:
		print "Time Left: " + str(time - ((datetime.datetime.now() - startTime).total_seconds()))
		
		# For each pixel in the created image we check it against 5 random 
		# pixels and out of those 6 pixels if switching it makes it closer to
		# the original image then we swap them
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

	# Creates the new image file
	newFile = srcName.split(".")[0] + " to " + destName.split(".")[0] + "." + srcName.split(".")[1]
	print newFile
	newImage.save("Created" + os.sep + newFile)
	if not reusedPixels:
		check(src, "Created" + os.sep + newFile)
	else:
		print "Success"

# Gets the difference between two pixels using Luma weighting which weighs
# red, green, and blue differently based on brightness since humans notice
# brightness differences much more than they notice color difference 
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

# Checks that the final result is actually the same pixels
def check(palette, copy):
    palette = sorted(Image.open(palette).convert('RGB').getdata())
    copy = sorted(Image.open(copy).convert('RGB').getdata())
    print 'Success' if copy == palette else 'Failed'

paletteChange("Original\\Chicago.jpg","Original\\New York.jpg", 150)
paletteChange("Original\\New York.jpg", "Original\\Chicago.jpg", 150)
