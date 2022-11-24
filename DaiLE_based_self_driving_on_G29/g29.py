import threading
import pygame
import sys
from pygame.locals import JOYAXISMOTION, QUIT
class g29(object):

    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    def __init__(self):
        
        self.steer = 0.5
        self.throttle = 0
        self.brake = 0
        self.clutch = 0
     
        self.vjoy_const = 32768

        self._is_running = True

        self._monitor_thread = threading.Thread(
            target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
    
    def __del__(self):
        self.stop()
        pygame.quit()
        
    def stop(self):
        self._is_running = False
        self._monitor_thread.join()
        
        print('Gamepad monitor thread ended')
      
    def read(self):
        return [self.steer, self.throttle, self.brake]#, self.clutch]
        
    def _monitor_controller(self):

        while self._is_running:
           
            events = pygame.event.get()
 
            for event in events:
                
                if event.type == JOYAXISMOTION: 
                 
                    if event.axis == 0:                                             
                        self.steer = (event.value + 1 )/ 2 
                    
                    if event.axis == 1:
                            self.throttle = 1-(event.value + 1) /2

                    if event.axis == 2:
                            self.brake = 1 - (event.value + 1) /2
                            
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()        
    
if __name__ == '__main__':
    import pyvjoy
    j = pyvjoy.VJoyDevice(1)
    controller = g29()

    while True:   
        print(controller.read())
