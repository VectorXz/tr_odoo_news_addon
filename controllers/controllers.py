# -*- coding: utf-8 -*-
from odoo import http

class News(http.Controller):
    @http.route('/news/', auth='public', website=True)
    def index(self, **kw):
        Posts = http.request.env['trinityroots.news']
        return http.request.render('news.index', {
            'posts': Posts.search([])
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