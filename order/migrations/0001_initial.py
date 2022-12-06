# Generated by Django 4.1.3 on 2022-12-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('order is paid', 'order is not paid yet '), ('order is not paid', 'order is paid')], default='order is not paid', max_length=20)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
