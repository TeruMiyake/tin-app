from django.db import models
from django.contrib import admin
from django.conf import settings # カスタムユーザーモデルを使うため

from django.urls import reverse # レコード追加後の遷移先指定のため

import uuid # UUIDFieldを使うため

# Create your models here.
# モデルを作ったら、admin.py を編集！

