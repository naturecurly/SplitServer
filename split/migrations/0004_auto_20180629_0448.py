# Generated by Django 2.0.6 on 2018-06-29 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('split', '0003_auto_20180629_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='user',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='split.Profile'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='username',
            field=models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='requests_from', to='split.Profile'),
        ),
    ]
