from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw, ImageFont

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    qr_code = models.ImageField(blank=True, upload_to='qrcodes/')
    date = models.DateField()

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.qr_code:
            event_info = f"{self.name}\n\n{self.description}\n\nDate: {self.date}"
            # qrcode_img = qrcode.make(self.name)
            qrcode_img = qrcode.make(event_info)
            canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)

            # Add the event info as text to the QR code image
            # draw = ImageDraw.Draw(canvas)
            # font = ImageFont.load_default()
            # text = event_info
            # text_width, text_height = draw.textsize(text, font)
            # x = (qrcode_img.pixel_size - text_width) / 2
            # y = qrcode_img.pixel_size
            # draw.text((x, y), text, font=font, fill='black')


            fname = f'qr_code-{self.name}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)