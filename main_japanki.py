import tkinter as tk

# 창 생성
root = tk.Tk()
root.title("자판기")  # 창 제목 설정
root.geometry("1200x800")  # 창 크기 설정

# 레이블 함수
def juice_Label(name, pady_value):
    name = tk.Label(root, text=name)
    name.pack(pady=pady_value)

# 버튼 함수
def juice_button(name_value, width_value, height_value, x_value, y_value):
    # 버튼 생성, 클릭 시 on_button_click 함수 호출
    button = tk.Button(root, text=name_value, width = width_value, height=height_value, command=lambda: on_button_click(button))
    button.place(x = x_value, y = y_value)

# 버튼 클릭 시 동작할 함수 정의
def on_button_click(button):
    # 버튼 텍스트 변경
    button.config(text="버튼이 클릭되었습니다!")

# 버튼 추가
juice_button('사이다', 6, 2, 100, 1)
juice_button('콜라', 6, 2, 200, 1)
juice_button('물', 6, 2, 300, 1)
juice_button('봉봉', 6, 2, 400, 1)
juice_button('제티', 6, 2, 500, 1)

# 창 실행
root.mainloop()
