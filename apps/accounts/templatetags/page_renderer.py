from django import template
register = template.Library()

@register.inclusion_tag('_pagination.html')
def render_paginator(object_list):
	return {'object_list': object_list}

@register.inclusion_tag('_featured.html')
def render_featured(object_list):
	return {'object_list': object_list}