from django import template
from ..models import Article
from datetime import datetime

register = template.Library()

@register.simple_tag
def total_articles():
    return Article.publish.count()

@register.filter(name="isnew")
def time_calculate(value):
    created_date = value.strftime("%d %m %y")
    now_date = datetime.now().strftime("%d %m %y")
    created_date_prime = datetime.strptime(created_date, "%d %m %y")
    now_date_prime = datetime.strptime(now_date, "%d %m %y")
    return (now_date_prime - created_date_prime).days < 7