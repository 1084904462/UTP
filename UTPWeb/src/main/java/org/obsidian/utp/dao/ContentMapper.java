package org.obsidian.utp.dao;

import java.util.List;
import org.apache.ibatis.annotations.Param;
import org.obsidian.utp.bean.ContentBean;
import org.obsidian.utp.entity.Content;
import org.obsidian.utp.entity.ContentExample;
import org.obsidian.utp.entity.Doc;

public interface ContentMapper {
    List<ContentBean> selectByDocId(Long docId);

    long countByExample(ContentExample example);

    int deleteByExample(ContentExample example);

    int deleteByPrimaryKey(Long id);

    int insert(Content record);

    int insertSelective(Content record);

    List<Content> selectByExample(ContentExample example);

    Content selectByPrimaryKey(Long id);

    int updateByExampleSelective(@Param("record") Content record, @Param("example") ContentExample example);

    int updateByExample(@Param("record") Content record, @Param("example") ContentExample example);

    int updateByPrimaryKeySelective(Content record);

    int updateByPrimaryKey(Content record);
}