# 입력 함수
def input_student():
    student_info = {}  # 학생 정보를 저장할 딕셔너리 생성

    # 학번, 이름, 영어, C-언어, 파이썬 점수 입력 받기
    student_info['학번'] = input("학번: ")
    student_info['이름'] = input("이름: ")
    student_info['영어'] = int(input("영어: "))
    student_info['C언어'] = int(input("C-언어: "))
    student_info['파이썬'] = int(input("파이썬: "))

    return student_info

# 총점과 평균 계산 함수
def calculate_total_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

# 학점 계산 함수
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# 등수 계산 함수
def calculate_rank(students):
    ranked_students = sorted(students, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(ranked_students):
        student['등수'] = i + 1
    return ranked_students

# 출력 함수
def print_students(students):
    # 테이블 헤더 출력
    print(" " * 7, "성적관리 프로그램")
    print("=" * 85)
    print(" {:<12s}{:<10s}{:<8s}{:<10s}{:<9s}{:<8s}{:<8s}{:<8s}{:<8s}".format(
        "학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수"))
    print("=" * 85)

    # 각 학생 정보 출력
    for student in students:
        print(" {:<12s}{:<10s}{:<8d}{:<10d}{:<9d}{:<8d}{:<8.2f}{:<8s}{:<8d}".format(
            student['학번'], student['이름'], student['영어'], student['C언어'], student['파이썬'],
            student['총점'], student['평균'], student['학점'], student['등수']))

    print("=" * 85)

def main():
    # 학생들의 성적 정보를 저장할 리스트 생성
    students = []

    # 5명의 학생 정보 입력 받기
    for _ in range(5):
        student_info = input_student()
        # 총점과 평균 계산
        student_info['총점'], student_info['평균'] = calculate_total_average(
            [student_info['영어'], student_info['C언어'], student_info['파이썬']])
        # 학점 계산
        student_info['학점'] = calculate_grade(student_info['평균'])
        students.append(student_info)

    # 등수 계산
    students = calculate_rank(students)

    # 학생 정보 출력
    print_students(students)

if __name__ == "__main__":
    main()
