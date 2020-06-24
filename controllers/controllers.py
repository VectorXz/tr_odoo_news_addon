# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class News(http.Controller):
    @http.route([
        '''/news''',
        '''/news/page/<int:page>'''
        ], auth='public', website=True)
    def index(self, page=0, **kw):
        Posts = http.request.env['trinityroots.news']
        posts_search = Posts.search([])
        posts_count = len(posts_search)
        pager = request.website.pager(url='/news', total=posts_count, page=page, step=8, scope=7, url_args=kw)

        posts_paged = Posts.search([], limit=8, offset=pager['offset'])
        return http.request.render('news.index', {
            'posts': posts_paged,
            'pager': pager
        })

    @http.route('/news/<model("trinityroots.news"):news>/', auth='public', website=True)
    def teacher(self, news):
        return http.request.render('news.read_news', {
            'news_obj': news
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