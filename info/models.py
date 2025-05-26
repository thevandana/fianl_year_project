from django.db import models

class news_table(models.Model):
    title = models.TextField()
    des = models.TextField()
    category = models.TextField()
    pub_draft = models.BooleanField()
    youtube_link = models.URLField(max_length=300,null=True)
    date = models.DateField(null=False , blank=False)
    time = models.TimeField(null=False , blank=False)
    image = models.ImageField(null=True,blank=True,upload_to='')
   # subscribe = models.EmailField(max_length=250,null=True,blank=True)


class comments(models.Model):
    post_id = models.ForeignKey(news_table,on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=250)
    mob_no = models.TextField(max_length=20)
    comment = models.TextField()
    date_time = models.DateTimeField()


class news_letter(models.Model):
    date_time = models.DateTimeField()
    email = models.EmailField()

class ads(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    ad_image = models.ImageField(null=True,blank=True,upload_to='')
    ad_url = models.URLField()

# class tranding(models.Model):
#      post_id = models.ForeignKey(news_table, on_delete=models.CASCADE)

class addcategory(models.Model):
    category_name = models.TextField(max_length=100)
    cat_dec = models.TextField()

