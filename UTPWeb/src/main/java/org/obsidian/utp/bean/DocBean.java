package org.obsidian.utp.bean;

import java.util.List;

/**
 * Created by BillChen on 2018/3/10.
 */
public class DocBean {
    private Long id;
    private String title;
    private String link;
    private List<ContentBean> contentBeanList;

    public DocBean() {
    }

    public DocBean(Long id, String title, String link, List<ContentBean> contentBeanList) {
        this.id = id;
        this.title = title;
        this.link = link;
        this.contentBeanList = contentBeanList;
    }

    @Override
    public String toString() {
        return "DocBean{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", link='" + link + '\'' +
                ", contentBeanList=" + contentBeanList +
                '}';
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public List<ContentBean> getContentBeanList() {
        return contentBeanList;
    }

    public void setContentBeanList(List<ContentBean> contentBeanList) {
        this.contentBeanList = contentBeanList;
    }
}
