from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


STATUS_CHOICES = (
   ('In Process', 'In process'),

   ('Accepted', 'Accepted'),

   ('Failed', 'Failed'),
)

class SendSubmission(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    name = models.CharField('name', max_length=25)

    surname = models.CharField('surname', max_length=25)

    email = models.EmailField('email')

    phone = PhoneNumberField(null=False, blank=False, unique=True)

    organization = models.CharField('organization', max_length=60)

    position = models.CharField('position', max_length=60)

    city = models.CharField('city', max_length=60)

    post_code_city = models.CharField('post_code_city', max_length=60)

    postal_address = models.CharField('postal_address', max_length=100)

    web_site = models.CharField('web_site', max_length=40)

    fax = models.CharField('fax', max_length=60)

    institute = models.CharField('institute', max_length=100)

    abstract_title = models.CharField('abstract_title', max_length=100)

    upload_abstract = models.FileField('upload_abstract', upload_to='file/', null=False, blank=False)

    talk_s = models.CharField('Do you have a talk', max_length=6, default="unsignet")

    section = models.CharField('section', max_length=40)

    invitation_s = models.CharField('Do you need a letter of invitation:', max_length=6,default="unsignet")

    message = models.TextField('message')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='In Process')

    send_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):

        return '%s %s' % (self.user, self.abstract_title)


