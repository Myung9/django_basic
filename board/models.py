from django.db import models

# Create your models here.


class Board(models.Model):
    objects = models.Manager() 
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('mguser.Mguser',
                                on_delete=models.CASCADE, # 삭제되면 같이 삭제
                                verbose_name='작성자')                                
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    def __str__(self): 
        return self.title

    class Meta:
        db_table = 'mg_board'
        verbose_name = '게시글'
        verbose_name_plural = 'mg 게시글' # 복수형