from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title + " - " + str(self.pub_date)

    def summary(self):
        return self.body[:100]

    def pub_date_truncated(self):
        return self.pub_date.strftime("%e %b %Y")
