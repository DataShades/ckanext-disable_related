import ckan.lib.base as base


class DisableRouteController(base.BaseController):
    def not_found(self, *args):
      base.abort(404)
