from django.db import models
from datas.models import DogBreed

class MyPet(models.Model):
    class Meta:
        verbose_name = "등록된 반려 동물"
        verbose_name_plural = "등록된 반려 동물"
    
    owner = models.CharField('주인 계정', max_length = 20)
    name = models.CharField('반려동물 이름', max_length = 20)
    age = models.CharField('반려동물 생년월일', max_length = 50)
    breed = models.ForeignKey(DogBreed, on_delete = models.SET_NULL, blank=True, null=True)
    weight = models.CharField('체중', max_length = 50)

    def __str__(self):
        return f"{self.owner}님의 반려동물 - {self.name} 정보"