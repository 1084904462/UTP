package org.obsidian.utp.dao;

import java.util.List;
import org.apache.ibatis.annotations.Param;
import org.obsidian.utp.entity.Doc;
import org.obsidian.utp.entity.DocExample;

public interface DocMapper {
    List<Doc> selectDocList(@Param("startId")Long startId,@Param("endId")Long endId);

    long countByExample(DocExample example);

    int deleteByExample(DocExample example);

    int deleteByPrimaryKey(Long id);

    int insert(Doc record);

    int insertSelective(Doc record);

    List<Doc> selectByExample(DocExample example);

    Doc selectByPrimaryKey(Long id);

    int updateByExampleSelective(@Param("record") Doc record, @Param("example") DocExample example);

    int updateByExample(@Param("record") Doc record, @Param("example") DocExample example);

    int updateByPrimaryKeySelective(Doc record);

    int updateByPrimaryKey(Doc record);
}