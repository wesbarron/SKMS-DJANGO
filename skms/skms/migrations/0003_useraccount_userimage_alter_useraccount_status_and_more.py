# Generated by Django 4.1.6 on 2023-02-19 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skms', '0002_useraccount_delete_userpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='userimage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='type',
            field=models.CharField(choices=[('User', 'User'), ('Expert', 'Expert')], default='User', max_length=255),
        ),
    ]