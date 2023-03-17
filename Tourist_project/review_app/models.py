from django.db import models
from msilib.schema import Condition


# Create your models here.
class cdf_mumbai(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_mumbai'
        
class cdf_agra(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_agra'

class cdf_ahmedabad(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_ahmedabad'

class cdf_bangalore(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_bangalore'

class cdf_chandigarh(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_chandigarh'

class cdf_delhi(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_delhi'

class cdf_goa(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_goa'

class cdf_jaipur(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_jaipur'

class cdf_kolkata(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_kolkata'

class cdf_pune(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_pune'

class cdf_udaipur(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_udaipur'

class cdf_varanasi(models.Model):
    
    city_name     = models.CharField(max_length=30)
    place_to_visit     = models.CharField(max_length=30)
    place_name      = models.CharField(max_length=30)
    avg_scoreR        = models.IntegerField()
    

    class Meta:
        app_label = 'review_app'
        db_table='cdf_varanasi'