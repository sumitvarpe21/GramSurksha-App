from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Issue(models.Model):
    CATEGORY_CHOICES = [
        ('waste', 'Waste'),
        ('accident', 'Accident'),
        ('crime', 'Crime'),
        ('animal', 'Animal Threat'),
        ('road', 'Road Damage'),
        ('water', 'Water Issue'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='issues/')
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class StatusUpdate(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)


from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='profile_photos/', default='default.png')
    is_admin = models.BooleanField(default=False)   # ADD THIS


    def __str__(self):
        return f"{self.user.username} - {self.points} points"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # For existing users, create profile if missing
        if not hasattr(instance, 'userprofile'):
            UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Issue)
def reward_points_on_completion(sender, instance, **kwargs):
    if instance.status == "Completed":
        profile = instance.user.userprofile
        profile.points += 10
        profile.save()