package com.example.SContext;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
//作为域对象使用
@WebServlet(name = "SContextDemo2", value = "/SContextDemo2")
public class SContextDemo2 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //获取代表web应用的与对象
        ServletContext servletContext = this.getServletConfig().getServletContext();
        servletContext.setAttribute("salary","100000");

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
