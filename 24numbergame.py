from itertools import permutations
import tkinter as tk
from tkinter import ttk
import webbrowser

languages = {
    "Chinese": {
        "title": "24点数字游戏",
        "label1": "第1个数字:",
        "label2": "第2个数字:",
        "label3": "第3个数字:",
        "label4": "第4个数字:",
        "calculate": "计算",
        "result": "四个数字：{0}、{1}、{2}、{3}\n表达式数量：{4}\n表达式组合：\n",
        "no_result": "无可组合的表达式！",
        "copy_success": "结果已复制到剪贴板",
        "clear_input": "清空输入",
        "copy_result": "复制结果"
    },
    "English": {
        "title": "24 Number Game",
        "label1": "Number 1:",
        "label2": "Number 2:",
        "label3": "Number 3:",
        "label4": "Number 4:",
        "calculate": "Calculate",
        "result": "Numbers: {0}, {1}, {2}, {3}\nExpression Count: {4}\nExpressions:\n",
        "no_result": "No composable expressions!",
        "copy_success": "Result copied to clipboard",
        "clear_input": "Clear Input",
        "copy_result": "Copy Result"
    }
}

current_language = "Chinese"

def check_24(event=None):
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    d = int(entry4.get())
    my_list = [a, b, c, d]
    result = [c for c in permutations(my_list, 4)]

    symbols = ["+", "-", "*", "/"]

    list2 = []
    flag = False

    for one, two, three, four in result:
        for s1 in symbols:
            for s2 in symbols:
                for s3 in symbols:
                    if s1 + s2 + s3 == "+++" or s1 + s2 + s3 == "***":
                        express = ["{0}{1}{2}{3}{4}{5}{6}".format(one, s1, two, s2, three, s3, four)]
                    else:
                        express = [
                            "(({0}{1}{2}){3}{4}){5}{6}".format(one, s1, two, s2, three, s3, four),
                            "({0}{1}{2}){3}({4}{5}{6})".format(one, s1, two, s2, three, s3, four),
                            "(({0}{1}({2}{3}{4})){5}{6})".format(one, s1, two, s2, three, s3, four),
                            "{0}{1}(({2}{3}{4}){5}{6})".format(one, s1, two, s2, three, s3, four),
                            "{0}{1}({2}{3}({4}{5}{6}))".format(one, s1, two, s2, three, s3, four)
                        ]

                    for e in express:
                        try:
                            if round(eval(e), 6) == 24:
                                list2.append(e)
                                flag = True
                        except ZeroDivisionError:
                            pass

    list3 = set(list2)
    
    result_text.delete('1.0', tk.END)

    if flag:
        result_text.insert(tk.END, languages[current_language]["result"].format(a, b, c, d, len(list3)))
        for i, expr in enumerate(list3):
            result_text.insert(tk.END, "({0}) {1}\n".format(i+1, expr))
    else:
        result_text.insert(tk.END, languages[current_language]["no_result"])

def clear_input():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def copy_result():
    result_text.clipboard_clear()
    result_text.clipboard_append(result_text.get("1.0", tk.END))
    show_copy_success()

def show_copy_success():
    copy_label.config(text=languages[current_language]["copy_success"], font=('Arial', 10), pady=0)  
    root.after(3000, clear_copy_label)

def clear_copy_label():
    copy_label.config(text="", pady=0) 

def update_language_button():
    if current_language == "Chinese":
        language_button.config(text="English")
    else:
        language_button.config(text="中文")

def toggle_language():
    global current_language
    if current_language == "Chinese":
        current_language = "English"
    else:
        current_language = "Chinese"
        
    language_button_text = "English" if current_language == "Chinese" else "中文"
    var_language.set(language_button_text)
    root.update()
    update_language_button()
    update_language()
    
    

def update_language():
    title_label.config(text=languages[current_language]["title"])
    label1.config(text=languages[current_language]["label1"])
    label2.config(text=languages[current_language]["label2"])
    label3.config(text=languages[current_language]["label3"])
    label4.config(text=languages[current_language]["label4"])
    submit_button.config(text=languages[current_language]["calculate"])
    clear_button.config(text=languages[current_language]["clear_input"])
    copy_button.config(text=languages[current_language]["copy_result"])

root = tk.Tk()
root.title(languages[current_language]["title"])
root.config(bg="#F7F7F7")  # 设置界面背景色为浅灰色

def open_link(event):
    webbrowser.open("https://www.github.com/viiayil")
title_label = tk.Label(root, text=languages[current_language]["title"], font=('Arial', 18, 'bold'), bg="#F7F7F7", fg="#333333")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10))
title_label.bind("<Button-1>", open_link)

title_label.bind("<Button-1>", open_link)

var_language = tk.StringVar()
var_language.set("English" if current_language == "Chinese" else "中文")

language_button = tk.Button(root, textvariable=var_language, command=toggle_language, font=('Arial', 8), bg="#F7F7F7", fg="#333333")
language_button.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 10), sticky="e")


entry_style = {'font': ('Arial', 12)}
button_style = {
    'width': 10,
    'font': ('Arial', 12),
    'bg': '#0A1931',  
    'fg': 'white',  
    'activebackground': 'black',  
    'activeforeground': 'white',  
}

input_frame = tk.Frame(root, bg="#F7F7F7")  
input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10))

label1 = tk.Label(input_frame, text=languages[current_language]["label1"], font=('Arial', 12), bg="#F7F7F7", fg="#333333")
label1.grid(row=0, column=0, padx=10, pady=3)
entry1 = tk.Entry(input_frame, **entry_style)
entry1.grid(row=0, column=1, padx=10, pady=3)

label2 = tk.Label(input_frame, text=languages[current_language]["label2"], font=('Arial', 12), bg="#F7F7F7", fg="#333333")
label2.grid(row=1, column=0, padx=10, pady=3)
entry2 = tk.Entry(input_frame, **entry_style)
entry2.grid(row=1, column=1, padx=10, pady=3)

label3 = tk.Label(input_frame, text=languages[current_language]["label3"], font=('Arial', 12), bg="#F7F7F7", fg="#333333")
label3.grid(row=2, column=0, padx=10, pady=3)
entry3 = tk.Entry(input_frame, **entry_style)
entry3.grid(row=2, column=1, padx=10, pady=3)

label4 = tk.Label(input_frame, text=languages[current_language]["label4"], font=('Arial', 12), bg="#F7F7F7", fg="#333333")
label4.grid(row=3, column=0, padx=10, pady=3)
entry4 = tk.Entry(input_frame, **entry_style)
entry4.grid(row=3, column=1, padx=10, pady=3)

submit_button = tk.Button(root, text=languages[current_language]["calculate"], command=check_24, **button_style)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=0)

result_frame = ttk.Frame(root)
result_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

result_text = tk.Text(result_frame, width=40, height=10, font=('Arial', 12), bg="white", fg="#333333")
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text.configure(yscrollcommand=scrollbar.set)

clear_button = tk.Button(root, text=languages[current_language]["clear_input"], command=clear_input, **button_style)
clear_button.grid(row=6, column=0, padx=10, pady=3)

copy_button = tk.Button(root, text=languages[current_language]["copy_result"], command=copy_result, **button_style)
copy_button.grid(row=6, column=1, padx=10, pady=3)

copy_label = tk.Label(root, text="", font=('Arial', 10))
copy_label.grid(row=7, column=0, columnspan=2, padx=10, pady=3)

root.bind('<Return>', check_24)

root.grid_columnconfigure(0, weight=1, minsize=200)
root.grid_columnconfigure(1, weight=1, minsize=200)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
