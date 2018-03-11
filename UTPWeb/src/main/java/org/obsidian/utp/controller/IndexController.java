package org.obsidian.utp.controller;

import org.apache.log4j.Logger;
import org.obsidian.utp.bean.DocBean;
import org.obsidian.utp.service.ContentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

/**
 * Created by BillChen on 2018/1/27.
 */
@Controller
public class IndexController {
    private Logger logger = Logger.getLogger(this.getClass());

    @Autowired
    private ContentService contentService;

    @RequestMapping("/")
    public String defaultPage(){
        logger.warn("进入首页");
        return "index";
    }

    @GetMapping("/update/{id}/{content}")
    public String updateContent(@PathVariable("id") Long id, @PathVariable("content") String content){
        logger.warn("更新内容,id:" + id + ",content:" + content);
        contentService.updateContent(id,1L,content);
        return "redirect:/";
    }

    @PostMapping("/getDocBeanList")
    public String getDocBeanList(Long startId,Long endId,Model model){
        logger.warn("startId:" + startId + " endId:" + endId);
        List<DocBean> docBeanList = contentService.getDocBeanList(startId,endId);
        System.out.println(docBeanList);
        model.addAttribute("docBeanList",docBeanList);
        return "doc";
    }
}
