from django.db import models

# Create your models here.
class NextTrackingNumber(models.Model):
    customer_id = models.UUIDField(max_length=255, db_index=True)
    customer_name = models.CharField(max_length=250,)
    weight = models.FloatField()
    customer_slug = models.CharField(max_length=250)
    origin_country_id = models.IntegerField()
    destination_country_id = models.IntegerField(db_index=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    
    def __str__(self):
        return self.customer_name