"""ROV_1 controller."""


from controller import Robot, Motor, Keyboard
#from controller import Motor

robot = Robot()
timestep = 64

keyboard = robot.getKeyboard()
keyboard.enable(1000)

rm=robot.getMotor("right_motor")
rm.setPosition(float('inf'))
rm.setVelocity(0.0)

lm=robot.getMotor("left_motor")
lm.setPosition(float('inf'))
lm.setVelocity(0.0)

vrm=robot.getMotor("vertical_right_motor")
vrm.setPosition(float('inf'))
vrm.setVelocity(0.0)

vlm=robot.getMotor("vertical_left_motor")
vlm.setPosition(float('inf'))
vlm.setVelocity(0.0)

cam=robot.getCamera("camera")
cam.enable(60)

speed=0.5 #0.1
vertical_speed=0 #min 0.95
while robot.step(timestep) != -1:
    
    
    key = keyboard.getKey()
    if (key==Keyboard.UP):
        rm.setVelocity(speed + (vertical_speed*0.5))
        lm.setVelocity(-speed - (vertical_speed*0.5))
        print("Forward")
    elif (key==Keyboard.DOWN):
        rm.setVelocity(-speed -  (vertical_speed*0.5))
        lm.setVelocity(speed + (vertical_speed*0.5))
        print("Backward")
    elif (key==Keyboard.LEFT):
        vrm.setVelocity(vertical_speed*5)#both plus
        vlm.setVelocity(vertical_speed*5)
        
        rm.setVelocity(speed*0.3)
        lm.setVelocity(speed*0.3)
        
        print("Left Turn")
    elif (key==Keyboard.RIGHT):
        vrm.setVelocity(-vertical_speed*5)#both negative
        vlm.setVelocity(-vertical_speed*5)
        
        rm.setVelocity(-speed*0.3)
        lm.setVelocity(-speed*0.3)
        
        print("Right Turn")
    elif (key==ord('S')):
        #vrm.setVelocity(vertical_speed)
        #vlm.setVelocity(-vertical_speed)
        vertical_speed=1 #min 0.95
        print("down")
    elif (key==ord('W')):
        vertical_speed=0
        print("down")
    else:
        rm.setVelocity(0)
        lm.setVelocity(0)
        vrm.setVelocity(vertical_speed)
        vlm.setVelocity(-vertical_speed)
        print("STOP")
    
    #vrm.setVelocity(vertical_speed)
    #vlm.setVelocity(-vertical_speed)
    #print(vertical_speed)
    pass

# Enter here exit cleanup code.
