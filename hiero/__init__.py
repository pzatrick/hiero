from hiero.interfaces   import IHieroEntryClass
from hiero.interfaces   import IHieroSeriesClass
from hiero.interfaces   import IHieroCategoryClass

from hem.config         import get_class_from_config

def includeme(config):
    settings = config.registry.settings

    if not config.registry.queryUtility(IHieroEntryClass):
        entry_class = get_class_from_config(settings, 'hiero.entry_class')
        config.registry.registerUtility(entry_class, IHieroEntryClass)

    if not config.registry.queryUtility(IHieroSeriesClass):
        series_class = get_class_from_config(settings, 'hiero.series_class')
        config.registry.registerUtility(series_class, IHieroSeriesClass)

    if not config.registry.queryUtility(IHieroCategoryClass):
        cat_class = get_class_from_config(settings, 'hiero.category_class')
        config.registry.registerUtility(cat_class, IHieroCategoryClass)

    config.include('hiero.routes')

 #   config.add_route('get_pages',   '/pages') 
 #   config.add_route('get_page',    '/pages/{link_title}')
 #   config.add_route('edit_page',   '/pages/{link_title}/edit')
 #   config.add_route('add_page',    '/add_page')
 #   config.add_route('remove_page', '/pages/{link_title}/remove')
    config.add_subscriber(add_renderer_globals, 'pyramid.events.BeforeRender')
    config.scan()
    return config.make_wsgi_app()


def add_renderer_globals(event):
  event['stylesheet_link_tag'] = stylesheet_link_tag
  event['script_tag'] = script_tag

def stylesheet_link_tag(request, url):
  full_url = request.static_url("hiero:static%s" % url)
  return "<link rel=\"stylesheet\" href=\"%s\" type=\"text/css\" media=\"screen\" charset=\"utf-8\" />" % full_url

def script_tag(request, url):
  full_url = request.static_url("hiero:static%s" % url)
  return "<script type=\"text/javascript\" src=\"%s\" charset=\"utf-8\" ></script>" % full_url

