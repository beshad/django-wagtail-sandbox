# Generated by Django 2.2.3 on 2019-07-17 01:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homepage_example'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='example',
        ),
        migrations.AddField(
            model_name='homepage',
            name='basic_stream_example',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', help_text='super helpful text')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True, verbose_name='Basic Stream Example'),
        ),
    ]
