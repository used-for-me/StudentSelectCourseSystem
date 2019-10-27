#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Dec 29, 2018 10:09:56 AM CST  platform: Windows NT

import sys
import platform
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

from system import student_gui_support, Auth_student


def vp_start_gui(user):
    # '''Starting point when module is the main routine.'''
    global val, w, root, this_user
    this_user = user
    root = tk.Tk()
    student_gui_support.set_tk_var(user)
    top = Toplevel1(root)
    student_gui_support.init(root, top)
    root.mainloop()


w = None
w_win = None


def create_Toplevel1(root, *args, **kwargs):
    # '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    student_gui_support.set_tk_var(student_gui_support.user)
    top = Toplevel1(w)
    student_gui_support.init(w, top)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


def teacher_and_teacher_num():
    pp = ["select TeacherNum,TeacherName from tb_teacher;", 0]
    sss = Auth_student.Student.selected_course(*pp)
    teacher1_dict = {}
    for i in sss:
        teacher1_dict[i[0]] = i[1]
    return teacher1_dict


def find_teacher_and_teacher_num(course_num):
    p = ["select CourseTeacherNum from tb_course where CourseNum='{0}'".format(course_num), 0]
    ss = Auth_student.Student.select_course(*p)
    return ss


class Toplevel1:
    def __init__(self, top=None):
        global teacher_dict
        teacher_dict = teacher_and_teacher_num()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Microsoft YaHei UI} -size 12 -weight bold " \
                "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("399x399+547+165")
        top.title("学生界面")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        # 选课页面
        self.student_select_course_frame = tk.Frame(top)
        self.student_select_course_frame.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)
        self.student_select_course_frame.configure(relief='groove')
        self.student_select_course_frame.configure(borderwidth="2")
        self.student_select_course_frame.configure(relief='groove')
        self.student_select_course_frame.configure(background="#d9d9d9")
        self.student_select_course_frame.configure(highlightbackground="#d9d9d9")
        self.student_select_course_frame.configure(highlightcolor="black")
        self.student_select_course_frame.configure(width=125)

        self.Label3 = tk.Label(self.student_select_course_frame)
        self.Label3.place(relx=0.05, rely=0.05, height=28, width=123)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''学生选课界面 ：''')

        self.Message1 = tk.Message(self.student_select_course_frame)
        self.Message1.place(relx=0.375, rely=0.025, relheight=0.063, relwidth=0.493)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(textvariable=student_gui_support.message1)
        self.Message1.configure(width=197)

        # 第一个界面tree_view
        self.style.configure('Treeview.Heading', font="TkDefaultFont")
        self.Scrolled_tree_view2 = ScrolledTreeView(self.student_select_course_frame)
        self.Scrolled_tree_view2.place(relx=0.05, rely=0.175, relheight=0.568, relwidth=0.9)
        self.Scrolled_tree_view2.configure(show='headings')
        self.Scrolled_tree_view2.configure(columns=["Col1", "Col2", "Col3", "Col4", "Col5"])
        self.Scrolled_tree_view2.heading("#0", text="Tree")
        self.Scrolled_tree_view2.heading("#0", anchor="center")
        self.Scrolled_tree_view2.column("#0", width="175")
        self.Scrolled_tree_view2.column("#0", minwidth="20")
        self.Scrolled_tree_view2.column("#0", stretch="1")
        self.Scrolled_tree_view2.column("#0", anchor="w")

        self.Scrolled_tree_view2.heading("Col1", text="课程号")
        self.Scrolled_tree_view2.heading("Col1", anchor="center")
        self.Scrolled_tree_view2.column("Col1", width="70")
        self.Scrolled_tree_view2.column("Col1", minwidth="20")
        self.Scrolled_tree_view2.column("Col1", stretch="1")
        self.Scrolled_tree_view2.column("Col1", anchor="w")

        self.Scrolled_tree_view2.heading("Col2", text="课程名字")
        self.Scrolled_tree_view2.heading("Col2", anchor="center")
        self.Scrolled_tree_view2.column("Col2", width="70")
        self.Scrolled_tree_view2.column("Col2", minwidth="20")
        self.Scrolled_tree_view2.column("Col2", stretch="1")
        self.Scrolled_tree_view2.column("Col2", anchor="w")

        self.Scrolled_tree_view2.heading("Col3", text="学分")
        self.Scrolled_tree_view2.heading("Col3", anchor="center")
        self.Scrolled_tree_view2.column("Col3", width="70")
        self.Scrolled_tree_view2.column("Col3", minwidth="20")
        self.Scrolled_tree_view2.column("Col3", stretch="1")
        self.Scrolled_tree_view2.column("Col3", anchor="w")

        self.Scrolled_tree_view2.heading("Col4", text="学时")
        self.Scrolled_tree_view2.heading("Col4", anchor="center")
        self.Scrolled_tree_view2.column("Col4", width="70")
        self.Scrolled_tree_view2.column("Col4", minwidth="20")
        self.Scrolled_tree_view2.column("Col4", stretch="1")
        self.Scrolled_tree_view2.column("Col4", anchor="w")

        self.Scrolled_tree_view2.heading("Col5", text="教师")
        self.Scrolled_tree_view2.heading("Col5", anchor="center")
        self.Scrolled_tree_view2.column("Col5", width="70")
        self.Scrolled_tree_view2.column("Col5", minwidth="20")
        self.Scrolled_tree_view2.column("Col5", stretch="1")
        self.Scrolled_tree_view2.column("Col5", anchor="w")

        def select_course_func():
            p = ["select IfTakeCourse from tb_control", 0]
            x_list = Auth_student.Student.select_course_control(*p)
            if str(x_list[0][0]) == '1':
                item = self.Scrolled_tree_view2.selection()
                ss = self.Scrolled_tree_view2.item(item, "values")
                ppp = ["select* from tb_stucourse where StudentNum='{0}' and CourseNum='{1}';".format(this_user, ss[0]),
                       0]
                if Auth_student.Student.select_course(*ppp):
                    student_gui_support.message1.set('课程已选请勿点击')

                else:
                    xlist = find_teacher_and_teacher_num(ss[0])
                    pp = ["insert into tb_stucourse (StudentNum, CourseNum, TeacherNum)values('{0}','{1}','{2}')".format
                          (this_user, ss[0], xlist[0][0]), 1]

                    Auth_student.Student.select_course(*pp)
                    student_gui_support.message1.set('')

            else:
                student_gui_support.message1.set('现在不是选课时间')

        # def onDBClick(event):
        #     item = self.Scrolled_tree_view2.selection()
        #     ss = self.Scrolled_tree_view2.item(item, "values")
        #     # print(ss)
        #
        # self.Scrolled_tree_view2.bind("<ButtonRelease-1>", onDBClick)

        def select_course():
            student_gui_support.message1.set('')
            p = ["select * from tb_course", 0]
            ss = Auth_student.Student.selected_course(*p)
            x = self.Scrolled_tree_view2.get_children()
            for item in x:
                self.Scrolled_tree_view2.delete(item)
            if ss:
                for item in ss:
                    self.Scrolled_tree_view2.insert('', '0',
                                                    values=(item[0], item[1], item[2], item[3], teacher_dict[item[4]]))

        select_course()

        self.Button6 = tk.Button(self.student_select_course_frame)
        self.Button6.place(relx=0.65, rely=0.875, height=28, width=89)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(command=select_course)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''刷新''')

        self.Button1 = tk.Button(self.student_select_course_frame)
        self.Button1.place(relx=0.4, rely=0.875, height=28, width=85)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=select_course_func)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''选课''')
        self.Button1.configure(width=105)

        # 已选课程界面
        self.selected_course_frame = tk.Frame(top)
        self.selected_course_frame.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)
        self.selected_course_frame.configure(relief='groove')
        self.selected_course_frame.configure(borderwidth="2")
        self.selected_course_frame.configure(relief='groove')
        self.selected_course_frame.configure(background="#d9d9d9")
        self.selected_course_frame.configure(highlightbackground="#d9d9d9")
        self.selected_course_frame.configure(highlightcolor="black")
        self.selected_course_frame.configure(width=125)

        self.Label5 = tk.Label(self.selected_course_frame)
        self.Label5.place(relx=0.05, rely=0.05, height=28, width=96)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''已选课程  ：''')

        self.Message4 = tk.Message(self.selected_course_frame)
        self.Message4.place(relx=0.388, rely=0.025, relheight=0.063, relwidth=0.418)
        self.Message4.configure(background="#d9d9d9")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(textvariable=student_gui_support.selected_course_message)
        self.Message4.configure(width=167)

        self.selected_course_tree_view = ScrolledTreeView(self.selected_course_frame)
        self.selected_course_tree_view.place(relx=0.05, rely=0.175, relheight=0.568, relwidth=0.9)
        self.selected_course_tree_view.configure(show="headings")
        self.selected_course_tree_view.configure(columns=["Col1", "Col2", "Col3", "Col4"])
        self.selected_course_tree_view.heading("#0", text="tree")
        self.selected_course_tree_view.heading("#0", anchor="center")
        self.selected_course_tree_view.column("#0", width="170")
        self.selected_course_tree_view.column("#0", minwidth="20")
        self.selected_course_tree_view.column("#0", stretch="1")
        self.selected_course_tree_view.column("#0", anchor="w")

        self.selected_course_tree_view.heading("Col1", text="学号")
        self.selected_course_tree_view.heading("Col1", anchor="center")
        self.selected_course_tree_view.column("Col1", width="90")
        self.selected_course_tree_view.column("Col1", minwidth="20")
        self.selected_course_tree_view.column("Col1", stretch="1")
        self.selected_course_tree_view.column("Col1", anchor="w")

        self.selected_course_tree_view.heading("Col2", text="课程号")
        self.selected_course_tree_view.heading("Col2", anchor="center")
        self.selected_course_tree_view.column("Col2", width="90")
        self.selected_course_tree_view.column("Col2", minwidth="20")
        self.selected_course_tree_view.column("Col2", stretch="1")
        self.selected_course_tree_view.column("Col2", anchor="w")

        self.selected_course_tree_view.heading("Col3", text="教师")
        self.selected_course_tree_view.heading("Col3", anchor="center")
        self.selected_course_tree_view.column("Col3", width="90")
        self.selected_course_tree_view.column("Col3", minwidth="20")
        self.selected_course_tree_view.column("Col3", stretch="1")
        self.selected_course_tree_view.column("Col3", anchor="w")

        self.selected_course_tree_view.heading("Col4", text="分数")
        self.selected_course_tree_view.heading("Col4", anchor="center")
        self.selected_course_tree_view.column("Col4", width="80")
        self.selected_course_tree_view.column("Col4", minwidth="20")
        self.selected_course_tree_view.column("Col4", stretch="1")
        self.selected_course_tree_view.column("Col4", anchor="w")

        def flush_withdrawal_course():
            p = ["select * from tb_stucourse where StudentNum='{0}';".format(this_user), 0]
            ss = Auth_student.Student.selected_course(*p)
            x = self.selected_course_tree_view.get_children()
            for item in x:
                self.selected_course_tree_view.delete(item)
            if ss:
                for item in ss:
                    self.selected_course_tree_view.insert('', '0',
                                                          values=(item[0], item[1], teacher_dict[item[2]], item[3]))

        def withdrawal_course_button():
            item = self.selected_course_tree_view.selection()
            ss = self.selected_course_tree_view.item(item, "values")
            print(ss)
            p = ["delete from tb_stucourse where StudentNum='{0}'and CourseNum='{1}';".format(ss[0], ss[1]), 1]
            Auth_student.Student.selected_course(*p)
            flush_withdrawal_course()

        flush_withdrawal_course()

        self.Button3 = tk.Button(self.selected_course_frame)
        self.Button3.place(relx=0.65, rely=0.875, height=28, width=89)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=flush_withdrawal_course)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''刷新''')

        self.Button2 = tk.Button(self.selected_course_frame)
        self.Button2.place(relx=0.4, rely=0.875, height=28, width=85)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=withdrawal_course_button)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''退选''')
        self.Button2.configure(width=85)

        # 修改密码页面

        self.change_password_frame = tk.Frame(top)
        self.change_password_frame.place(relx=0.0, rely=0.0, relheight=1.003, relwidth=1.003)
        self.change_password_frame.configure(relief='groove')
        self.change_password_frame.configure(borderwidth="2")
        self.change_password_frame.configure(relief='groove')
        self.change_password_frame.configure(background="#d9d9d9")
        self.change_password_frame.configure(highlightbackground="#d9d9d9")
        self.change_password_frame.configure(highlightcolor="black")
        self.change_password_frame.configure(width=125)

        self.Label6 = tk.Label(self.change_password_frame)
        self.Label6.place(relx=0.05, rely=0.05, height=28, width=130)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''更改密码页面  ：''')

        self.Label7 = tk.Label(self.change_password_frame)
        self.Label7.place(relx=0.213, rely=0.175, height=23, width=50)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''用户  ：''')

        self.Label8 = tk.Label(self.change_password_frame)
        self.Label8.place(relx=0.4, rely=0.175, height=23, width=87)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''user''')
        self.Label8.configure(textvariable=student_gui_support.user)

        self.Label9 = tk.Label(self.change_password_frame)
        self.Label9.place(relx=0.2, rely=0.325, height=23, width=66)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''原密码   ：''')

        self.Label9_1 = tk.Label(self.change_password_frame)
        self.Label9_1.place(relx=0.2, rely=0.425, height=23, width=66)
        self.Label9_1.configure(activebackground="#f9f9f9")
        self.Label9_1.configure(activeforeground="black")
        self.Label9_1.configure(background="#d9d9d9")
        self.Label9_1.configure(disabledforeground="#a3a3a3")
        self.Label9_1.configure(foreground="#000000")
        self.Label9_1.configure(highlightbackground="#d9d9d9")
        self.Label9_1.configure(highlightcolor="black")
        self.Label9_1.configure(text='''新密码   ：''')

        self.Entry3 = tk.Entry(self.change_password_frame)
        self.Entry3.place(relx=0.4, rely=0.325, height=17, relwidth=0.36)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(show="*")
        self.Entry3.configure(textvariable=student_gui_support.password)

        self.Entry3_2 = tk.Entry(self.change_password_frame)
        self.Entry3_2.place(relx=0.4, rely=0.425, height=17, relwidth=0.36)
        self.Entry3_2.configure(background="white")
        self.Entry3_2.configure(disabledforeground="#a3a3a3")
        self.Entry3_2.configure(font="TkFixedFont")
        self.Entry3_2.configure(foreground="#000000")
        self.Entry3_2.configure(highlightbackground="#d9d9d9")
        self.Entry3_2.configure(highlightcolor="black")
        self.Entry3_2.configure(insertbackground="black")
        self.Entry3_2.configure(selectbackground="#c4c4c4")
        self.Entry3_2.configure(selectforeground="black")
        self.Entry3_2.configure(show="*")
        self.Entry3_2.configure(textvariable=student_gui_support.change_password)

        self.Button4 = tk.Button(self.change_password_frame)
        self.Button4.place(relx=0.475, rely=0.55, height=28, width=79)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=student_gui_support.change_password_button)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief='groove')
        self.Button4.configure(text='''提交''')

        self.Message2 = tk.Message(self.change_password_frame)
        self.Message2.place(relx=0.4, rely=0.05, relheight=0.063, relwidth=0.443)

        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(textvariable=student_gui_support.change_password_message)
        self.Message2.configure(width=177)

        # 首先显示页面
        self.student_select_course_frame.tkraise()

        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.student_select_course_frame.tkraise,
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="选课")
        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.selected_course_frame.tkraise,
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="查询选课信息")
        self.menubar.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            command=self.change_password_frame.tkraise,
            compound="left",
            font="TkMenuFont",
            foreground="#000000",
            label="更改密码")


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    # '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui('11412')
