package com.easymall.servlet;

import com.easymall.utils.JDBCUtils;
import com.easymall.utils.WebUtils;
import com.mchange.v2.c3p0.ComboPooledDataSource;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.beans.PropertyVetoException;
import java.io.IOException;
import java.sql.*;

@WebServlet(name = "RegistServlet", value = "/RegistServlet")
public class RegistServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //请求乱码处理
        request.setCharacterEncoding("utf-8");
        //响应乱码处理
        response.setContentType("text/html;charset=utf-8");
        //2.请求参数
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String password2 = request.getParameter("password2");
        String nickname = request.getParameter("nickname");
        String email = request.getParameter("email");
        String valistr = request.getParameter("valistr");

        //3.非空校验
        if (WebUtils.isNULL(username)){
            //将错误提示放入request域
            request.setAttribute("msg","用户名不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        if (WebUtils.isNULL(password)){
            //将错误提示放入request域
            request.setAttribute("msg","密码不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        if (WebUtils.isNULL(password2)){
            //将错误提示放入request域
            request.setAttribute("msg","确认密码不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        if (WebUtils.isNULL(nickname)){
            //将错误提示放入request域
            request.setAttribute("msg","昵称不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        if (WebUtils.isNULL(email)){
            //将错误提示放入request域
            request.setAttribute("msg","邮箱不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        if (WebUtils.isNULL(valistr)){
            //将错误提示放入request域
            request.setAttribute("msg","验证码不能为空");
            //使用请求转发，将request转发到regist.jsp页面
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            //打断注册
            return;
        }
        //4.密码一致性校验
        if (password != null && password2 != null && !password.equals(password2)){
            request.setAttribute("msg","两次密码不一致");
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            return;
        }
        //5.邮箱格式校验
        //van_d@163.com
        String reg = "\\w+@\\w+(\\.\\w+)+";
        if (email!=null && !email.matches(reg)){
            request.setAttribute("msg","邮箱格式不正确");
            request.getRequestDispatcher("/regist.jsp").forward(request,response);
            return;
        }
        //6.验证码校验
        //TODD:session
        //7.完成注册
        //连接池
        //用户名是否存在校验
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection conn = null;
        try {
            conn = JDBCUtils.getConnection();
            ps = conn.prepareStatement("select * from user where username=?");
            ps.setString(1,username);
            rs = ps.executeQuery();
            if (rs.next()){ //用户已存在，再页面中作出提示
                request.setAttribute("msg","用户名已存在");
                request.getRequestDispatcher("/regist.jsp").forward(request,response);
                return;
            }else { //用户名不存在，完成注册
                conn = JDBCUtils.getConnection();
                ps = conn.prepareStatement("insert into user values(null,?,?,?,?)");
                ps.setString(1,username);
                ps.setString(2,password);
                ps.setString(3,nickname);
                ps.setString(4,email);
                ps.executeUpdate();
                ps.executeBatch();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JDBCUtils.close(conn,ps,rs);
        }

        //8.跳转回首页
        response.getWriter().write("<h1 align='center'><font color='red'>恭喜注册成功，3秒后跳转回首页</font></h1>");
        response.setHeader("refresh","3;url=http://www.easymall.com");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);

    }
}
