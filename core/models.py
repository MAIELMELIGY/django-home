from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

class Header(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	icon = models.ImageField(null=True, blank=True)
	apple = models.ImageField(null=True, blank=True)
	navlogo = models.ImageField(null=True, blank=True)
	videofile= models.FileField(upload_to = 'videos/', null=True, verbose_name="")
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	slider_text = models.CharField(max_length=255, null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )

	def __str__(self):
		return self.title or ''
  
	@property
	def videofileURL(self):
		try:
			url = self.videofile.url
		except:
			url = ''
		return url

	@property
	def navlogoimageURL(self):
		try:
			url = self.navlogo.url
		except:
			url = ''
		return url

	@property
	def appleimageURL(self):
		try:
			url = self.apple.url
		except:
			url = ''
		return url

	@property
	def iconimageURL(self):
		try:
			url = self.icon.url
		except:
			url = ''
		return url

class About(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	body= RichTextField(null=True, blank=True)
	number_of_project = models.IntegerField(null=True , blank=True)
	number_of_Awards=models.IntegerField(null=True , blank=True)
	Years_of_experience=models.IntegerField(null=True , blank=True)
	number_of_client= models.IntegerField(null=True , blank=True)
	about_image = models.ImageField(upload_to= 'Home/', max_length=254,null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )

	def __str__(self):
		return self.title or ''
	@property
	def about_imageimageURL(self):
		try:
			url = self.about_image.url
		except:
			url = ''
		return url


class Client(models.Model):
	client_name = models.CharField(max_length=255)
	review_message = models.TextField(null=True, blank=True)
	img = models.ImageField(upload_to='Home/', max_length=254,null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )

	def __str__(self):
		return self.client_name or ''  
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url  
class mision_vision(models.Model):
	title = models.CharField(max_length=255)
	body =  RichTextField(null=True, blank=True)
	icon = models.CharField(max_length=255, null=True, blank=True)
	img = models.ImageField(upload_to='Home/', max_length=254,null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )

	def __str__(self):
		return self.title or ''  
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url  
class why_home(models.Model):
	icon = models.CharField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title or ''
class Service(models.Model):
	icon = models.CharField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255)
	body =  RichTextField(null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )


	def __str__(self):
		return self.title or ''

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=12)
	subject = models.CharField(max_length=100)
	message = RichTextField(null=True, blank=True)
	contact_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.email


class Projects_in(models.Model):
	img = models.ImageField(upload_to='Home/', max_length=254,null=True, blank=True)
	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

class SubCategory(models.Model):
	name = models.CharField(max_length=150)
	img = models.ImageField(upload_to='product/')
	slug =  models.SlugField(unique=True, null=True, blank=True )

	@property
	def imgimageURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

	def __str__(self):
		return self.name or ''
class Tag(models.Model):
	name = models.CharField(max_length=150)
	slug =  models.SlugField(unique=True, null=True, blank=True )
	description = RichTextField(null=True, blank=True)
	img_slider = models.ImageField(upload_to='product/' ,null=True, blank=True)
	img_description = models.ImageField(upload_to='product/' ,null=True, blank=True)
	def __str__(self):
		return self.name or ''
	@property
	def img_sliderimageURL(self):
		try:
			url = self.img_slider.url
		except:
			url = ''
		return url
	@property
	def img_descriptionimageURL(self):
		try:
			url = self.img_description.url
		except:
			url = ''
		return url
class ProductHdl (models.Model):
	SubCategory = models.ForeignKey(SubCategory ,on_delete=models.CASCADE)
	name = models.CharField(max_length=300)
	description = RichTextField(null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )
	image_1 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_2 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_3 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_4 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_5 = models.ImageField(upload_to='product/',null=True, blank=True)
	videofile= models.FileField(upload_to='videos/', null=True,blank=True)

	def __str__(self):
		return self.name
	@property
	def image_1imageURL(self):
		try:
			url = self.image_1.url
		except:
			url = ''
		return url

	@property
	def image_2imageURL(self):
		try:
			url = self.image_2.url
		except:
			url = ''
		return url

	@property
	def image_3imageURL(self):
		try:
			url = self.image_3.url
		except:
			url = ''
		return url

	@property
	def image_4imageURL(self):
		try:
			url = self.image_4.url
		except:
			url = ''
		return url

	@property
	def image_5imageURL(self):
		try:
			url = self.image_5.url
		except:
			url = ''
		return url

	@property
	def videofileURL(self):
		try:
			url = self.videofile.url
		except:
			url = ''
		return url
class ProductTuya(models.Model):
	SubCategory = models.ForeignKey(SubCategory ,on_delete=models.CASCADE)
	name = models.CharField(max_length=300)
	tag = models.ForeignKey(Tag ,on_delete=models.CASCADE )
	description = RichTextField(null=True, blank=True)
	slug =  models.SlugField(unique=True, null=True, blank=True )
	image_1 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_2 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_3 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_4 = models.ImageField(upload_to='product/',null=True, blank=True)
	image_5 = models.ImageField(upload_to='product/',null=True, blank=True)
	videofile= models.FileField(upload_to='videos/', null=True, blank=True)
	def __str__(self):
		return self.name


	@property
	def image_1imageURL(self):
		try:
			url = self.image_1.url
		except:
			url = ''
		return url

	@property
	def image_2imageURL(self):
		try:
			url = self.image_2.url
		except:
			url = ''
		return url

	@property
	def image_3imageURL(self):
		try:
			url = self.image_3.url
		except:
			url = ''
		return url

	@property
	def image_4imageURL(self):
		try:
			url = self.image_4.url
		except:
			url = ''
		return url

	@property
	def image_5imageURL(self):
		try:
			url = self.image_5.url
		except:
			url = ''
		return url

	@property
	def videofileURL(self):
		try:
			url = self.videofile.url
		except:
			url = ''
		return url