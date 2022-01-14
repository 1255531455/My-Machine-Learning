package com.example.SContext;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
//获取全局初始化配置信息
@WebServlet(name = "SContextDemo1", value = "/SContextDemo1")
public class SContextDemo1 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //获取ServletContext对象
//        ServletContext servletContext = this.getServletConfig().getServletContext();
//        String name = servletContext.getInitParameter("name");
//        System.out.println("name:"+name);

        //读取域属性
        ServletContext servletContext = this.getServletContext();
        String salary = (String) servletContext.getAttribute("salary");
        System.out.println("salary:"+salary);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
