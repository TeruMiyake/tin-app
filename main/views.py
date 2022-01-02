from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q # 検索

# クラスベースビューのデコレート（login_required）をするため、method_decorator も必要になる
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# クラスベース汎用ビューのインポート
# レコード追加ビュー
from django.views.generic.edit import CreateView

# models.py からクラスとして定義されたモデル（＝DBテーブルになる）を読み込む
from .models import *
from accounts.models import User

# forms.py からクラスとして定義されたフォームを読み込む
from .forms import *

# Create your views here.

def index(request):
  users = User.objects.all()
  # そのうち、記録なしのユーザはフィルタしてもいいかも
  # users = users.filter(
  #   Q(text__icontains=searchword) # icontains : 部分一致
  # ).distinct() # 重複を省く（要るか？？modelsで重複を禁止すればいいのでは）
  return render(request, 'main/index.html', {'users':users})





# クラスベース汎用ビューを使ってみる

# ↑なんだっけそれ？ kkhub 参照