#Step 1: import modules 
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import os 


#Step 2: set up connection to email server 

#provide server address and port number 
#use smtp.ehlo() for ehlo(extended hello) command.
#use emtp.starttls() to enable tls(transfer layer service).
smtp = smtplib.SMTP('smtp.gmail.com',25)
smtp.ehlo()
smtp.starttls()

#login with our email and pasword
smtp.login('gupta.chakshu0301@gmail.com','chakshu0301')


#Step 3: send our email message 'msg' to other person

def message(subject='hello',text='',img=None,attachment=None):

    #build a message conntent 
    msg=MIMEMultipart()

    #add subject 
    msg['Subject']=subject

    #add text containt
    msg.attach(MIMEText(text))

    #add image 
    #check anything given in image or not 
    if img is not None:
        #check the img is in list form or not 
        if type(img) is not list:
            # if not , make it one
            img = [img]
        #iterate images list
        for one_img in img:
            #read the imaage data in binary from
            img_data = open(one_img,'rb').read()
            #attach the image data into message object using MIMEImage
            msg.attach(MIMEImage(img_data,name=os.path.basename(one_img)))

    
    #same for attachments 
    #check attachments given or not 
    if  attachment is not None:
        #check attachment is a list or not 
        if type(attachment) is not list:
            #make it one  
            attachment=[attachment]
        #iterate attchaments
        for one_attachment in attachment:
            with open(one_attachment,'rb') as f:
                #read in the attchment using MIMEApplication
                file = MIMEApplication(f.read(),name = os.path.basename(one_attachment))
            file['Content-Disposition'] = f'attachment;\
                    filename="{os.path.basename(one_attachment)}"'
            msg.attach(file)
        
    return msg

#call the message function
msg = message("hello",'i am chakshu gupta',r"C:\Users\HP\Downloads\poster (6).png",r"C:\Users\HP\Downloads\Pdf_858709330300723.pdf")

#make a list of emails ,where you wanna send mail
to = ["guptachakshu0107@gmail.com"]

#provide some data to the sendmail function
smtp.sendmail(from_addr='gupta.chakshu0301@gmail.com',to_addrs=to,msg=msg.as_string())

#finally, close the connection
smtp.quit()