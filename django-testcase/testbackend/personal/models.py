from django.db import models
from datas.models import DogBreed



def get_mypet_image_filename(instance, filename):
    instance_id = instance.owner
    return f"mypet_images/{instance_id}/{filename}"


class MyPet(models.Model):
    class Meta:
        verbose_name = "등록된 반려 동물"
        verbose_name_plural = "등록된 반려 동물"
    
    owner = models.CharField('주인 계정', max_length = 20)
    name = models.CharField('반려동물 이름', max_length = 20)
    age = models.CharField('반려동물 생년월일', max_length = 50)
    breed = models.ForeignKey(DogBreed, on_delete = models.SET_NULL, blank=True, null=True)
    weight = models.CharField('체중', max_length = 50)
    image = models.ImageField('반려동물 이미지', upload_to = get_mypet_image_filename, default='mypet_images/default/dog.jpg')
    
    def __str__(self):
        return f"{self.owner}님의 반려동물 - {self.name} 정보"