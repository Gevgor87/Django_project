from django.shortcuts import render, redirect
from .models import (HomeBgInfo, HomeImg, HeadBg, Icon, TrendingGame, MostPlayed, Category, Title_1, Title_2, Title_3, 
                     Food_1, Food_2, Footer, Shop_cat, GameCat, Contact, ContackPost, Cart)

# Create your views here.

def index(request):
    home_bginfo = HomeBgInfo.objects.all()[0]
    home_img = HomeImg.objects.all()[0]
    head_bg = HeadBg.objects.all()[0]
    icon = Icon.objects.all()
    trending_games = GameCat.objects.all()[0]
    most_played = GameCat.objects.all()[1]
    category = Category.objects.all()
    title_1 = Title_1.objects.all()[0]
    title_2 = Title_2.objects.all()[0]
    title_3 = Title_3.objects.all()[0]
    food_1 = Food_1.objects.all()[0]
    food_2 = Food_2.objects.all()[0]
    footer = Footer.objects.all()[0]


    return render(request, 'index.html', context={
        "home_bginfo": home_bginfo,
        "home_img": home_img,
        "head_bg": head_bg,
        "icon": icon,
        "trending_games": trending_games,
        "most_played": most_played,
        "category": category,
        "title_1": title_1,
        "title_2": title_2,
        "title_3": title_3,
        "food_1": food_1,
        "food_2": food_2,
        "footer": footer,
        "link":"index"

    })


def product_details(request, id):
    my_prod = TrendingGame.objects.get(pk = id)
    title_3 = Title_3.objects.all()[0]
    category = Category.objects.all()
    footer = Footer.objects.all()[0]
    head_bg = HeadBg.objects.all()[0]

    return render(request, 'product-details.html', context={
        "my_prod": my_prod,
        "title_3": title_3,
        "category": category,
        "footer": footer,
        "head_bg": head_bg,
    


    })


def shop(request):
    shop_cat = Shop_cat.objects.all()
    trending_games = TrendingGame.objects.all()
    most_played = MostPlayed.objects.all()
    footer = Footer.objects.all()[0]
    head_bg = HeadBg.objects.all()[0]

    return render(request, 'shop.html', context={
        "shop_cat": shop_cat,
        "trending_games": trending_games,
        "most_played": most_played,
        "footer": footer,
        "head_bg": head_bg,
        "link":"shop"
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        ContackPost.objects.create(name = name, surname = surname, email = email, subject = subject, message = message)
        return redirect("index")

    footer = Footer.objects.all()[0]
    head_bg = HeadBg.objects.all()[0]
    contacts = Contact.objects.all()[0]

    return render(request, 'contact.html', context={
        "footer": footer,
        "head_bg": head_bg,
        "contacts": contacts,
        "link":"contact"

    })

def basket(request):
    footer = Footer.objects.all()[0]
    head_bg = HeadBg.objects.all()[0]
    summ = 0
    if request.method == "POST":
        prod_id = request.POST.get('id')
        my_product = TrendingGame.objects.get(id = prod_id)
        Cart.objects.create(prod_item = my_product)
        return redirect('shop')
    cart_list = Cart.objects.all()
    for i in cart_list:
        summ+= i.prod_item.new_price

    return render(request, 'basket.html', context={
        "footer": footer,
        "head_bg": head_bg,
        "cart_list": cart_list,
        "summ": summ,
    })

def delete_product(request):
    if request.method == "POST":
        prod_id = request.POST.get("id")
        Cart.objects.filter(id = prod_id).delete()
        return redirect('basket')