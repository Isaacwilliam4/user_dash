# Generated by Django 2.2 on 2020-07-20 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard_app', '0003_auto_20200720_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='for_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments_for', to='user_dashboard_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='from_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments_from', to='user_dashboard_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='for_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='messages_for', to='user_dashboard_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='messages_from', to='user_dashboard_app.User'),
            preserve_default=False,
        ),
    ]
