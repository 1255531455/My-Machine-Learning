package com.easymall.servlet;

import com.easymall.utils.VerifyCode;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.FileOutputStream;
import java.io.IOException;
//验证码生成的Servlet
@WebServlet(name = "ValidateServlet", value = "/ValidateServlet")
public class ValidateServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //控制浏览器不适用缓存
        response.setDateHeader("Expires",-1);
        response.setHeader("Cache-Control","no-cache");
        VerifyCode vc = new VerifyCode();
        //当前servlet只有img标签调用，所以将图片放入缓冲区，最终会在其调用的位置输出在浏览器中
        vc.drawImage(response.getOutputStream());
        String code = vc.getCode();
        System.out.println(code);
        System.out.println("执行成功~!");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
