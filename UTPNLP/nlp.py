# -*- coding: utf-8 -*-

from gensim import corpora, models, similarities
import jieba
import re
import json
import db_helper

MAIN_TEXT_SUM = 400
SIMILARITY_THRESHOLD_LIST = (0, 0.2, 0.3, 0.2, 0.2, 0.2)  # 相似度阈值可以改成数组，不同的内容相似度阈值可以设置成不同


def say():
    print("hello")


def process_nlp():
    utp_text = read_text()
    for item in utp_text:
        if len(item['detail']) < MAIN_TEXT_SUM:
            continue
        values = []
        model_id = db_helper.get_model_id()     # 确定使用哪种模型
        keyword_id_list = db_helper.get_keyword_ids(model_id)   # 查询该模型的所有关键词
        for (keyword_id,) in keyword_id_list:   # 查询每个关键词对应的正则
            patterns = db_helper.get_patterns(keyword_id)
            pattern_list = []
            for (gain_word, pre_pattern, gain_pattern, aft_pattern) in patterns:
                pattern = ""
                if gain_word is not None:
                    pattern += " *".join(word for word in gain_word if word != '\\')
                if pre_pattern is not None:
                    pattern += pre_pattern
                if gain_pattern is not None:
                    pattern += gain_pattern
                if aft_pattern is not None:
                    pattern += aft_pattern
                pattern_list.append(pattern)
            value = parse(item, "|".join(pattern_list))
            for i in value:
                value = (keyword_id, i)
                values.append(value)   # 根据正则获取的结果
        keyword_ids, raw_documents = get_corpus(1)
        ans_list = check_in_corpus(keyword_ids, raw_documents, values)
        print("---------------", ans_list, "---------------")
        # db_helper.insert_in(item, ans_list)


def read_text():
    utp_file = open("../UTPSpider/UTPSpider/utp.json", 'r', encoding="utf-8")
    utp_text = [json.loads(line) for line in utp_file.readlines()]
    return utp_text


def parse(item, patterns):
    pattern = re.compile(patterns, re.DOTALL)
    results = pattern.findall(item["detail"])
    content_list = []
    for result in results:
        content_list += result
    while "" in content_list:
        content_list.remove("")
    new_content_list = []
    [new_content_list.append(i) for i in content_list if i not in new_content_list]
    return new_content_list


def check_in_corpus(keyword_ids, raw_documents, values):
    ans_list = []
    tfidf = models.TfidfModel.load("tfidf.txt")
    dictionary = corpora.Dictionary.load("dictionary.txt")
    similarity = similarities.MatrixSimilarity.load("similarity.txt")
    for (keyword_id, content) in values:
        # print("__________________________________________")
        new_doc = content
        new_vec = dictionary.doc2bow(jieba.cut(new_doc, cut_all=False))
        new_vec_tfidf = tfidf[new_vec]
        sims = similarity[new_vec_tfidf]
        sims_list = []
        for sim in sims:
            sims_list.append(sim)
        keyword_ids_list = []
        for i in sims_list:
            if i > SIMILARITY_THRESHOLD_LIST[keyword_id]:
                keyword_ids_list.append(keyword_ids[sims_list.index(i)])
                # print("相似度：", i, "关键词ID：", keyword_ids[sims_list.index(i)], "对应文本：", raw_documents[sims_list.index(i)])
        if keyword_id in keyword_ids_list:
            ans = (keyword_id, content)
            ans_list.append(ans)
        # print("__________________________________________")
    return ans_list


def get_corpus(model_id):
    items = db_helper.get_contents(model_id)
    raw_documents = [item for (keyword_id, item,) in items]
    keyword_ids = [keyword_id for (keyword_id, item,) in items]
    texts = [[word for word in jieba.cut(document, cut_all=False)] for document in raw_documents]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    similarity = similarities.MatrixSimilarity(corpus_tfidf)
    tfidf.save("tfidf.txt")
    dictionary.save("dictionary.txt")
    similarity.save("similarity.txt")
    return keyword_ids, raw_documents


def format_text(text):
    text = text.replace("\n\n", "\n")
    words = db_helper.get_separator()
    for (word,) in words:
        word_re = re.compile("[0123456789一二三四五六七八九十\.。、（）\(\) ]*" + word)
        text = re.sub(word_re, "\n\n" + word, text)
    return text


if __name__ == '__main__':
    process_nlp()
