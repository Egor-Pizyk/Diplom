# Generated by Django 4.1.5 on 2023-01-29 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_candidate_contactmethod_country_worktype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workcategory',
            old_name='work_type_id',
            new_name='work_type',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='avatar_img',
            field=models.ImageField(upload_to='user_upload/avatar_files/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='cv_file',
            field=models.FileField(upload_to='user_upload/cv_files/'),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('about_company', models.TextField()),
                ('position', models.CharField(max_length=255)),
                ('company_url', models.URLField()),
                ('dou_url', models.URLField()),
                ('employ_count', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
