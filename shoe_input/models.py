#shoe_input/models.py
from django.db import models
from django.contrib.auth.models import User


class Shoe(models.Model):
    SHOE_TYPES = [ 
        ('NIKE SHOX', 'NIKE SHOX'),
        ('TN AIRMAX', 'TN AIRMAX'),
        ('SB.DUNK', 'SB.DUNK'),
        ('PORTAL', 'PORTAL'),
        ('AIRMAX 95', 'AIRMAX 95'),
        ('JORDAN 1', 'JORDAN 1'),
        ('JORDAN 2', 'JORDAN 2'),
        ('JORDAN 3', 'JORDAN 3'),
        ('JORDAN 4', 'JORDAN 4'),
        ('JORDAN 5', 'JORDAN 5'),
        ('JORDAN 6', 'JORDAN 6'),
        ('JORDAN 11', 'JORDAN 11'),
        ('NIKE ZOOM', 'NIKE ZOOM'),
        ('AIRFORCE 1', 'AIRFORCE 1'),
        ('LUIS VUITTON', 'LUIS VUITTON'),
        ('ALEXANDER MC', 'ALEXANDER MC'),
        ('Dr. MARTENS', 'Dr. MARTENS'),        
        ('CONVERSE TYLOR', 'CONVERSE TYLOR'),
        ('VANS KNU', 'VANS KNU'),
        ('ADDIDAS SAMBA', 'ADDIDAS SAMBA'),
        ('NB 530', 'NB 530'),
        ('NB 1000', 'NB 1000'),
        ('NB 740', 'NB 740'),
        ('NB 760', 'NB 760'),
        ('NB 1906R', 'NB 1906R'),
        ('NB 9060 SEASALT', 'NB 9060 SEASALT'),
        ('TIMBERLAND', 'TIMBERLAND'),
        ('ADDIDAS CASUALS', 'ADDIDAS CASUALS'),
        ('REEBOK', 'REEBOK'),
        ('PUMA JOGGER', 'PUMA JOGGER'),
        ('PUMA PARKSTYLE', 'PUMA PARKSTYLE'),
        ('PUMA FENTY', 'PUMA FENTY'),
        ('PUMA SOFT-FOAM', 'PUMA SOFT-FOAM'),
        ('PUMA SUEDE', 'PUMA SUEDE'),
        ('NIKE FASTAGE', 'NIKE FASTAGE'),
        ('TRAVIS SCOTT J1 LOW CUT', 'TRAVIS SCOTT J1 LOW CUT'),
        ('NIKE WORKOUT', 'NIKE WORKOUT'),
        ('DR MARTEWS LOW CUT', 'DR MARTEWS LOW CUT'),
        ('NIKE VOMERO 5', 'NIKE VOMERO 5'),          
       
        
    ]
    
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPES)
    size = models.IntegerField()
    color = models.CharField(max_length=50)
    pieces = models.PositiveIntegerField()
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='shoes/', blank=True, null=True)  

    user_added = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Assuming user ID 1 exists



    def __str__(self):
        return f"{self.shoe_type} - {self.size}"
