import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import _
from routes.mapper import SubMapper

import logging
log = logging.getLogger(__name__)


class Disable_RelatedPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IRoutes, inherit=True)

    _controller = 'ckanext.disable_related.controller:DisableRouteController'

    # IAuthFunctiona

    def _auth_deny_related(self, context, data_dict=None):
      return {
        'success': False,
        'msg': _('This feature is currently disabled')
        }

    def get_auth_functions(self):
      return {
        'related_create': self._auth_deny_related,
        'related_show': self._auth_deny_related,
        'related_delete': self._auth_deny_related,
        'related_update': self._auth_deny_related,
        'related_create': self._auth_deny_related,
        }

    # IRoutes

    def before_map(self, map):
        with SubMapper(map, controller=self._controller) as m:
            m.connect('related_new',
                      '/dataset/{id}/related/new',
                      action='not_found')
            m.connect('related_edit',
                      '/dataset/{id}/related/edit/{related_id}',
                      action='not_found')
            m.connect('related_delete',
                      '/dataset/{id}/related/delete/{related_id}',
                      action='not_found')
            m.connect('related_list',
                      '/dataset/{id}/related',
                      action='not_found')
            m.connect('related_read',
                      '/related/{id}',
                      action='not_found')
            m.connect('related_dashboard',
                      '/related',
                      action='not_found')
        return map

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'disable_related')
