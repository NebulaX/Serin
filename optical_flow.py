from SimpleCV import *

def movement_check(x = 0,y = 0,t=1):
    direction = ""
    directionX = ""
    if x > t:
        directionX = "Right"
    if x < -1*t:
        directionX = "Left"

    direction = directionX
    if direction is not "":
        return direction
    else:
        return "No Motion"

def main():
    scale_amount = (200,150)
    #d = Display(scale_amount)
    cam = Camera(0)
    prev = cam.getImage().scale(scale_amount[0],scale_amount[1])
    #redhue = prev.hueDistance(Color.RED).binarize(100).invert()
    #prev = prev - redhue
    #prev = prev.erode().erode()
    time.sleep(0.5)
    t = 0.5
    buffer = 1
    count = 0
    while True:
        current = cam.getImage()
        current = current.scale(scale_amount[0],scale_amount[1])
        #rhue = current.hueDistance(Color.RED).binarize(100).invert()
        #current = current - rhue
        #current = current.erode().erode()
        if( count < buffer ):
            count = count + 1
        else:
            fs = current.findMotion(prev, window=15, method="BM")
            lengthOfFs = len(fs)
            if fs:
                dx = 0
                dy = 0
                for f in fs:
                    dx = dx + f.dx
                    dy = dy + f.dy

                dx = (dx / lengthOfFs)
                dy = (dy / lengthOfFs)
                motionStr = movement_check(dx,dy,t)
                print motionStr

        prev = current
        time.sleep(0.01)
        #current.save(d)

if __name__ == '__main__':
    main()
