import os
import pickle

def input_scores():
    print("[점수 입력]")
    scores = []
    i = 0
    while True:
        n = int(input(f"#{i + 1}? "))
        if n == -1:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(scores):
    total = sum(scores)
    return total / len(scores) if len(scores) > 0 else 0

def show_scores(scores):
    print("개인점수:", end=" ")
    for score in scores:
        print(score, end=" ")
    print()

def save_scores(scores):
    with open("score.bin", "wb") as file:
        pickle.dump(scores, file)

def load_scores():
    try:
        with open("score.bin", "rb") as file:
            scores = pickle.load(file)
            return scores
    except FileNotFoundError:
        return []

def main():
    scores = load_scores()

    if scores:
        print("[파일 읽기]\n")
        print("[점수 출력]")
        show_scores(scores)
        print("평균:", round(get_average(scores), 2))
    else:
        scores = input_scores()
        save_scores(scores)

    print("\n[점수 출력]")
    show_scores(scores)
    print("평균:", round(get_average(scores), 2))

if __name__ == "__main__":
    main()
