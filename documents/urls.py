from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^create/$', 'documents.views.create', name='doc_create'),
    url(r'^list/$', 'documents.views.list', name='doc_list'),
    url(r'^get/(?P<doc_id>.+)$', 'documents.views.get', name='doc_get'),
    url(r'^query/(?P<search_string>.+)$', 'documents.views.query', name='doc_query'),
    url(r'^meta/(?P<doc_id>.+)$', 'documents.views.meta', name='doc_meta'),

    url(r'^import/list/$', 'documents.views.importList', name='doc_list'),
    url(r'^import/get/(?P<doc_id>.+)$', 'documents.views.importGet', name='doc_get'),
    url(r'^import/query/(?P<search_string>.+)$', 'documents.views.importQuery', name='doc_query'),
    url(r'^import/meta/(?P<doc_id>.+)$', 'documents.views.importMeta', name='doc_meta'),
)