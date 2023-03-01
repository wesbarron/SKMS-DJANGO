# Generated by Django 4.1.6 on 2023-03-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skms', '0005_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_comments', models.TextField()),
                ('voice_user', models.CharField(choices=[('Current User', 'Current User'), ('Anonymous', 'Anonymous')], default='Anonymous', max_length=300)),
                ('voice_date', models.DateTimeField(auto_now_add=True)),
                ('contact_preference', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='N', max_length=3)),
                ('voice_anonymously', models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='Y', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='report_anonymously',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], default='Y', max_length=3),
        ),
        migrations.AlterField(
            model_name='report',
            name='reporter_name',
            field=models.CharField(choices=[('Current User', 'Current User'), ('Anonymous', 'Anonymous')], default='Anonymous', max_length=300),
        ),
    ]
