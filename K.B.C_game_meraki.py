question_list=["how many continents are there?",
              "what is the capital of india?",
              "NG mei kaun se course phdhaya jaata hai?"]
optinos_list=[["four","nine","seven","eight"],
              ["chandigarh","bhopal","chennai","delhi"],
              ["software engineering","counseling","tourism","agriculture"]]
solution_list=[3,4,1]
life_line=[[3,4],[2,4],[1,2]]
money=[1000,5000,8000]
i=0
sum=0
coun=0
while i<len(question_list):
    print(i+1,question_list,[i])
    j=0
    while j<len(optinos_list):
        print(j+1,optinos_list[i][j])
        j=j+1
    if coun<1:
        print("do you want a life?")
        h=input("say yes our no?")
        if h=="yes":
            coun=coun+1
            print(life_line[i])
        else:
            print("you have used your life line")
        a=int(input("enter the number"))
        if a==solution_list[i]:
            sum=sum+money[i]
            print("ur ans is correcr,you have won the rupees",sum,"only/-")
        else:
            print("ur ans is wrong,you have won the ruprrs",sum,"only/-")
            break
    i=i+1