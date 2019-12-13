from django.db import models

# Create your models here.

#모델이 바뀌면 makemigration 다시
class Mguser(models.Model):
    objects = models.Manager() # vscode 오류 / 추가하고 or pylint-django 설치
    username = models.CharField(max_length=128,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')                                
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    def __str__(self): # 관리자페이지에 object를 이름으로 명시
        return self.username

    class Meta:
        db_table = 'mg_mguser'
        verbose_name = 'mg 사용자'
        verbose_name_plural = 'mg 사용자' # 복수형