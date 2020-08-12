from django.db import models

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


class AgeRange(models.Model):
      
    class Meta:
        verbose_name = "연령 데이터"
        verbose_name_plural = "연령 데이터"
    # temp = models.CharField
    name = models.CharField('연령', max_length=20)
    slug = models.SlugField('슬러그', blank=True, null=True)
    desc = models.TextField('설명', blank=True)
    min_age = models.PositiveIntegerField("최소 개월수", blank=True, null=True)
    max_age = models.PositiveIntegerField("최대 개월수", blank=True, null=True)
    # 이처럼 age range를 받고,
    # caution_disease = models.TextField('주의 질병(피부/관절/눈/심장/신장/방광/치아/간/췌장염/종양/비타민결핍/칼슘결핍/면역력결핍)', null=True, blank=True)
    disease = models.ManyToManyField(Disease, verbose_name="관련 질병", blank=True, null=True) 
    # wp에는... 해당 나이에 대한 질병 데이터가 있숨.... => 그래서 그냥 그걸 데이터로 띄워주는데 이것 필요할까?
        
    a = models.PositiveIntegerField('피부(위험도 %)', null=True, blank=True)
    b = models.PositiveIntegerField('관절(위험도 %)', null=True, blank=True)
    c = models.PositiveIntegerField('눈(위험도 %)', null=True, blank=True)
    d = models.PositiveIntegerField('심장(위험도 %)', null=True, blank=True)
    e = models.PositiveIntegerField('신장(위험도 %)', null=True, blank=True)
    f = models.PositiveIntegerField('방광(위험도 %)', null=True, blank=True)
    g = models.PositiveIntegerField('치아(위험도 %)', null=True, blank=True)
    h = models.PositiveIntegerField('간(위험도 %)', null=True, blank=True)
    i = models.PositiveIntegerField('췌장염(위험도 %)', null=True, blank=True)
    j = models.PositiveIntegerField('종양(위험도 %)', null=True, blank=True)
    k = models.PositiveIntegerField('비타민결핍(위험도 %)', null=True, blank=True)
    m = models.PositiveIntegerField('칼슘결핍(위험도 %)', null=True, blank=True)
    l = models.PositiveIntegerField('면역력결핍(위험도 %)', null=True, blank=True)
    n = models.PositiveIntegerField('장건강(위험도 %)', null=True, blank=True)
    o = models.PositiveIntegerField('비만(위험도 %)', null=True, blank=True)
    p = models.PositiveIntegerField('호흡기(위험도 %)', null=True, blank=True)

    def __str__(self):
        return self.name


class DogBreed(models.Model):
    class Meta:
        verbose_name = "품종 데이터"
        verbose_name_plural = "품종 데이터"

    name = models.CharField('견종', max_length=20)

    def __str__(self):
        return self.name
