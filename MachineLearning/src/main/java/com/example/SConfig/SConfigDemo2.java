package com.example.SConfig;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
//使用方法直接产生一个ServletConfig对象
@WebServlet(name = "SConfigDemo2", value = "/SConfigDemo2")
public class SConfigDemo2 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        ServletConfig config = this.getServletConfig();
        String driver = config.getInitParameter("driver");
        String url = config.getInitParameter("url");
        System.out.println("driver:"+driver+"url:"+url);

        ServletContext servletContext = this.getServletConfig().getServletContext();
        String name = servletContext.getInitParameter("name");
        System.out.println("name:"+name);

        Object salary = servletContext.getAttribute("salary");
        System.out.println("salary:"+salary);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
