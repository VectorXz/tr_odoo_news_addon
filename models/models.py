# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

# class news(models.Model):
#     _name = 'news.news'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class News(models.Model):
    _name="trinityroots.news"
    _description="News"
    _rec_name = 'title'

    #find default category
    def _default_category(self):
        return self.env['trinityroots.category'].search([('name', '=', 'Uncategorized')], limit=1).id

    #find_posts_number
    def _count_posts(self):
        Posts = self.env['trinityroots.news'].search([])
        _logger.debug("This is my debug message ! ")
        _logger.debug("LENGTH : "+str(len(Posts)))
        if len(Posts) == 0:
            _logger.debug("True ! ")
            return True
        else:
            _logger.debug("False ! ")
            return False

    #Fields
    title = fields.Char(string="Title", required=True)
    writer = fields.Many2one('res.users', string="Write by", index=True, default=lambda self: self.env.user)
    poster = fields.Many2one('res.users', string="Post by", index=True, default=lambda self: self.env.user)
    content = fields.Html()
    image = fields.Binary()
    category = fields.Many2one('trinityroots.category', string="Category", default=_default_category)
    publish = fields.Boolean("Publish", default=True)

class Category(models.Model):
    _name="trinityroots.category"
    _description="Category"

    #Fields
    image = fields.Binary()
    name = fields.Char(string="Name", required=True)
    publish = fields.Boolean("Publish", default=True)

    # To change all posts in this category to have the same publish value
    def write(self, values):
        res = super(Category, self).write(values)
        all_news = self.env['trinityroots.news'].search([('category', '=', [self.name])])
        for news in all_news:
            news.publish = self.publish
        return res