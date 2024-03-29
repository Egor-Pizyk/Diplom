# Generated by Django 4.1.5 on 2023-01-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_rename_work_type_id_workcategory_work_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='email',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='avatar_img',
            field=models.ImageField(blank=True, null=True, upload_to='user_upload/avatar_files/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='user_upload/cv_files/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='portfolio_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='telegram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
