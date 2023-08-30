from django.contrib import admin
from .models import (HomeBgInfo, HomeImg, HeadBg, Icon, TrendingGame, MostPlayed, Category, 
                     Title_1, Title_2, Title_3, Food_1, Food_2, Footer, Shop_cat, GameCat, Contact, 
                     ContackPost, Cart)

# Register your models here.

@admin.register(HomeBgInfo)
class HomeBgInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]

admin.site.register(GameCat)

@admin.register(TrendingGame)
class TrendingGameAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "new_price"]
    list_display_links = ["id", "name", "new_price"]
    search_fields = ["name", "new_price"]

@admin.register(MostPlayed)
class MostPlayedAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "new_price"]
    list_display_links = ["id", "name", "new_price"]
    search_fields = ["name", "new_price"]

@admin.register(Title_1)
class Title_1Admin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]

@admin.register(Title_2)
class Title_2Admin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]

@admin.register(Title_3)
class Title_3Admin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]

@admin.register(Shop_cat)
class Shop_catAdmin(admin.ModelAdmin):
    list_display = ["id", "cat"]
    list_display_links = ["id", "cat"]
    search_fields = ["cat"]

admin.site.register(HomeImg)
admin.site.register(HeadBg)
admin.site.register(Category)
admin.site.register(Food_1)
admin.site.register(Food_2)
admin.site.register(Footer)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "phone", "email"]
    list_display_links = ["id", "phone", "email"]
    search_fields = ["phone", "email"]

@admin.register(ContackPost)
class ContactPostAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    list_display_links = ["id", "name", "email"]
    search_fields = ["name", "email"]

admin.site.register(Cart)












