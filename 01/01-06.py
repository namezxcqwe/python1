print('Ваша задача отвечать только да или нет')
firstquestion = input('Вы любите играть в компьютер? ')
secondquestion = input('Вы любите программировать? ')
if firstquestion == 'да' and secondquestion == 'да':
    print('Вы можете попробовать отучиться на программиста и стать IT-специалистом')
elif firstquestion == 'да' and secondquestion == 'нет':
    print('Вы - компьютерный червь. Вам стоит меньше играть в компьютер')
elif firstquestion == 'нет' and secondquestion == 'да':
    print('Поздравляю, мир нуждается в таких как вы!')
elif firstquestion == 'нет' and secondquestion == 'нет':
    print('В таком случае, в каком направлении вы сильны?')
else:
    print('Вы не отвечали да или нет на наши вопросы!')