from django.db import models

class AgeRange(models.Model):
      
    class Meta:
        verbose_name = "연령 데이터"
        verbose_name_plural = "연령 데이터"

    name = models.CharField('연령', max_length=20)
    desc = models.TextField('설명', blank=True)
    # min_age = models.
    # max_age = models.
    # 이처럼 age range를 받고,
    # wp에는... 해당 나이에 대한 질병 데이터가 있숨.... => 그래서 그냥 그걸 데이터로 띄워주는데 이것 필요할까?
    # 
    def __str__(self):
        return self.name



        
class Disease(models.Model):
      
    class Meta:
        verbose_name = "질병 데이터"
        verbose_name_plural = "질병 데이터"

    name = models.CharField('질병 이름', max_length=20)
    desc = models.TextField('설명', blank=True)
    
    def __str__(self):
        return self.name

class NutrientData(models.Model):
      
    class Meta:
        verbose_name = "영양 성분 데이터"
        verbose_name_plural = "영양 성분 데이터"

    name = models.CharField('영양 성분', max_length=20)
    desc = models.TextField('설명', blank=True)
    disease = models.ManyToManyField(Disease, verbose_name="관련 질병", blank=True, null=True) 
    
    def __str__(self):
        return self.name


class DogBreed(models.Model):
    class Meta:
        verbose_name = "품종 데이터"
        verbose_name_plural = "품종 데이터"

    name = models.CharField('견종', max_length=20)

    def __str__(self):
        return self.name
