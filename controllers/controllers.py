# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class News(http.Controller):
    @http.route([
        '''/news''',
        '''/news/page/<int:page>'''
        ], auth='public', website=True)
    def listing(self, page=0, **kw):
        Posts = http.request.env['trinityroots.news']
        posts_search = Posts.search([])
        posts_count = len(posts_search)
        pager = request.website.pager(url='/news', total=posts_count, page=page, step=8, scope=7, url_args=kw)

        posts_paged = Posts.search([], limit=8, offset=pager['offset'])
        return http.request.render('tr_odoo_news_addon.index', {
            'all_categ': http.request.env['trinityroots.category'].search([]),
            'posts': posts_paged,
            'pager': pager
        })

    @http.route('/news/<model("trinityroots.news"):news>/', auth='public', website=True)
    def read_news(self, news):
        return http.request.render('tr_odoo_news_addon.read_news', {
            'news_obj': news
        })

    @http.route('/news/search/', auth='public', website=True)
    def search_news(self, keyword='', category='all', **kw):
        Posts = http.request.env['trinityroots.news']
        if category == 'all':
            posts_search = Posts.search([('title','ilike',keyword)])
        else:
            posts_search = Posts.search([('title','ilike',keyword), ('category.id','=',category)])
        return http.request.render('tr_odoo_news_addon.search_result', {
            'all_results': posts_search,
            'keyword': keyword,
            'all_categ': http.request.env['trinityroots.category'].search([]),
            'sel_categ': int(category) if category != 'all' else category,
        })

#     @http.route('/news/news/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('news.listing', {
#             'root': '/news/news',
#             'objects': http.request.env['news.news'].search([]),
#         })

#     @http.route('/news/news/objects/<model("news.news"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('news.object', {
#             'object': obj
#         })