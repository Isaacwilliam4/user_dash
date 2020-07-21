# Generated by Django 2.2 on 2020-07-20 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0004_auto_20200720_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='for_user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='from_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user_dashboard_app.User'),
            preserve_default=False,
        ),
    ]
