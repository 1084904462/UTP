package org.obsidian.utp.service;

import org.obsidian.utp.bean.ContentBean;
import org.obsidian.utp.bean.DocBean;
import org.obsidian.utp.entity.Content;
import org.obsidian.utp.entity.Doc;

import java.util.List;

/**
 * Created by BillChen on 2018/2/9.
 */
public interface ContentService {
    List<Content> selectAllContent();

    int updateContent(Long id,Long keywordId,String content);

    List<ContentBean> selectByDocId(Long docId);

    List<Doc> selectDoc(Long startId,Long endId);

    List<DocBean> getDocBeanList(Long startId,Long endId);
}
