from django.db import models
from django.core.exceptions import ValidationError
from user.models import SUser

## 파일 크기 검사
def validate_file_size(value):
    max_size = 2 * 1024 * 1024  # 2MB
    if value.size > max_size:
        raise ValidationError('업로드 할 파일 사이즈는 2MB를 초과할 수 없습니다.')
        
## 파일 확장자 검사
def validate_image_extension(value):
    valid_extensions = ['jpg', 'jpeg', 'png']
    ext = value.name.split('.')[-1].lower()
    if ext not in valid_extensions:
        raise ValidationError("지원하는 확장자: jpg, jpeg, png")

"""
 * MODEL No. 1
 * MODEL Name : Review  ##테이블 이름
"""
class Review(models.Model):
    author = models.ForeignKey(SUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    imgfile = models.ImageField(
        blank=True,
        upload_to="images",
        null=True,
        validators=[validate_file_size, validate_image_extension]
    )

    def __str__(self):
        return self.subject


"""
 * MODEL No. 2
 * MODEL Name : Comment  ##테이블 이름
"""
class Comment(models.Model):
    author = models.ForeignKey(SUser, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()