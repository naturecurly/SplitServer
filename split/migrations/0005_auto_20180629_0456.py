# Generated by Django 2.0.6 on 2018-06-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split', '0004_auto_20180629_0448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='username',
            new_name='friend',
        ),
        migrations.AddField(
            model_name='relationship',
            name='is_pending',
            field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='is_friend',
        ),
        migrations.AlterUniqueTogether(
            name='relationship',
            unique_together={('user', 'friend')},
        ),
    ]
