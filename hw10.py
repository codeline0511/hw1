import os
import pickle

filename = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores

def show(scores):
    print('[점수 출력]')
    print('개인점수:', end =' ')
    for score in scores:
        print(score, end = ' ')
    print()
    print(f'평균: {sum(scores) / len(scores):.1f}')

def save_data(scores, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

if os.path.exists(filename):
    print('[파일 읽기]\n')
    score_list = load_data(filename)
    show(score_list)
else:
    score_list = input_scores()
    show(score_list)
    save_data(score_list, filename)
