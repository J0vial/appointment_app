# Generated by Django 4.1 on 2022-09-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_additionaluserinfo_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaluserinfo',
            name='catagory',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('patient', 'patient')], max_length=50),
        ),
    ]
