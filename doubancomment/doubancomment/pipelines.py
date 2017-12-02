# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class DoubancommentPipeline(object):
    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        fiename = base_dir + '/moviescore/' + item['starname']+"\001".encode('utf-8')+item['id'].encode('utf-8')+'.txt'
        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(fiename, 'a') as f:
            f.write(item['name'].encode('utf-8')+ "\001".encode('utf-8') + item['time'].encode('utf-8') + "\001".encode('utf-8') + item['score'].encode('utf-8') +"\n")
        return item