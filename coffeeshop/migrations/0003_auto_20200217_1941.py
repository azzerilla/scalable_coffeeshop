# Generated by Django 2.1.2 on 2020-02-17 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0002_auto_20200217_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizableAttributeOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, verbose_name='Customizable Field Option')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='coffeeshop.CustomizableAttribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='customizableattributeoptions',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='product',
            name='customizable_Attributes',
        ),
        migrations.AddField(
            model_name='product',
            name='customizable_attributes',
            field=models.ManyToManyField(to='coffeeshop.CustomizableAttribute'),
        ),
        migrations.DeleteModel(
            name='CustomizableAttributeOptions',
        ),
    ]
