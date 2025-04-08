import tkinter as tk

# 창 생성
root = tk.Tk()
root.title("자판기")  # 창 제목 설정
root.geometry("1920x1080")  # 창 크기 설정
money = 10000000


# 레이블 함수
def juice_Label(name, pady_value):
    name = tk.Label(root, text=name)
    name.pack(pady=pady_value)

# 버튼 함수
def juice_button(name_value, width_value, height_value, x_value, y_value):
    # 버튼 생성, 클릭 시 on_button_click 함수 호출
    button = tk.Button(root, text=name_value, width = width_value, height=height_value, command=lambda: on_button_click(button, name_value))
    button.place(x = x_value, y = y_value)

# 버튼 클릭 시 동작할 함수 정의
def on_button_click(button, name_value):
    # 버튼 텍스트 변경
    name = tk.Label(root, text=f'{name_value}을 선택했습니다.')
    name.place(x= 100, y =700)
    name.destroy()


# 버튼 추가
juice_button('사이다', 6, 2, 50, 150)
juice_button('콜라', 6, 2, 150, 150)
juice_button('물', 6, 2, 250, 150)
juice_button('봉봉', 6, 2, 350, 150)
juice_button('제티', 6, 2, 450, 150)
juice_button('환타', 6, 2, 550, 150)
juice_button('밀키스', 6, 2, 650, 150)
juice_button('게토레이', 6, 2, 750, 150)
juice_button('마운티듀', 6, 2, 850, 150)
juice_button('아침햇살', 6, 2, 50, 300)
juice_button('토레타', 6, 2, 150, 300)
juice_button('닥터페퍼', 6, 2, 250, 300)
juice_button('웰치스', 6, 2, 350, 300)
juice_button('솔의 눈', 6, 2, 450, 300)
juice_button('2프로', 6, 2, 550, 300)
juice_button('데미소다', 6, 2, 650, 300)
juice_button('초록매실', 6, 2, 750, 300)
juice_button('핫식스', 6, 2, 850, 300)
juice_button('쌕쌕', 6, 2, 50, 450)



# 창 실행
root.mainloop()
