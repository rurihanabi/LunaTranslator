 
import re
import time
from urllib.parse import quote 
from translator.basetranslator import basetrans
import platform 
import ctypes
import re
import os
from utils.config import globalconfig
import subprocess

st=subprocess.STARTUPINFO()
st.dwFlags=subprocess.STARTF_USESHOWWINDOW
st.wShowWindow=subprocess.SW_HIDE

class TS(basetrans):
     
    def inittranslator(self ) :
        self.typename='jb7'
        self.path=os.path.join(globalconfig['fanyi']['jb7']['args']['路径'],'JBJCT.dll')
        if platform.architecture()[0]=='32bit':
            self._x64=False
            try:
                self.dll=  ctypes.CDLL(self.path)
            except:
                pass
        else:
            self._x64=True
            self.x64('おはおよう')
    def x64(self,content):
         
        ress=''
        for line in content.split('\n'):
            if len(line)==0:
                continue
            if ress!='':
                ress+='\n'

            p=subprocess.Popen(r'./files/jb7x64runner/win32dllforward.exe "'+self.path+'" '+line, stdout=subprocess.PIPE,startupinfo=st)
            ress+=str(p.stdout.readline(),encoding='GB2312',errors='ignore')
        ress=ress.replace('Translation(TaskNo = 1) is OK. (remainder threads = 0)\r\n','')
        return ress
    def x86(self,content):
        CODEPAGE_JA = 932
        CODEPAGE_GB = 936
        CODEPAGE_BIG5 = 950
        BUFFER_SIZE = 3000

            
        size = BUFFER_SIZE 
        out = ctypes.create_unicode_buffer(size) 
        buf = ctypes.create_unicode_buffer(size) 
        outsz = ctypes.c_int(size) 
        bufsz = ctypes.c_int(size) 
        try:
            self.dll.JC_Transfer_Unicode( 0, # int, unknown 
                CODEPAGE_JA    , # uint     from, supposed to be 0x3a4 (cp932) 
                CODEPAGE_GB, # uint to, eighter cp950 or cp932 
                1, # int, unknown 
                1, # int, unknown 
                content, #python 默认unicode 所有不用u'
                out, # wchar_t* 
                ctypes.byref(outsz), # ∫ 
                buf, # wchar_t* 
                ctypes.byref(bufsz)) # ∫ 
        except:
            pass
        return out.value
    def realfy(self,content): 
        if self._x64:
            return self.x64(content)
        else:
            return self.x86(content)
        
          