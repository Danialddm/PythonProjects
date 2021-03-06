# Generated by Django 3.0.4 on 2020-04-02 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_auto_20200316_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_word', models.CharField(max_length=32)),
                ('user_name', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=50)),
                ('desc_comm', models.CharField(blank=True, max_length=500)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
