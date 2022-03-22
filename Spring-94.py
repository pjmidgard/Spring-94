from time import time
cvf=0
import os
import binascii
import math
import os.path

lenf=0
name=""
szx=""
wer=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":


                        i=1

                    if namez=="e":
                        i=2
                 
                    sda4=""
                    sda5=""
                    sda6=""
                    
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    ccc=1
                    Cx=0
                    sda7=""
                    Circle_times2=0

                   

                    if i==2:
                        Format=".Spring93"
                        Long_Format=len(Format)
                        if nameas[nac-Long_Format:nac]==".Spring93":
                   
                        	nameas=name[:nac-Long_Format]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-Long_Format:nac]!=".Spring94":
                                print("Sorry, this is not .Spring94")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".Spring94"
                    
                    	
                    nac=len(nameas)
                    Lenf_File=0
                    
                    Circle_times3=0
                    Circle_times7=0
                    T8=0
                    
                    Circle_times5=0
                    Circle_times6=0
                    
                    Start_N=0

                    T9=0
                    
                    cvf=2
                    cvf1=0
                    s=""

                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""
                    sda16=""

                    sda11=""

                    D=0

                    DD=0
                    N1=2
                    Number_Back_N=7
                    T7=0
                    T8=0
                    T9=0
                    S=1
                    T7=0
                    T9=0
                    T=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()
                    T10=0

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        lenf8=lenf7
                        if lenf7>=(2**40)-1:
                                raise SystemExit
                        if lenf7==0:
                        	raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                        Lenf16=0
                                   
                        sda23=""
 
                        sda18=""
                        sda29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                

                                #########################################################################################################################################################
                                
                                
                                if i==1:
                                   
                                    lenf5=len(sda2)

                                    sda3=sda2
                                 
                                    lenf5=len(sda3)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                  
                                    sda17=""
                   
                                    g=0

                                    sda3=sda2

                                    lenf6=len(sda3)                      
                                    sda17=""
                                
                                    sda3=sda2

                                    lenf8=int((lenf7*8)//1.1)
                                    
                                    lenf6=len(sda3)
                                
                                    szx=""

                                    sda6=""
                                   
                                   

                                    #Compression

                                    sda10=""
                                    sda11=""
                                    
                                    sda17=""

                                    if Circle_times2==0 and S==1:
                                        sda3="11111111"+sda3
                                        S=0
                                    
                                    lenf6=len(sda3)
                                    
                                    
                                    sda4=sda3[lenf6:lenf6-8]

                                    sda11=sda4[::-1]
                                    
                                    sda6=sda3[0:lenf6-8]
                                    
                                    sda3=sda11+sda6
                                    Circle_times6=Circle_times6+1

                                    
                                   
                                            
                                    if sda3[0:8]=="11111111" and Circle_times6>0 or Circle_times6<=127 and sda3[0:8]=="11111111":

                                            
                                        

                                        sda15=bin(Circle_times6)[2:]
                                             
                                        lenf=len(sda15)
                                        
                                        szx4=""
                                        xc=7-lenf%7
                                        z=0
                                        if xc!=7:
                                                while z<xc:
                                                        szx4="0"+szx4
                                                        z=z+1

                                        sda16=sda16+szx4+sda15
                                        Lenf16=len(sda16)
                                        
                                        Circle_times6=0
                                        sda3=sda3[8:]
                                        
                                        
                                    if Circle_times6>127:
                                           ccc=2

                                    
                                   
                                    

                                                    
                                   
                              
                                    sda17=sda3
                                    lenfS=len(sda17)
                                    #print(lenfS)
                                
                                    
                                    

                                   
                                    Circle_times2=Circle_times2+1
                                    
                          
                                    sda2=sda17

                                    if lenf6>(2**48)-1:
                                            print("This file too big")
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)

                                    if  lenfS<=8 or Circle_times7==(2**48)-1 or ccc==2:
                                              
                                                    
                                              
                                                
                                             sda174=bin(Lenf16)[2:]
                                             
                                             
                                             lenf=len(sda174)
                                             
    

                                        
                                             szx5=""
                                             xc=48-lenf%48
                                             z=0
                                             if xc!=48:
                                                     while z<xc:
                                                         szx5="0"+szx5
                                                         z=z+1
                                    	

                                    if  lenfS<=8 or Circle_times7==(2**48)-1 or ccc==2:
                                                                                                                              
                                                    
                                              
                                                
                                             sda172=bin(lenf7)[2:]
                                             
                                             lenf=len(sda172)
                                             T=T+1
                                                                                
                                             
                                        
                                             szx3=""
                                             xc=48-lenf%48
                                             z=0
                                             if xc!=48:
                                                     while z<xc:
                                                         szx3="0"+szx3
                                                         z=z+1
                                    	
                                    if  lenfS<=8 or Circle_times7==(2**48)-1 or ccc==2:
                                              
                                                    
                                              
                                                
                                             sda171=bin(T)[2:]
                                             
                                             lenf=len(sda171)
                                        
                                             szx1=""
                                             xc=48-lenf%48
                                             z=0
                                             if xc!=48:
                                                     while z<xc:
                                                         szx1="0"+szx1
                                                         z=z+1
   
                               
                                    if  lenfS<=8 or Circle_times7==(2**48)-1 and c==2:
                                                
                                             sda17="1"+sda16+sda17
                                             lenf=len(sda17)
                                        
                                             szx=""
                                             xc=8-lenf%8
                                             z=0
                                             if xc!=8:
                                                     while z<xc:
                                                         szx="0"+szx
                                                         z=z+1
   
                                    
                                             lenf=len(sda17)
                                             
                                            
                                             sda17=szx5+sda174+szx3+sda172+szx1+sda171+szx+sda17
                                             sda16=""
                                             sda2=sda17
                                             ccc=1
                                             #print(len(sda17))

                                    if lenfS<=8 or Circle_times7==(2**48)-1:
                                        
                                    		L=len(sda17)
                                    		n = int(sda17, 2)
                                    		qqwslenf=len(sda17)
                                    		qqwslenf=(qqwslenf//8)*2
                                    		qqwslenf=str(qqwslenf)
                                    		qqwslenf="%0"+qqwslenf+"x"
                                    		jl=binascii.unhexlify(qqwslenf % n)
                                    		sssssw=len(jl)
                                    		szxzzza=""
                                    		szxzs=""
                                    		sda2=sda6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(jl)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    sda17=""
                              
                                    sda3=sda2
                                    
                                    lenf6=len(sda3)

                                    szx=""

                                    sda6=""

                                    #Extract

                                    sda10=""
                                    sda11=""
                                  
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    Minus_One_bits=""
                                    Number_Start=0
                                    Times=""
                                    Ones=""
                                    Minus_One=0
                                    
                                
                                    
                                    
                                    
                                    
                                    
                        
                                 
                                    if C==1:
                                        if   Circle_times2==0 and S==1:

                                                sda11=sda3[0:160]
                                                Lenf_File = int(sda11, 2)
                                                sda3=sda3[160:]

                                                Minus_One_bits=sda3[0:8]
                                                Minus_One = int(Minus_One_bits, 2)
                                                sda3=sda3[8:]

                                                Times=sda3[0:160]
                                                T = int(Times, 2)
                                                sda3=sda3[160:]
                                                

                                                if Minus_One==1:
                                                        Number_Start=-1
                                                
                                                        
                                                elif sda3[0:9]=="000000001":
                                                        sda3=sda3[9:]
                                                elif sda3[0:8]=="00000001":
                                                        sda3=sda3[8:]

                                                elif sda3[0:7]=="0000001":
                                                        sda3=sda3[7:]

                                                elif sda3[0:6]=="000001":
                                                        sda3=sda3[6:]

                                                elif sda3[0:5]=="00001":
                                                        sda3=sda3[5:]
                                                        
                                                elif sda3[0:4]=="0001":
                                                        sda3=sda3[4:]

                                                elif sda3[0:3]=="001":
                                                        sda3=sda3[3:]

                                                elif sda3[0:2]=="01":
                                                        sda3=sda3[2:]

                                                elif sda3[0:1]=="1":
                                                        sda3=sda3[1:]
                                                T7 = int(sda3, 2)
                                                S=0
                                                
                                                        
                                                                                        

                                        if   Circle_times2>=0:
                                                
                                              
                                                
                                                if C==1 and T!=0:
                                                        
                                                            
                                                            
                                                            
                                                            T7=T7+(2**Lenf_File)
                                                            Circle_times2=Circle_times2+1
                                                                    
                                                
                                                      
                                                        
                                                
                                                        
                                        if C==1 and T!=0:
                                                sda17=sda3
                                                
                                                
                                       
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                   
                                    sda5=""
                                    
                                    
                                    sda17=bin(T7)[2:]
                                     
                                    sda2=sda17
                                   

                                    if i==2:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                                

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        
                                        	   
                                        	   
                                        
                                            	
                                            if C==1 and T!=0 or T==0:
 
                                            	sda17=bin(T7)[2:]
                                            	lenf14=len(sda17)
                                            	#print(lenf14)
                                            	lenf16=lenf14%8
                                            	
                                            	
                                            	lenf=len(sda17)
                                            	szx=""
                                            	xc=(Lenf_File*8)-lenf%(Lenf_File*8)
                                            	z=0
                                            	if xc!=0:
                                            	        if xc!=Lenf_File*8:
                                            	            while z<xc:
                                            	            	szx="0"+szx
                                            	            	z=z+1
                                            	sda17=szx+sda17

                                            L=len(sda17)
                                         
                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
