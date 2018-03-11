package org.obsidian.utp.service.impl;

import org.obsidian.utp.bean.ContentBean;
import org.obsidian.utp.bean.DocBean;
import org.obsidian.utp.dao.ContentMapper;
import org.obsidian.utp.dao.DocMapper;
import org.obsidian.utp.entity.Content;
import org.obsidian.utp.entity.ContentExample;
import org.obsidian.utp.entity.Doc;
import org.obsidian.utp.service.ContentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by BillChen on 2018/2/9.
 */
@Service
@CacheConfig(cacheNames = "content")
public class ContentServiceImpl implements ContentService {
    @Autowired
    private ContentMapper contentMapper;

    @Autowired
    private DocMapper docMapper;

    @Cacheable("allContent")
    @Override
    public List<Content> selectAllContent() {
        ContentExample example = new ContentExample();
        return contentMapper.selectByExample(example);
    }

    @CacheEvict(value = {"allContent"}, allEntries = true)
    @Override
    public int updateContent(Long id, Long keywordId, String content) {
        Content content1 = new Content();
        content1.setId(id);
        content1.setKeywordId(keywordId);
        content1.setContent(content);
        ContentExample example = new ContentExample();
        example.or().andIdEqualTo(id);
        return contentMapper.updateByExample(content1,example);
    }

    @Transactional
    @Override
    public List<ContentBean> selectByDocId(Long docId) {
        List<ContentBean> contentBeanList = contentMapper.selectByDocId(docId);
        if(contentBeanList.isEmpty()){
            return null;
        }
        return contentBeanList;
    }

    @Transactional
    @Override
    public List<Doc> selectDoc(Long startId, Long endId) {
        List<Doc> docList = docMapper.selectDocList(startId,endId);
        if(docList.isEmpty()){
            return null;
        }
        return docList;
    }

    @Transactional
    @Override
    public List<DocBean> getDocBeanList(Long startId, Long endId) {
        List<DocBean> docBeanList = new ArrayList<>();
        List<Doc> docList = this.selectDoc(startId,endId);
        for(Doc doc : docList){
            List<ContentBean> contentList = this.selectByDocId(doc.getId());
            DocBean docBean = new DocBean(doc.getId(),doc.getTitle(),doc.getLink(),contentList);
            docBeanList.add(docBean);
        }
        return docBeanList;
    }


}
