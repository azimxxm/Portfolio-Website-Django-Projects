from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=50, verbose_name="User Name")
    images = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Photo")
    about_me = models.TextField(max_length=300, verbose_name="Description")
    html = models.IntegerField(default=0, null=True, verbose_name="HTML")
    css = models.IntegerField(default=0, null=True, verbose_name="CSS")
    javascript = models.IntegerField(default=0, null=True, verbose_name="JavaScript")
    python = models.IntegerField(default=0, null=True, verbose_name="PYTHON")
    postgresql = models.IntegerField(default=0, null=True, verbose_name="POSTGRSQL")
    photoshoop = models.IntegerField(default=0, null=True, verbose_name="ABODE PHOTOSHOOP")
    photographer = models.IntegerField(default=0, null=True, verbose_name="PHOTOGRAPHER")
    mysql = models.IntegerField(default=0, null=True, verbose_name="MySQL")
    mongoDB = models.IntegerField(default=0, null=True, verbose_name="MongoDB")
    reactjs = models.IntegerField(default=0, null=True, verbose_name="ReactJS")
    nextjs = models.IntegerField(default=0, null=True, verbose_name="NextJS")
    vuejs = models.IntegerField(default=0, null=True, verbose_name="VueJS")
    i18next_community = models.IntegerField(default=0, null=True, verbose_name="I18next Translator")


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "User Skill"
        verbose_name_plural = "User Skill"
