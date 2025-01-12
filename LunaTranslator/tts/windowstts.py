    
from utils.config import globalconfig  
import subprocess
class tts():
    
    def __init__(self,showlist ): 
                
        st=subprocess.STARTUPINFO()
        st.dwFlags=subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow=subprocess.SW_HIDE

        p=subprocess.Popen('./files/tts/tts_l.exe',stdout=subprocess.PIPE,startupinfo=st)
        
        count=str(p.stdout.readline(),encoding='utf8')
        count=count.replace('\r','').replace('\n','')
        count=int(count)
        self.voicelist=[]
        for i in range(count):

             
            res=str(p.stdout.readline(),encoding='utf8').replace('\r','').replace('\n','')
            self.voicelist.append(res.split('\\')[-1]) 
        showlist.emit(self.voicelist)
        self.speaking=None
    def read(self,content,rate=1):
        print('reading',content)
        i=self.voicelist.index(globalconfig['windowstts']['voice'])
        if i==-1:
            return 
        if self.speaking:
            self.speaking.kill()
                
        st=subprocess.STARTUPINFO()
        st.dwFlags=subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow=subprocess.SW_HIDE

        self.speaking=subprocess.Popen(f'./files/tts/tts_s.exe {i} {globalconfig["windowstts"]["rate"]} {globalconfig["windowstts"]["volume"]} "{content}"',startupinfo=st )
        
      