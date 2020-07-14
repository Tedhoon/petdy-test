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
    calorie = models.CharField("칼로리(kcal/100g)", max_length=1000)
    moisture = models.CharField("수분량(%)", max_length=1000)
    crude_protein = models.CharField("조단백(%)", max_length=1000)
    crude_fat = models.CharField("조지방(%)", max_length=1000)
    crude_fiber = models.CharField("조섬유(%)", max_length=1000)
    crude_ash = models.CharField("조회분(%)", max_length=1000)
    calcium = models.CharField("칼슘(%)", max_length=1000)
    phosphorus = models.CharField("인(%)", max_length=1000)

    # 환산 기준
    # standard = models.CharField("기준량(g)", max_length=1000, default="", blank=True, null=True)

    def __str__(self):
        return self.name

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
    # 칼로리 수분량 조단백 조지방 조섬유 조회분 칼슘 인
    calorie = models.CharField("칼로리(kcal/100g)", max_length=1000)
    moisture = models.CharField("수분량(%)", max_length=1000)
    crude_protein = models.CharField("조단백(%)", max_length=1000)
    crude_fat = models.CharField("조지방(%)", max_length=1000)
    crude_fiber = models.CharField("조섬유(%)", max_length=1000)
    crude_ash = models.CharField("조회분(%)", max_length=1000)
    calcium = models.CharField("칼슘(%)", max_length=1000)
    phosphorus = models.CharField("인(%)", max_length=1000)

    def __str__(self):
        return self.name
    









# 본 모델은 1g당 존재하는 kcal, ml, g수
class ExchangedFeed(models.Model):
    
    class Meta:
        verbose_name = "사료 환산 - [1g당 성분양]"
        verbose_name_plural = "사료 환산- [1g당 성분양]"

    name = models.CharField("사료 이름", max_length=50)
    TYPE_CHOICES = (
        ('촉촉', '촉촉'),
        ('처방', '처방')
    )
    types = models.CharField("분류", max_length=2, choices=TYPE_CHOICES)  
    # 칼로리 수분량 조단백 조지방 조섬유 조회분 칼슘 인
    calorie = models.CharField("칼로리(kcal)", max_length=1000)
    moisture = models.CharField("수분량(g)", max_length=1000)
    crude_protein = models.CharField("조단백(g)", max_length=1000)
    crude_fat = models.CharField("조지방(g)", max_length=1000)
    crude_fiber = models.CharField("조섬유(g)", max_length=1000)
    crude_ash = models.CharField("조회분(g)", max_length=1000)
    calcium = models.CharField("칼슘(g)", max_length=1000)
    phosphorus = models.CharField("인(g)", max_length=1000)

    def __str__(self):
        return self.name



# 본 모델은 1g당 존재하는 kcal, ml, g수
class ExchangedNutrient(models.Model):
    
    class Meta:
        verbose_name = "영양제 환산 - [1g당 성분양]"
        verbose_name_plural = "영양제 환산- [1g당 성분양]"

    name = models.CharField("영양제 이름", max_length=50)

    calorie = models.CharField("칼로리(kcal)", max_length=1000)
    moisture = models.CharField("수분량(g)", max_length=1000)
    crude_protein = models.CharField("조단백(g)", max_length=1000)
    crude_fat = models.CharField("조지방(g)", max_length=1000)
    crude_fiber = models.CharField("조섬유(g)", max_length=1000)
    crude_ash = models.CharField("조회분(g)", max_length=1000)
    calcium = models.CharField("칼슘(g)", max_length=1000)
    phosphorus = models.CharField("인(g)", max_length=1000)

    def __str__(self):
        return self.name