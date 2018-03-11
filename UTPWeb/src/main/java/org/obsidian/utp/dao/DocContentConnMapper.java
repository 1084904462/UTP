package org.obsidian.utp.dao;

import java.util.List;
import org.apache.ibatis.annotations.Param;
import org.obsidian.utp.entity.DocContentConn;
import org.obsidian.utp.entity.DocContentConnExample;

public interface DocContentConnMapper {
    long countByExample(DocContentConnExample example);

    int deleteByExample(DocContentConnExample example);

    int deleteByPrimaryKey(Long id);

    int insert(DocContentConn record);

    int insertSelective(DocContentConn record);

    List<DocContentConn> selectByExample(DocContentConnExample example);

    DocContentConn selectByPrimaryKey(Long id);

    int updateByExampleSelective(@Param("record") DocContentConn record, @Param("example") DocContentConnExample example);

    int updateByExample(@Param("record") DocContentConn record, @Param("example") DocContentConnExample example);

    int updateByPrimaryKeySelective(DocContentConn record);

    int updateByPrimaryKey(DocContentConn record);
}