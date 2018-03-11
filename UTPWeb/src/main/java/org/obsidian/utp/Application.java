package org.obsidian.utp;

import org.apache.log4j.Logger;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;



/**
 * Created by BillChen on 2017/8/12.
 */
@SpringBootApplication
public class Application {
    private static Logger logger = Logger.getLogger(Application.class);

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
        logger.warn("============= SpringBoot Start Success =============");
    }
}
