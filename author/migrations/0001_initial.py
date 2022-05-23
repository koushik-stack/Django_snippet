# Generated by Django 3.2.5 on 2022-05-23 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'moderator'), (3, 'general')], default=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='profile-pic-default.jpg', upload_to='profile_images')),
                ('cover_pic', models.ImageField(default='cover-pic-default.jpg', upload_to='cover_images')),
                ('bio', models.CharField(help_text='Short Bio (eg. I love traveling and games)', max_length=100)),
                ('address', models.CharField(help_text='Enter Your Address', max_length=100)),
                ('city', models.CharField(help_text='Enter Your City', max_length=100)),
                ('country', models.CharField(help_text='Enter Your Country', max_length=100)),
                ('zip_code', models.CharField(help_text='Enter Your Zip Code', max_length=100)),
                ('twitter_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('instagram_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('facebook_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('github_url', models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmailConfirmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=500)),
                ('email_confirm', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Email Confirm',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, to='author.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]