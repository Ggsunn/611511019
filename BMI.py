
import math


def get_number(message):
    while True:
        try:
            number = float(input(message))
            if not math.isfinite(number) or number <= 0:
                print("請輸入大於 0 的有效數字。")
                continue
            return number
        except ValueError:
            print("輸入錯誤，請輸入數字。")


def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def main():
    print("===== BMI 計算程式 =====")

    while True:
        weight = get_number("請輸入體重 (kg)：")
        height = get_number("請輸入身高 (cm)：")

        try:
            bmi = calculate_bmi(weight, height)
            if not math.isfinite(bmi) or bmi <= 0:
                raise ValueError
        except (ValueError, OverflowError, ZeroDivisionError):
            print("數值超出計算範圍，請重新輸入。")
            continue

        print(f"\nBMI：{bmi:.2f}")

        if bmi < 18.5:
            print("體重過輕")
        elif bmi < 24:
            print("正常範圍")
        elif bmi < 27:
            print("體重過重")
        else:
            print("肥胖")

        again = input("\n繼續計算？(y/n)：").strip().lower()
        if again != "y":
            print("程式結束")
            break


if __name__ == "__main__":
    main()
