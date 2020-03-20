# Generated by Django 2.2.6 on 2020-03-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '账号', 'verbose_name_plural': '账号'},
        ),
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('1', '男'), ('2', '女'), ('0', '未知')], default='0', max_length=1, verbose_name='性别'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='ips',
            field=models.TextField(blank=True, null=True, verbose_name='IP历史'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='管理员备注（用户不会看到）'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='type',
            field=models.CharField(choices=[(0, '管理员'), (1, '普通用户')], default='99', max_length=2, verbose_name='类型'),
        ),
    ]