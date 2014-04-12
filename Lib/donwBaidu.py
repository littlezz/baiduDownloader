#creat by zz
#2013-11-9

import urllib.request as rt

from bs4 import BeautifulSoup
import os.path as op
import re
import gzip
import io



def Dac(url):

  #  head={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
  #        'Accept-Encoding':'gzip'}
    
    base=url.split(r'/')[-1].replace('?','')
    
    #gzip
    req=rt.Request(url,headers=head)
   
    bi=io.BytesIO(rt.urlopen(req).read())
    u=gzip.GzipFile(fileobj=bi,mode='rb').read()
    
    u=BeautifulSoup(u,from_encoding='gb18030')
    #gzip
    ImgUrl=r'http://imgsrc.baidu.com/forum/pic/item/'
    no=0
    pt=re.compile(r'^(http://imgsrc.baidu.com/forum/).*?(\.jpg|\.png|\.gif|\.PNG)$')
   
    #TagA=u.find_all('img',pic_ext=True,src=pt)
    #TagA=u.find_all('img',src=pt)
    #for baidu outline
    TagA=u.find_all('img',{'class':'BDE_Image'})
    #
    tot=len(TagA)

    #

   
    
    for w in range(tot):
        
        i=TagA[w]
        #print(i.get('src'))
            
        no+=1
        #print('downloading...',no)
        filename=base+"_"+str(no)+'.jpg'
        print('downloading...',no)
        if op.exists(filename)and op.getsize(filename)>0:continue
        
        with open(filename,'wb') as f:
            #try:
            #Url=ImgUrl+i.get('src').split(r'/')[-1]
            # for outline
            Url=i.get('src')
            #
            #print(Url)
           
            r=rt.Request(Url,headers=head)
            f.write(rt.urlopen(r).read())
         #   print(i.get('href'))
            #except :
            #pass
        
        #rt.urlretrieve(i.get('href'),filename) 
         
                   
    print(base,'...ok')
    # next page
    it=u.find('a',text='下一页')
    if it :
        return it.get('href')
    else :return '0'
    
    
    
def anals(url):

    #gzip
    req=rt.Request(url,headers=head)
   
    bi=io.BytesIO(rt.urlopen(req).read())
    u=gzip.GzipFile(fileobj=bi,mode='rb').read()
    
    u=BeautifulSoup(u)
    #gzip

    
    #u=BeautifulSoup(rt.urlopen(url),from_encoding='gb18030')
    i=u.find("a",text="尾页")
    if i:
        try:
            return(int(i.get('href').split('=')[-1]))
        except:
            return 1

    else:return 1  
#Dac(input())
head={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
          'Accept-Encoding':'gzip'}
    
