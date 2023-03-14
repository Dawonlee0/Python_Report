# 사용자로부터 원의 반지름을 정수 로 입력받아 그 원의 넓이를 구하는 프로그램을 작성하세요


pi = 3.14

# 반지름 입력 함수
def get_radius(prompt):
    r = int(input(prompt))
    return r

# 넓이 구하는 함수
def get_circle_area(radius):
    area = pi * radius ** 2
    return area

radius = get_radius("넓이를 구하고자 하는 원의 반지름은 ? ")
원넓이 = get_circle_area(radius)

# 출력
print(f"반지름 {radius}인 원의 넓이 = {pi} x {radius} = {원넓이}")