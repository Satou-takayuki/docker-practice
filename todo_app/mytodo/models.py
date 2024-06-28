from django.db import models


# Create your models here.
class Task(models.Model):
    class Meta:
        db_table = "tasks"
    
    # タスク名　テキスト(短い)データ　NotNull
    title = models.CharField(verbose_name="タスク名", max_length=255)
    
    # 詳細　テキスト(長い)データ
    description = models.TextField(verbose_name="詳細", null=True, blank=True)
    
    # 完了フラグ　数値データ(1=完了　0=未完了)　デフォルト=0
    comlete = models.IntegerField(verbose_name="完了フラグ", default=0)
    
    # 開始日時
    start_date = models.DateTimeField(verbose_name="開始日", null=True, blank=True)
    
    # 終了日時
    end_date = models.DateTimeField(verbose_name="終了日", null=True, blank=True)
    
    def __str__(self):
        return self.title
    