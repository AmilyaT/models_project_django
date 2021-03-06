# Generated by Django 3.2.3 on 2021-05-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolchart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='schoolchart.faculty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='postal_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='certifcate_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolchart.certificate_type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolchart.department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolchart.grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolchart.school'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_of_graduation',
            field=models.IntegerField(),
        ),
    ]
