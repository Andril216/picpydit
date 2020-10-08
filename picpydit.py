from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from PIL import Image,ImageEnhance,ImageFilter
import imageio
import os
from os import listdir
from os.path import isfile, join
import time
import sys
root=Tk()
root["bg"]="black"
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
fp=filedialog.askopenfilename()
try:
        a=imageio.get_reader(fp)
except:
        sys.exit()
ex=0
fj=1
fh=1
wn=1
wh=1
wo=0
oo=0
jo=0
vk=0
if(fp.split(".")[-1]=="gif" or fp.split(".")[-1]=="mp4" or fp.split(".")[-1]=="avi" or fp.split(".")[-1]=="ogg"):
        bkr=len(a)*1000/(a.get_meta_data()["duration"]*(len(a)-1))
else:
    bkr=0
def emb():
    global wo
    wo+=1
    if(wo==2):
        wo=0
def cont():
    global oo
    oo+=1
    if(oo==2):
        oo=0
def edg():
    global jo
    jo+=1
    if(jo==2):
        jo=0
def smt():
    global vk
    vk+=1
    if(vk==2):
        vk=0
def don():
    global fj
    global fh
    global wn
    global wh
    global ex
    global bkr
    ex+=1
    fj=s.get()
    fh=s1.get()
    wn=s2.get()
    wh=s3.get()
    bkr=s4.get()
    eof=root.winfo_children()
    for dx in eof:
                dx.destroy()

    

br=Label(root,text="Brightness")
br.place(x=0,y=30)
s=Scale(from_=0,to=20,orient="horizontal")
s.set(1)
s.place(x=100,y=0)
cr=Label(root,text="Colour")
cr.place(x=0,y=90)
s1=Scale(from_=-10,to=10,orient="horizontal")
s1.set(1)
s1.place(x=100,y=60)
co=Label(root,text="Contrast")
co.place(x=0,y=150)
s2=Scale(from_=-10,to=10,orient="horizontal")
s2.set(1)
s2.place(x=100,y=120)
sh=Label(root,text="Sharpness")
sh.place(x=0,y=210)
s3=Scale(from_=-10,to=10,orient="horizontal")
s3.set(1)
s3.place(x=100,y=180)
fpe=Label(root,text="fps")
fpe.place(x=0,y=270)
s4=Scale(from_=0,to=20,orient="horizontal")
s4.set(bkr)
s4.place(x=100,y=240)
em=Button(root,text="Emboss",command=emb)
con=Button(root,text="Contour",command=cont)
ed=Button(root,text="Edge Enhance",command=edg)
sm=Button(root,text="Smooth",command=smt)
do=Button(root,text="Done",command=don)
em.place(x=0,y=300)
con.place(x=0,y=340)
ed.place(x=0,y=380)
sm.place(x=0,y=420)
do.place(x=0,y=470)
l=Label(root)
l.place(x=270,y=60)
fg=Label(root,text="Preview",font=(20),height=3,fg="white",bg="black")
fg.place(x=270,y=0)
while True:
        if(ex==1):
                break
        try:
                if(fp.split(".")[-1]=="gif" or fp.split(".")[-1]=="mp4" or fp.split(".")[-1]=="avi" or fp.split(".")[-1]=="ogg"):
                        for i in a:
                                imageio.imwrite("wp.bmp",i)
                                break
                else:
                        raw=imageio.imread(fp)
                        imageio.imwrite("wp.bmp",raw)
                fh=imageio.imread("wp.bmp")
                imageio.imwrite("wp.jpg",fh)
                im=Image.open("wp.jpg")
                sw=1
                ads=list(im.size)
                while True:
                        if(ads[0]/sw<=root.winfo_screenwidth()*3/4 and ads[1]/sw<=root.winfo_screenheight()/2):
                                break
                        sw+=1

                im=im.resize((int(ads[0]/sw),int(ads[1]/sw)), Image.ANTIALIAS)
                imi=ImageEnhance.Brightness(im)
                im=imi.enhance(s.get())
                imi=ImageEnhance.Color(im)
                im=imi.enhance(s1.get())
                imi=ImageEnhance.Contrast(im)
                im=imi.enhance(s2.get())
                imi=ImageEnhance.Sharpness(im)
                im=imi.enhance(s3.get())
                if(wo==1):
                        im=im.filter(ImageFilter.EMBOSS)
                if(oo==1):
                        im=im.filter(ImageFilter.CONTOUR)
                if(jo==1):
                        im=im.filter(ImageFilter.EDGE_ENHANCE)
                if(vk==1):
                        im=im.filter(ImageFilter.SMOOTH)
                im.save("fm.gif")
                p=PhotoImage(file=os.path.abspath("fm.gif"))
                l["image"]=p
                root.update()
        except:
                raise
                pass
