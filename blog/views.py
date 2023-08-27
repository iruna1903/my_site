from datetime import date

from django.shortcuts import render

all_posts = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpq",
    "author": "Iryna",
    "date": date(2023, 8, 25),
    "title": "Mountain Hiking",
    "excerpt": " There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    "content": "The aroma of coffee wafted from the cafe, enticing passersby to step in for a warm cup on a chilly morning."
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render (request, "blog/posts-detail.html")
