from django import template

register = template.Library()

#https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
#https://stackoverflow.com/questions/420703/how-do-i-add-multiple-arguments-to-my-custom-template-filter-in-a-django-templat
@register.filter(name='add_css')
def add_css(field, args):
    css = [arg.strip() for arg in args.split(',')]
    return field.as_widget(attrs={'class': css[0], 'placeholder': css[1]})
