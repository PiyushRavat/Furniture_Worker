from django.db import models
from django.urls import reverse

# Create your models here.
# class Category(models.Model):
# 	fur_name = models.CharField(max_length=120)

# 	def __str__(self):
# 		return self.fur_name

class Category(models.Model):
	name=models.CharField(max_length=250)
	slug=models.SlugField(max_length=200, unique=True)                                             

	# def get_absolute_url(self):
 #        return reverse('c', args=[self.slug, self.self])
	
	def __str__(self):
		return self.name

   
class Home(models.Model):
	img  = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg');
	name = models.CharField(max_length = 35);
	desc = models.CharField(max_length = 100); 
	slug = models.SlugField(max_length=100);


	def __str__(self):
		return self.name



class Worker(models.Model):
	img  = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg');
	city = models.CharField(max_length = 50);
	name = models.CharField(max_length = 35);
	desc = models.CharField(max_length = 100); 
	address = models.CharField(max_length = 100); 
	Experience = models.IntegerField(max_length= 10); 
	mobile = models.PositiveIntegerField();
	slug = models.SlugField(max_length=100);


	def __str__(self):
		return self.name


# class Worker(models.Model):
# 	#img  = models.ImageField(upload_to = 'pic_folder/');
# 	img = models.CharField(max_length = 500);
# 	name = models.CharField(max_length = 50);
# 	city = models.CharField(max_length = 50)
# 	#disc = models.CharField(max_length = 100, blank=True); 
# 	slug = models.SlugField(max_length=250);
# 	cw = models.IntegerField();
# 	ex = models.IntegerField();
# 	category = models.ForeignKey(Category,max_length = 50, on_delete=models.CASCADE);
# 	#project = models.IntegerField(max_length=20, blank=True);

# 	def __str__(self):
# 		return self.name

# 	def get_absolute_url(self):
# 		return reverse('detail',args=[self.id,self.self])