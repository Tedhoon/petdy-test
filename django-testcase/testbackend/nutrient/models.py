from django.db import models

class Feed(models.Model):
    
    class Meta:
        verbose_name = "사료"
        verbose_name_plural = "사료"

    name = models.CharField("사료 이름", max_length=50)
    TYPE_CHOICES = (
        ('촉촉', '촉촉'),
        ('처방', '처방')
    )
    types = models.CharField("분류", max_length=2, choices=TYPE_CHOICES)  
    # 칼로리 수분량 조단백 조지방 조섬유 조회분 칼슘 인
    calorie = models.CharField("칼로리", max_length=1000)
    moisture = models.CharField("수분량", max_length=1000)
    crude_protein = models.CharField("조단백", max_length=1000)
    crude_fat = models.CharField("조지방", max_length=1000)
    crude_fiber = models.CharField("조섬유", max_length=1000)
    crude_ash = models.CharField("조회분", max_length=1000)
    calcium = models.CharField("칼슘", max_length=1000)
    phosphorus = models.CharField("인", max_length=1000)

class Snack(models.Model):
    
    class Meta:
        verbose_name = "간식"
        verbose_name_plural = "간식"
        
    name = models.CharField("간식 이름", max_length=50)
    pass

class Nutrient(models.Model):
    
    class Meta:
        verbose_name = "영양제"
        verbose_name_plural = "영양제"
        

    name = models.CharField("영양제 이름", max_length=50)
    calorie = models.CharField("칼로리", max_length=1000)
    moisture = models.CharField("수분량", max_length=1000)
    crude_protein = models.CharField("조단백", max_length=1000)
    crude_fat = models.CharField("조지방", max_length=1000)
    crude_fiber = models.CharField("조섬유", max_length=1000)
    crude_ash = models.CharField("조회분", max_length=1000)
    calcium = models.CharField("칼슘", max_length=1000)
    phosphorus = models.CharField("인", max_length=1000)
    
