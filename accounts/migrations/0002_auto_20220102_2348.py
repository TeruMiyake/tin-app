# Generated by Django 3.1.1 on 2022-01-02 14:48

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='displayname',
            field=models.CharField(help_text='（必須）40 文字以下にしてください。', max_length=40, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ランキング表示名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tmpevidenceurl',
            field=models.URLField(blank=True, help_text='（推奨）ただし、β 版への移行時などに SS 無しの記録を削除することがあり得ます。', verbose_name='スクリーンショット等の URL'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tmpmiss',
            field=models.IntegerField(default=0, help_text='（必須）最高記録時のミス数を入力してください。※ 51 ミス以上だと登録できません。', validators=[django.core.validators.MaxValueValidator(50, message='51 ミス以上だと登録できません。')], verbose_name='最高記録時のミス数'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tmptime',
            field=models.DecimalField(decimal_places=3, default=999.999, help_text='（必須）333.333 など、半角英数時で小数点 3 桁まで入力してください。', max_digits=7, validators=[django.core.validators.MinValueValidator(18.0, message='正しい記録を入力してください。')], verbose_name='最高記録'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tmpuserurl',
            field=models.URLField(blank=True, help_text='（不要）必須ではありません。友達づくり用です。', verbose_name='Web サイトや Twitter アカウント等の URL'),
        ),
    ]
