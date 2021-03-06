# Generated by Django 2.2.3 on 2019-07-22 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('blog', '0009_auto_20190722_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=models.CharField(help_text='Overwrites the default title', max_length=100),
        ),
    ]
