package com.example.SConfig;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
//获取当前servlet的初始化配置信息
//@WebServlet(name = "SConfigDemo1", value = "/SConfigDemo1")
public class SConfigDemo1 extends HttpServlet {
    public ServletConfig config = null;
    @Override
    public void init(ServletConfig config) throws ServletException {
        this.config = config;
//        String driver = config.getInitParameter("driver");
//        System.out.println("driver:"+driver);
//        super.init();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String driver = config.getInitParameter("driver");
        System.out.println("driver:"+driver);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
