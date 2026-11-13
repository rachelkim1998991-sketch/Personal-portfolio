from django.db import models


class Skill(models.Model):
    name = models.CharField("Nomi", max_length=50)
    category = models.CharField(
        "Toifa", max_length=30, default="Backend",
        help_text="Masalan: Backend, Frontend, DevOps, Tools",
    )
    order = models.PositiveSmallIntegerField("Tartib", default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField("Nomi", max_length=120)
    description = models.TextField("Tavsif")
    technologies = models.CharField(
        "Texnologiyalar", max_length=200,
        help_text="Vergul bilan: Django, PostgreSQL, Docker",
    )
    github_url = models.URLField("GitHub havolasi", blank=True)
    demo_url = models.URLField("Demo havolasi", blank=True)
    image = models.ImageField("Rasm", upload_to="projects/", blank=True)
    order = models.PositiveSmallIntegerField("Tartib", default=0)
    is_published = models.BooleanField("Ko'rsatilsin", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [t.strip() for t in self.technologies.split(",") if t.strip()]


class Message(models.Model):
    name = models.CharField("Ism", max_length=100)
    email = models.EmailField("Email")
    text = models.TextField("Xabar")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField("O'qildi", default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.email})"
