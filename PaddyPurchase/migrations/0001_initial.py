# Generated by Django 4.0.4 on 2022-05-02 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaddyPurchase',
            fields=[
                ('ref_no', models.IntegerField(primary_key='true', serialize=False)),
                ('token_no', models.CharField(max_length=8)),
                ('agent_name', models.CharField(max_length=20)),
                ('trip_no', models.IntegerField()),
                ('date', models.DateField()),
                ('vehicle_no', models.CharField(max_length=10)),
                ('jute75', models.IntegerField()),
                ('jute40', models.IntegerField()),
                ('plastic40', models.IntegerField()),
                ('farmer_name', models.CharField(max_length=20)),
                ('farmer_address', models.CharField(max_length=20)),
                ('farm_mob', models.CharField(max_length=10)),
                ('gross_weight', models.IntegerField()),
                ('tier_weight', models.IntegerField()),
                ('gt_weight', models.IntegerField()),
                ('bags_weight', models.IntegerField()),
                ('net_weight', models.FloatField()),
                ('loading', models.IntegerField()),
                ('unloading', models.IntegerField()),
                ('unloading_point', models.CharField(max_length=30)),
                ('wb_operator', models.CharField(max_length=10)),
                ('rate', models.IntegerField()),
                ('jute_bags', models.CharField(max_length=12)),
                ('gross_total', models.IntegerField()),
                ('deduction', models.IntegerField()),
                ('wb_charges', models.IntegerField()),
                ('lo_unlo_charges', models.IntegerField()),
                ('our_vehicle_charges', models.IntegerField()),
                ('agent_commission', models.IntegerField()),
                ('other_exp', models.IntegerField()),
                ('other_exp_remark', models.CharField(max_length=50)),
                ('advance', models.IntegerField()),
                ('net_total', models.IntegerField()),
            ],
        ),
    ]
