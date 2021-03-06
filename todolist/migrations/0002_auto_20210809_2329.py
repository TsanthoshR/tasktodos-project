# Generated by Django 3.2.5 on 2021-08-09 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
