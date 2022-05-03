from django.db import models


# Create your models here.


class PaddyPurchase(models.Model):
    ref_no = models.IntegerField(primary_key='true')
    token_no = models.CharField(max_length=8)
    agent_name = models.CharField(max_length=20)
    trip_no = models.IntegerField()
    date = models.DateField()
    vehicle_no = models.CharField(max_length=10)
    jute75 = models.IntegerField()  # Bora
    jute40 = models.IntegerField()  # Katta
    plastic40 = models.IntegerField()   # Plastic
    farmer_name = models.CharField(max_length=20)
    farmer_address = models.CharField(max_length=20)
    farm_mob = models.CharField(max_length=10)
    gross_weight = models.IntegerField()
    tier_weight = models.IntegerField()
    gt_weight = models.IntegerField()   # gt_weight = Gross Weight - Tier Weight
    bags_weight = models.IntegerField()  # Bora Weight
    net_weight = models.FloatField()
    loading = models.IntegerField()
    unloading = models.IntegerField()
    unloading_point = models.CharField(max_length=30)
    wb_operator = models.CharField(max_length=10)   # Dharamkanta Operator
    rate = models.IntegerField()
    jute_bags = models.CharField(max_length=12)  # Status of Bardana - Jama OR Le Gaya
    gross_total = models.IntegerField()
    deduction = models.IntegerField()     # Full & Final On Site Payment Deduction
    wb_charges = models.IntegerField()    # Dharamkanta Rate
    lo_unlo_charges = models.IntegerField()   # Hemali
    our_vehicle_charges = models.IntegerField()
    agent_commission = models.IntegerField()
    other_exp = models.IntegerField()
    other_exp_remark = models.CharField(max_length=50)
    advance = models.IntegerField()
    net_total = models.IntegerField()


# For returning data in ADMIN SITE
def __str__(self):
    return self.name
