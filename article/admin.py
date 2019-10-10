from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
# list_display komutu admin sayfasındaki postlerımızda hangi bilgileri tutacağını belirliyoruz.
    list_display = ["title", "author","created_date"]

# list_display_links komutunda normalde sadece title a tıklayınca gidilen sayfaya nelere tıkladığımızda gideceğimizi belirtiyoruz.
    list_display_links = ["title","author"]

# search_fields komutu arama sekmesi oluşturur ve neye göre arama yapabileceklerimizi belirler.
    search_fields = ["title"]

# sağ tarafta tarihleri ayırmaya yarıyo.Eğer date değilde title dersek yan tarafta title'ları sıralar.
    list_filter = ["created_date"]


#class meta djangonun önerdiği bir classtır başka isim veremiyoruz.
    class Meta:
        model = Article