os.remove(os.path.abspath("wp.jpg"))
os.remove(os.path.abspath("fm.gif"))
os.remove(os.path.abspath("wp.bmp"))

Label(root,text="Please Wait").pack()
progress = Progressbar(root, orient = HORIZONTAL, 
              length = 100, mode = 'determinate')
def bar(): 
    progress['value'] = 20
    root.update()
    time.sleep(0.2)
    progress['value'] = 40
    root.update() 
    time.sleep(0.2)
    progress['value'] = 50
    root.update()
    time.sleep(0.2)
    progress['value'] = 60
    root.update()
    time.sleep(0.2)
    progress['value'] = 80
    root.update()
    time.sleep(0.2)
    progress['value'] = 100
progress.pack(pady = 10)

try:
    os.mkdir("wofkisjcdos")
except:
        pass
z1=os.path.abspath("wofkisjcdos")
az=0
for f in a:
    az+=1
    bar()
    root.update()
    imageio.imwrite(z1+"/"+str(az)+".bmp",f)
    f=imageio.imread(z1+"/"+str(az)+".bmp")
    imageio.imwrite(z1+"/"+str(az)+".jpg",f)
    im=Image.open(z1+"/"+str(az)+".jpg")
    imi=ImageEnhance.Brightness(im)
    im=imi.enhance(fj)
    imi=ImageEnhance.Color(im)
    im=imi.enhance(fh)
    imi=ImageEnhance.Contrast(im)
    im=imi.enhance(wn)
    imi=ImageEnhance.Sharpness(im)
    imqw=imi.enhance(wh)
    if(wo==1):
        im=im.filter(ImageFilter.EMBOSS)
    if(oo==1):
        im=im.filter(ImageFilter.CONTOUR)
    if(jo==1):
        im=im.filter(ImageFilter.EDGE_ENHANCE)
    if(vk==1):
        im=im.filter(ImageFilter.SMOOTH)    
    im.save(z1+"/"+str(az)+".gif")
    os.remove(z1+"/"+str(az)+".bmp")
    os.remove(z1+"/"+str(az)+".jpg")
onlyfiles = [f for f in listdir(z1) if isfile(join(z1, f))]
eof=root.winfo_children()
for dx in eof:
        dx.destroy()
soz=Label(root,bg="black")
soz.pack()
def play():
    for soo in onlyfiles:
        eoc=PhotoImage(file=z1+"/"+soo)
        soz["image"]=eoc
        root.update()
        if(bkr!=0):
            time.sleep(1/bkr)
    soz["image"]=eoc
    root.update()
def exit():
    for jsz in onlyfiles:
        os.remove(z1+"/"+jsz)
    sys.exit()
def save():
        if(fp.split(".")[-1]=="gif" or fp.split(".")[-1]=="mp4" or fp.split(".")[-1]=="ogg" or fp.split(".")[-1]=="avi"):
                wpz=imageio.get_writer(fp,fps=bkr)
        else:
                wpz=imageio.get_writer(fp)
        for mxz in onlyfiles:
                qza=imageio.imread(z1+"/"+mxz)
                wpz.append_data(qza)
if(fp.split(".")[-1]=="gif" or fp.split(".")[-1]=="mp4" or fp.split(".")[-1]=="ogg" or fp.split(".")[-1]=="avi"):
        Button(root,text="Play",command=play).pack()
Button(root,text="Exit",command=exit).pack()
Button(root,text="Save Changes",command=save).pack()
root.mainloop()
