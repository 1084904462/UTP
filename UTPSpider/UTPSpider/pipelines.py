# -*- coding: utf-8 -*-

import json
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".." + "/UTPNLP"))
import nlp


class JsonPipeline(object):
    def __init__(self):
        self.file = open('utp.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item['detail'] = nlp.format_text(item['detail'])
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()
        nlp.process_nlp()
