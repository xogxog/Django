from django.db import models

# Create your models here.


class Artist(models.Model) :
    name = models.CharField(max_length=20)
    birth = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', blank=True) # 프로필사진 경로 들어가는 곳
    content = models.TextField()

    def __str__(self) -> str:
        return self.name

#album_index에 보내줄 db
class Albums(models.Model) :
    title = models.CharField(max_length=50)
    released = models.CharField(max_length=50)
    singer = models.CharField(max_length= 30)
    album_cover = models.FileField(upload_to='album_cover/', blank=False)

    def __str__(self) -> str:
        return self.title

#album_detail에 보내줄 db
class songs(models.Model):
    album_fk = models.ForeignKey(Albums, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    stars = models.CharField(max_length=5)
    
    def __str__(self) -> str:
        return self.title
