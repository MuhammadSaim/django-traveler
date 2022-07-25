from django import template

register = template.Library()


def rating(value):
    if value >= 4.5:
        return "Excellent"
    if value >= 3.5:
        return "Very Good"
    if value >= 2.5:
        return "Good"
    if value >= 2:
        return "Average"
    if value >= 1.5:
        return "Bad"
    if value < 1.5:
        return "Very Bad"


def div(value, arg):
    return value / arg


register.filter('rating', rating)
register.filter('div', div)
