from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Diego",
        "date": date(2024, 9, 23),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view ",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Diego",
        "date": date(2024, 9, 11),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view ",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Diego",
        "date": date(2024, 9, 20),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst i was enjoying the view ",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia molestias modi esse, blanditiis ullam sapiente facere totam maiores corrupti qui optio officia, sequi laudantium ad facilis. Nemo nam dicta deserunt!
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.



def starting_page(request):
    sorted_posts = all_posts.sort(key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")