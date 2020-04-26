import math
import sys

def combo(n, k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))

def prob_correct_answer(n, k, c):
    #n: number of questions
    #k: number of correct questions guess right
    #c: number of choices; assume only one correct answer
    #p: probability of getting k correct guessed answered and n-k wrong guessed answer
    p = math.pow(1/c, k) * math.pow((1 - 1/c), n-k)
    #c: number of the combination choice k object from n choices
    c = combo(n, k)
    return p*c


def main():
    if len(sys.argv) == 4:
       n= int(sys.argv[1])
       k= int(sys.argv[2])
       c= int(sys.argv[3])
       for i in range(n):
           print(i, prob_correct_answer(n,i,c))
    else:
       n= int(input("Enter number of questions: "))
       k= int(input("Enter number of correct guessed questions: "))
       c= int(input("Enter number of the choice per question: "))
    
    x = prob_correct_answer(n,k,c)
    print(f'The probability of guessing {k} questions correctly \nfor {n} multiple choice questions \nhaving {c} choices per questions is \n{x}\n')
    

if __name__ == '__main__':
    main()
    sys.exit()
