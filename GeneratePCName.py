from random import choice

ladict = ['Sakura',
          'Yume',
          'Function',
          'Owari',
          'Operate',
          'Matrix',
          'Mirai',
          'Tsuki',
          'Light',
          'Kaze',
          'Prompt',
          'Ame',
          'Source',
          'Volume',
          'Hikari',
          'Thread',
          'Object',
          'Kaguya',
          'Compile',
          'Yoru',
          'Hoshi',
          'Sora',
          'Yuki',
          'Ake',
          'Analyst',
          'Negotiator',
          'Spring',
          'Logical']

count = 0
while(count < 10):
    print(choice(ladict) + choice(ladict))
    count = count+1
    