from django.db import models

# Define categories once so both classes can use it
CATEGORY_CHOICES = [
    ('engineering', 'Mechanical Engineering'),
    ('welding', 'Welding'),
    ('both', 'Both'),
]

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # Make sure this exists
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class CaseStudy(models.Model):
    CASE_CATEGORY_CHOICES = [
        ('mechanical', 'Mechanical Engineering'),
        ('welding', 'Welding'),
        ('fabrication', 'Fabrication'),
        ('repair', 'Repair & Maintenance'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CASE_CATEGORY_CHOICES)
    client_name = models.CharField(max_length=100, blank=True, help_text="Client name or company")
    location = models.CharField(max_length=200, help_text="Where was the work done?")
    problem = models.TextField(help_text="What was the problem?")
    solution = models.TextField(help_text="How did we solve it?")
    results = models.TextField(blank=True, help_text="What were the results?")
    image = models.ImageField(upload_to='case_studies/', blank=True, null=True)
    before_image = models.ImageField(upload_to='case_studies/before/', blank=True, null=True, help_text="Before fix photo")
    after_image = models.ImageField(upload_to='case_studies/after/', blank=True, null=True, help_text="After fix photo")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']