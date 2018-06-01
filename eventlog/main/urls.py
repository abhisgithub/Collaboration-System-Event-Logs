from . import eventNameMapping

# This dictionary is used to map the url to the event names
EVENT_NAME_DICT={
    
    # handles community view event
    r'^community-view/(?P<pk>\d+)/$':{
        'GET':{
               'event_name' : 'event.community.view'
        }
    },
    
    #handles article view event
    r'^article-view/(?P<pk>\d*)/$':{
        'GET':{
              'event_name' : 'event.article.view'
        }
    },
    
    #handles article edited, visible, publishable, published events 
    r'^article-edit/(?P<pk>\d*)/$':{
        'POST':{
              'function'   : eventNameMapping.article_event_type,
              'article_edited' : 'event.article.edited',
              'article_visible' : 'event.article.statusChanged',
              'article_publishable' :'event.article.statusChanged',
              'article_published' : 'event.article.published'
        }
    },
}
