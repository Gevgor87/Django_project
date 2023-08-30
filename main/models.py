from django.db import models

# Create your models here.

class HomeBgInfo(models.Model):
    title = models.CharField("HomeBgInfo title", max_length=200)
    title_info = models.CharField("HomeBgInfo title_info", max_length=200)
    info = models.CharField("HomeBgInfo Info_text", max_length=500)
    button_name = models.CharField("HomeBgInfo Button", max_length=50)

    def __str__(self) -> str:
        return self.title
    
class HomeImg(models.Model):
    img = models.ImageField("Home image", upload_to="images")
    price = models.PositiveIntegerField("Home price")
    discount = models.PositiveIntegerField("Home discount")

class HeadBg(models.Model):
    logo = models.ImageField("HeadBg logo", upload_to="images")
    bg = models.ImageField("HeadBg bg", upload_to="images")

class Icon(models.Model):
    icon_png = models.ImageField("Icon png", upload_to="images")
    title = models.CharField("Icon title", max_length=20)

    def __str__(self) -> str:
        return self.title

class GameCat(models.Model):
    cat = models.CharField("Game category", max_length=50)

    def __str__(self) -> str:
        return self.cat

class TrendingGame(models.Model):
    gamecat = models.ForeignKey("GameCat", on_delete=models.CASCADE, related_name="game_cat")
    image = models.ImageField("Trending Games image", upload_to="images")
    name = models.CharField("Trending Games name", max_length=60)
    category = models.CharField("Trending Games category", max_length=50)
    old_price = models.PositiveIntegerField("Trending Games old price")
    new_price = models.PositiveIntegerField("Trending Games")
    about = models.TextField("About game")
    tags = models.CharField("TrendingGames tags", max_length=50)
    reviews = models.TextField("TG Reviews")

class Cart(models.Model):
    prod_item = models.ForeignKey("TrendingGame", on_delete=models.CASCADE, related_name="cart_item")


class MostPlayed(models.Model):

    image = models.ImageField("Trending Games image", upload_to="images")
    name = models.CharField("Trending Games name", max_length=60)
    category = models.CharField("Trending Games category", max_length=50)
    old_price = models.PositiveIntegerField("Trending Games old price")
    new_price = models.PositiveIntegerField("Trending Games")
    about = models.TextField("About game")
    tags = models.CharField("TrendingGames tags", max_length=50)
    reviews = models.TextField("TG Reviews")

class Category(models.Model):
    image = models.ImageField("Category image", upload_to="images")
    cat_name = models.CharField("Category name", max_length=50)

class Title_1(models.Model):
    sub = models.CharField("Title 1 sub", max_length=50)
    title = models.CharField("Title 1 title", max_length=50)

    def __str__(self) -> str:
        return self.title

class Title_2(models.Model):
    sub = models.CharField("Title 2 sub", max_length=50)
    title = models.CharField("Title 2 title", max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Title_3(models.Model):
    sub = models.CharField("Title 3 sub", max_length=50)
    title = models.CharField("Title 3 title", max_length=50)

    def __str__(self) -> str:
        return self.title

class Food_1(models.Model):
    title = models.CharField("Food 1 title", max_length=30)
    text_1 = models.CharField("Food 1 t_1", max_length=60)
    text_2 = models.CharField("Food 1 t_2", max_length=60)
    text_3 = models.CharField("Food 1 t_3", max_length=60)
    p = models.CharField("Food 1 p", max_length=200)
    button = models.CharField("Food 1 button", max_length=20)

    def __str__(self) -> str:
        return self.title


class Food_2(models.Model):
    title = models.CharField("Food 2 title", max_length=30)
    text_1 = models.CharField("Food 2 t_1", max_length=60)
    text_2 = models.CharField("Food 2 t_2", max_length=60)
    text_3 = models.CharField("Food 2 t_3", max_length=60)
    button = models.CharField("Food 2 button", max_length=20)

    def __str__(self) -> str:
        return self.title

class Footer(models.Model):
    text_1 = models.CharField("Footer text 1", max_length=200)
    text_2 = models.CharField("Footer text 2", max_length=200)
    link = models.URLField("Footer URL")

class Shop_cat(models.Model):
    cat = models.CharField("Shop category", max_length=20)

class Contact(models.Model):
    sub = models.CharField("Contact subtitle", max_length=50)
    title = models.CharField("Contact title", max_length=50)
    p = models.TextField("Contact text")
    address = models.CharField("Contact address", max_length=200)
    phone = models.PositiveIntegerField("Contact phone")
    email = models.EmailField("Contact Email")

class ContackPost(models.Model):

    name = models.CharField("User name", max_length=100)
    surname = models.CharField("User surname", max_length=100)
    email = models.EmailField("Usen email")
    subject = models.CharField("User subject", max_length=100)
    message = models.TextField("User text")



