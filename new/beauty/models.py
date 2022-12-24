from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

service_list= (
	('Tailoring','Tailoring'),
	('Hair Style','Hair Style'),
	('Heena','Heena'),
	('Neckles','Neckles'),
	('Hand ring', 'Hand ring'),
	('Puredicurist','Puredicurist')
	)

class Service(models.Model):
	name = models.CharField(max_length=70,default=True)

	def __str__(self):
		return str(self.name)
		


		#return reverse('service', args=(str(self.id)))

	

	#def get_absolute_url(self):
		#return reverse('from', args=(str(self.id)))


		



	#def get_absolute_url(self):
		#return reverse('article', args=(str(self.id)))
		#return reverse('home')



class Time_BOOK(models.Model):
	book_time=models.TimeField()

	def __str__(self):
		return f"{self.book_time}"
		




class Person(models.Model):
	full_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	mobile = models.CharField(max_length=20)
	date = models.DateField(default=True)
	time=models.OneToOneField(Time_BOOK,on_delete=models.CASCADE,related_name='book')
	book = models.ManyToManyField(Service, choices=service_list, default=True)

	

	def __str__(self):
		return f"{self.full_name} | {self.address} | {self.mobile} | {self.date} | {self.time} | {self.book}"

#class BOOK_Service(models.Model):
 	#book_service = models.CharField(max_length=10)

 	#def __str__(self):
 	#	return self.book_service


#class Time_BOOK(models.Model):
	#time_book = models.TimeField()

	#def __str__(self):
	#	return self.time



#class BOOK(models.Model):
	#name = models.ForeignKey(Person,on_delete=models.CASCADE)
	#time = models.OneToOneField(Time_BOOK,on_delete=models.CASCADE)
	#service=models.ForeignKey(book_time,on_delete=models.CASCADE)
	#book = models.ManyToManyField(BOOK_Service, choice=service_list,on_delete = models.CASCADE)

	#def __str__(self):
		#return self.name






