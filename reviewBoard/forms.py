from django import forms
from PIL import Image
from django.core.exceptions import ValidationError
from reviewBoard.models import Review, Comment

#파일 유효성 검사
def validate_image(file):
    try:
        img = Image.open(file)
        img.verify()
    except Exception as e:
        raise ValidationError("Invalid image file")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        ## Review 모델 속성
        fields = ['subject', 'content', 'imgfile']
        labels = {
            'subject': '제목',
            'content': '내용',
            'imgfile': '이미지'
        }

    ## 업로드 시 유효한 이미지 파일인지 검사
    def clean_imgfile(self):
        imgfile = self.cleaned_data.get('imgfile', False)
        if imgfile:
            validate_image(imgfile)
        return imgfile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        ## Comment 모델 속성
        fields = ['content']
        labels = {
            'content': '댓글',
        }
