from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    technologies = models.CharField(
        max_length=300, help_text="Через кому: Django, React, PostgreSQL"
    )
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    github_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-date", "title"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("tooling", "Tooling/DevOps"),
        ("soft", "Soft"),
    ]

    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=50, help_text="0-100")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="soft")

    class Meta:
        ordering = ["-level", "name"]

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class Experience(models.Model):
    position = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        period = f"{self.start_date} — {self.end_date or 'Present'}"
        return f"{self.position} @ {self.company} ({period})"
