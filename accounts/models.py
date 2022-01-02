from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib import auth # UserManagerのため

from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import uuid # UUIDFieldを使うため

# Create your models here.

# django.contrib.auth.models からコピーして編集している
class User(AbstractUser):
  pass

  # id を UUID に変更
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  # username は 実質 userid として使う
  # UnicodeUsernameValidator は日本語を許容してしまう
  username_validator =  ASCIIUsernameValidator()
  username = models.CharField(
    _('ユーザー ID'),
    unique=True,
    max_length=150,
    help_text=_(
      'Required. 150 characters or fewer.'
      ' Letters, digits and @/./+/-/_ only.'),
    validators=[username_validator],
  )
  displayname_validator = UnicodeUsernameValidator()
  displayname = models.CharField(
    _('ランキング表示名'),
    max_length=40,
    help_text=_('（必須）40 文字以下にしてください。'),
    validators=[displayname_validator],
  )
  tmptime = models.DecimalField(
    _('最高記録'),
    max_digits=7,
    decimal_places=3,
    default=999.999,
    validators=[MinValueValidator(18.0, message="正しい記録を入力してください。")],
    help_text=_('（必須）333.333 など、半角英数時で小数点 3 桁まで入力してください。'))
  tmpmiss = models.IntegerField(_('最高記録時のミス数'), 
    null=False,
    default=0,
    help_text=('（必須）最高記録時のミス数を入力してください。※ 51 ミス以上だと登録できません。'),
    validators=[MaxValueValidator(50, message="51 ミス以上だと登録できません。")]
  )
  tmpevidenceurl = models.URLField(_('スクリーンショット等の URL'),
    blank=True,
    help_text=_('（推奨）ただし、β 版への移行時などに SS 無しの記録を削除することがあり得ます。'))
  tmpuserurl = models.URLField(_('Web サイトや Twitter アカウント等の URL'),
    blank=True,
    help_text=_('（不要）必須ではありません。友達づくり用です。'))
  def __str__(self):
    return self.username