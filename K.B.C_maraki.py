question_list=["how many continents are there?",
              "what is the capital of india?",
              "NG mei kaun se course phdhaya jaata hai?",]
opstion_list=[["four","nine","seven","eight"],
              ["chandigarh","bhopal","chennai","delhi"],
              ["software engineering","counseling","tourism","agriculture"]]
solution_list=[1,4,1]
answer_list=[["1.four","3.seven"],
            ["2.bhopal","4.delhi"],
            ["1.software engineering","4.agriculture"]]
print("koun bnega crorepati(KBC)")
i=0
sum=0
coun=0
while i<len(question_list):
    print(question_list[i]) 
    j=0 
    k=1
    while j<=len(opstion_list):
        print(k,".",opstion_list[i][j])
        k=k+1
        j=j+1
    num=input("do u want 50 50 life line")
    if num =="yes":
        print("50 50 lifeline")
        if coun<1:
            print(answer_list[i])
            num1=int(input("enter the number"))
            if num1==solution_list[i]:
                sum=sum+10000
                print("your answer is correct")
                print("u win RS/-",sum)
            else:
                print("your answer is incorrect")
                break
            coun=coun+1
        else:
            print("u alredy used your life line")
            m=int(input("enter the number"))
            if m==solution_list[i]:
                print("congrats,ur answer is right")
                sum=sum+1000
                print("u win",sum)
            else:
                print("ur answer is wrong")
                print("u win",sum)
                break
    else:
        k=int(input("enter the number"))
        if k==solution_list[i]:
            print("right answer")
            sum=sum+100000
            print("u win RS/-",sum)
            print("congratulation")
        else:
            # print("no chance")
            print("ur answer is rigth")
    i=i+1







