# Generated by Django 4.1.13 on 2024-01-01 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_usercertification_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usereducation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userinterest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userlanguage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersocialmedia',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userworkexperience',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserCertification',
        ),
        migrations.DeleteModel(
            name='UserContact',
        ),
        migrations.DeleteModel(
            name='UserEducation',
        ),
        migrations.DeleteModel(
            name='UserInterest',
        ),
        migrations.DeleteModel(
            name='UserLanguage',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserProject',
        ),
        migrations.DeleteModel(
            name='UserSkill',
        ),
        migrations.DeleteModel(
            name='UserSocialMedia',
        ),
        migrations.DeleteModel(
            name='UserWorkExperience',
        ),
    ]