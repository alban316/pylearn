#!/usr/bin/env python

class Door:
    def __init__(self):
        self._isopen = False
    
    def isOpen(self):
        return self._isopen
        
    def close(self):
        self._isopen = False
        
    def open(self):
        self._isopen = True
 
 
class FrontDoor(Door):
    def __init__(self):
        Door.__init__(self)
    
    def ringBell(self):
        print 'Who can it be now?'
        
        
def main():
    frontDoor = FrontDoor()
    frontDoor.open()
    if frontDoor.isOpen():
        print 'Door\'s open!'
    else:
        print 'The way is shut!'
        
    frontDoor.ringBell()
        
        
if __name__ == '__main__':
    main()
