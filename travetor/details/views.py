from django.shortcuts import render, render_to_response
from details.models import TrekCategory, Trek, Provider, Trek_date
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import RequestContext

def show_category(request, cat_slug):
	try:
		db_category_slug=TrekCategory.objects.get(category_slug=cat_slug)
	except TrekCategory.DoesNotExist:
		raise Http404
	
	treks=db_category_slug.trek_set.all
	return render_to_response('show_category.html',{"treks":treks},)
	

def show_trek(request,cat_slug,tr_slug):
	try:
		db_trek=Trek.objects.get(trek_slug=tr_slug,trek_categories_id__category_slug=cat_slug)
	except Trek.DoesNotExist:
		raise Http404

	return render_to_response('show_trek.html',{"db_trek":db_trek})
	
	'''try:
		db_category_slug=TrekCategory.objects.get(category_slug=cat_slug)
	except TrekCategory.DoesNotExist:
		return render_to_response('aboutus.html', {},
                             context_instance=RequestContext(request))
		raise Http404
	
	try:
		db_trek_slug=db_category_slug.trek_set.get(trek_slug=tr_slug)
	except Trek.DoesNotExist:
		raise Http404

	return render_to_response('show_trek.html',{"db_trek_info":db_trek_slug},)

	if db_trek.trek_categories.category_slug==cat_slug:
		return render_to_response('show_trek.html',{"db_trek":db_trek})
	else:
		render_to_response('show_blog.html')'''

def show_blog(request):
	return render_to_response('show_blog.html')




# Create your views here.
