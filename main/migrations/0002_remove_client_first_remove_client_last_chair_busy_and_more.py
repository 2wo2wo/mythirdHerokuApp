# Generated by Django 4.0.3 on 2022-04-07 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='first',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last',
        ),
        migrations.AddField(
            model_name='chair',
            name='busy',
            field=models.BooleanField(default=False, verbose_name='bandmi: '),
        ),
        migrations.AddField(
            model_name='client',
            name='User_id',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='client',
            name='chair',
            field=models.ManyToManyField(blank=True, related_name='desks', to='main.chair'),
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='client',
            name='online',
            field=models.BooleanField(default=False, verbose_name='onlinemi: '),
        ),
        migrations.AddField(
            model_name='meal',
            name='info',
            field=models.TextField(default='info', verbose_name='ovqat haqida: '),
        ),
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.FloatField(default='0.00', verbose_name='price: '),
        ),
        migrations.RemoveField(
            model_name='client',
            name='meals',
        ),
        migrations.AddField(
            model_name='client',
            name='meals',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.meal'),
        ),
    ]
