import time
import tkinter as tk

def start_timer():
    countdown(25 * 60)  # 设置专注时长为25分钟

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f'{mins:02d}:{secs:02d}')
        root.update()
        time.sleep(1)
        seconds -= 1
    timer_label.config(text="Time's up!")

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 创建标签显示倒计时
timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 创建开始按钮
start_button = tk.Button(root, text="开始专注", command=start_timer)
start_button.pack()

# 运行主循环
root.mainloop()
