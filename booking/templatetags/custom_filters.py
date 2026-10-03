from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, class_name):
    css_classes = field.field.widget.attrs.get('class', '')
    css_classes += f' {class_name}'
    field.field.widget.attrs['class'] = css_classes.strip()
    return field