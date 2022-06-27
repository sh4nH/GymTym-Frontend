# Generated by Django 3.0.14 on 2022-06-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeslots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpshtraffic',
            name='fri',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='mon',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='sat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='sun',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='thu',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='tue',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpshtraffic',
            name='wed',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='fri',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='mon',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='sat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='sun',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='thu',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='tue',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='numberofreadings',
            name='wed',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='fri',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='mon',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='sat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='sun',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='thu',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='tue',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usctraffic',
            name='wed',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='fri',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='mon',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='sat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='sun',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='thu',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='tue',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='uttraffic',
            name='wed',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='fri',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='mon',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='sat',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='sun',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='thu',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='tue',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='wellnesstraffic',
            name='wed',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
