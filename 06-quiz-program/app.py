score = 0

for key, value in []:
  answer = input('Answer?')

  if answer.lower() == value['answer'].lower():
    print('Correct')
    score = score + 1
  else:
    print('Incorrect')