
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



# Create your models here.
class Todos(models.Model):
    reqdate = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField()
    part = models.CharField(max_length=50)
    description = models.TextField( )
    duedate = models.DateField()
    vendor = models.CharField(max_length=50)
    refnum = models.CharField(max_length=25, )
    toapprove= models.BooleanField(default=False)
    tobill = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    rush = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billed = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    amount= models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    

    def __str__(self):
        return self.part 


class QRCode(models.Model):
    item = models.OneToOneField(Todos, on_delete=DO_NOTHING, primary_key=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
  
    def save(self, todo_id,*args, **kargs):

        qr= qrcode.QRCode(version=1,box_size =5, border =1)
        qr.add_data(todo_id)
        qr.make(fit=True)
 
        #qrcode_img= qrcode.make(todo_id)
        #print(self.item)
        #canvas = Image.new('RGB', (290, 290), 'white')
        #draw = ImageDraw(canvas)
        #canvas.paste(qr)
        fname = f'qr_code-{self.item}'+'.png'
        buffer = BytesIO()
        img = qr.make_image(fill='black', back_color='white')
        img.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        #canvas.close()
        super().save(*args, **kargs)

    def __str__(self):
        return str(self.item)




    # def save(self, *args, **kargs):
        
    #     qrcode_img= qrcode.make(self.pk.name)
    #     print(self.pk.name)
    #     canvas = Image.new('RGB', (290, 290), 'white')
    #     #draw = ImageDraw(canvas)
    #     canvas.paste(qrcode_img)
    #     fname = f'qr_code-{self.part}'+'.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kargs)
 
    