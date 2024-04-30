ranking = ['John', 'Sen', 'Lisa']

person_rank = input("Enter a rank number: ")

match int(person_rank):
    case 1:
        person_rank = 'John'
    case 2:
        person_rank = 'Sen'
    case 3:
        person_rank = 'Lisa'

print(person_rank)
