# Generated by Django 3.0.1 on 2020-01-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200107_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_dp',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
