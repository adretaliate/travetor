from details.models import Trek, TrekCategory
from travetor import settings

def travetor(request):
	return{
	'active adventure categories':TrekCategory.objects.filter(is_active=True),
	'active treks':Trek.objects.filter(is_active=True),
	'site_name':settings.SITE_NAME,
	'meta_keywords':settings.META_KEYWORDS,
	'meta_description':settings.META_DESCRIPTION,
	'request':request
	}
