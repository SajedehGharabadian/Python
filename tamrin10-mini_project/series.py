

from media_class import Media

class Series(Media):
    def __init__(self,t,n,dir,Im,u,dur,p,act,s=0):
        Media.__init__(self,t,n,dir,Im,u,dur,act)
        self.part = p
        self.season = s
