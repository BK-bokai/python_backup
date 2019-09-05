from django.db import models

# Create your models here.
class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址
	def __str__(self):
		return self.vendor_name
		
class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	price_name = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢,max_digits = 3 最大長度,decimal_places=0 小數點後幾位
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的,CASCADE(聯集)當今天攤販被delete，連同食物也會一起刪除。

	def __str__(self):
	    return self.food_name