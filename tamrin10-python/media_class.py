
import pytube

class Media:
    
    def __init__(self,t,n,dir,Im,u,dur,act):
        self.type = t
        self.name = n
        self.director = dir
        self.score = Im
        self.url = u
        self.duration = dur
        self.actor = act

    def show_info(self):
        print("Type:",self.type , "Name:" , self.name ,"Director:",self.director,"Score:",self.score,"Url:",self.url,"Duration:",self.duration,"actors:",self.actor)

    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='test.mp4')


            


