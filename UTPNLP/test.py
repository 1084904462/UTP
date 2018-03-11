# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
import json
import jieba
import db_helper
import re
import nlp


SIMILARITY_THRESHOLD_LIST = (0, 0.2, 0.3, 0.2, 0.2, 0.2)  # 相似度阈值可以改成数组，不同的内容相似度阈值可以设置成不同
keywords = {1: "招标单位", 2: "中标单位", 3: "主要内容", 4: "公告时间", 5: "中标金额"}
num = 7
test_keyword_id = 2


def test():
    item = read_item()
    values = []
    print(item['detail'])
    print("_______________________________________________________________")
    keyword_id_list = db_helper.get_keyword_ids(1)
    for (keyword_id,) in keyword_id_list:
        patterns = db_helper.get_patterns(keyword_id)
        pattern_list = []
        for (gain_word, pre_pattern, gain_pattern, aft_pattern) in patterns:
            pattern = ""
            if gain_word is not None:
                for word in gain_word:
                    if word == '\\':
                        pattern += word
                    else:
                        pattern += word + " *"
            if pre_pattern is not None:
                pattern += pre_pattern
            if gain_pattern is not None:
                pattern += gain_pattern
            if aft_pattern is not None:
                pattern += aft_pattern
            pattern_list.append(pattern)
        value = nlp.parse(item, "|".join(pattern_list))
        for i in value:
            value = (keyword_id, i)
            values.append(value)   # 根据正则获取的结果
    keyword_ids, raw_documents = nlp.get_corpus(1)
    ans_list = nlp.check_in_corpus(keyword_ids, raw_documents, values)
    print("最终结果:", ans_list)


def test_single():
    item = read_item()
    values = []
    patterns = db_helper.get_patterns(test_keyword_id)
    pattern_list = []
    for (gain_word, pre_pattern, gain_pattern, aft_pattern) in patterns:
        pattern = ""
        if gain_word is not None:
            for word in gain_word:
                if word == '\\':
                    pattern += word
                else:
                    pattern += word + " *"
        if pre_pattern is not None:
            pattern += pre_pattern
        if gain_pattern is not None:
            pattern += gain_pattern
        if aft_pattern is not None:
            pattern += aft_pattern
        # print(pattern)
        pattern_list.append(pattern)
    value = nlp.parse(item, "|".join(pattern_list))
    for i in value:
        value = (test_keyword_id, i)
        print(value)
        values.append(value)   # 根据正则获取的结果
    keyword_ids, raw_documents = nlp.get_corpus(1)
    ans_list = []
    tfidf = models.TfidfModel.load("tfidf.txt")
    dictionary = corpora.Dictionary.load("dictionary.txt")
    similarity = similarities.MatrixSimilarity.load("similarity.txt")
    for (id, content) in values:
        new_doc = content
        new_vec = dictionary.doc2bow(jieba.cut(new_doc, cut_all=False))
        new_vec_tfidf = tfidf[new_vec]
        sims = similarity[new_vec_tfidf]
        sims_list = []
        for sim in sims:
            sims_list.append(sim)
        keyword_ids_list = []
        for i in sims_list:
            if i > SIMILARITY_THRESHOLD_LIST[test_keyword_id]:
                keyword_ids_list.append(keyword_ids[sims_list.index(i)])
                print("相似度：", i, "关键词ID：", keyword_ids[sims_list.index(i)])
        print(keyword_ids_list)
        if test_keyword_id in keyword_ids_list:
            ans = (test_keyword_id, content)
            ans_list.append(ans)


def read_item():
    i = 0
    item = {}
    utp_file = open("../UTPSpider/UTPSpider/utp.json", 'r', encoding="utf-8")
    for line in utp_file.readlines():
        if i == num:
            item = json.loads(line)
        i = i + 1
    return item


if __name__ == '__main__':
    test()
    print("_______________________________________________________________")
    test_single()
