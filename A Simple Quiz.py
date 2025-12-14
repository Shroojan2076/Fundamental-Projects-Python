import random as r
import time as t

q1 = ['Which language among these is the easiest to learn?', 'A) HTML', 'B) C or C++', 'C) Python', 'D) Kotlin', 'Ans :- A) HTML']
q2 = ['Who is the first person to step on the moon?', 'A) Yuri Gagarin', 'B) Edwin \'Buzz\' Aldrin', 'C) Neil Armstrong', 'D) Alan Shepard', 'Ans :- C) Neil Armstrong']
q3 = ['Who painted the Mona Lisa?', 'A) Vincent van Gogh', 'B) Pablo Picasso', 'C) Leonardo da Vinci', 'D) Michelangelo', 'Ans :- C) Leonardo da Vinci']
q4 = ['Which is the smallest country in the world by land area?', 'A) Monaco', 'B) Vatican City', 'C) San Marino', 'D) Liechtenstein', 'Ans :- B) Vatican City']
q5 = ['Which is the largest organ in the human body?', 'A) Liver', 'B) Heart', 'C) Skin', 'D) Lungs', 'Ans :- C) Skin']
q6 = ['What is the hardest natural substance on Earth?', 'A) Iron', 'B) Granite', 'C) Diamond', 'D) Quartz', 'Ans :- C) Diamond']
q7 = ['Which ocean is the largest?', 'A) Atlantic Ocean', 'B) Indian Ocean', 'C) Arctic Ocean', 'D) Pacific Ocean', 'Ans :- D) Pacific Ocean']
q8 = ['What is the chemical symbol for Gold?', 'A) Au', 'B) Ag', 'C) Gd', 'D) Go', 'Ans :- A) Au']
q9 = ['Which company owns the Android operating system?', 'A) Apple', 'B) Microsoft', 'C) Google', 'D) IBM', 'Ans :- C) Google']
q10 = ['Which of these is NOT a programming language?', 'A) Python', 'B) Java', 'C) HTML', 'D) Anaconda', 'Ans :- D) Anaconda']

quiz = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
option = ['0', 'A', 'B', 'C', 'D']
prize = [0, 100, 250, 450, 700, 1000, 1350, 1750, 2200, 2700, 3250]

count = 0
win = 0

r.shuffle(quiz)

print('Welcome to "A Simple Quiz!"')
print('Enter \'quit\' to Quit the game.')

for i in quiz:
    print(f'Current Winning: {win}')
    print('\n'.join(i[:-1]))

    try:
        ans = input('Enter Your Answer: ')
        if ans.lower() == 'quit':
            print('Your reward will be saved')
            break

        elif i[option.index(ans.upper())] == i[-1][7:]:
            print('Correct Answer!!')
            count += 1
            win += prize[count]
            print(f'You have won {prize[count]} points !!')
        else:
            print('Wrong Answer')
            print(f'Correct answer was {i[-1][7:]}')
    
    except ValueError:
        print('No such option exists. Question skipped.')
    except KeyboardInterrupt:
        pass

print(f'Congratuations !! You have won {win} points' if win != 0 else f'Better luck next time!')
print('Thank You!')
