package org.obsidian.utp.bean;

/**
 * Created by BillChen on 2018/3/10.
 */
public class ContentBean {
    private Long id;
    private String keyword;
    private String content;

    public ContentBean() {
    }

    public ContentBean(Long id, String keyword, String content) {
        this.id = id;
        this.keyword = keyword;
        this.content = content;
    }

    @Override
    public String toString() {
        return "ContentBean{" +
                "id=" + id +
                ", keyword='" + keyword + '\'' +
                ", content='" + content + '\'' +
                '}';
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
