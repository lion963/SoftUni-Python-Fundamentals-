tickets_list = input().split(', ')

for ticket in tickets_list:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print(f'invalid ticket')
    else:
        left_ticket = ticket[:10]
        right_ticket = ticket[10:]
        if 6 <= left_ticket.count('@') < 10 and 6 <= right_ticket.count('@') < 10:
            match_length = left_ticket.count('@')
            print(f'ticket \"{ticket}\" - {match_length}@')
        elif 6 <= left_ticket.count('#') < 10 and 6 <= right_ticket.count('#') < 10:
            match_length = left_ticket.count('#')
            print(f'ticket \"{ticket}\" - {match_length}#')
        elif 6 <= left_ticket.count('$') < 10 and 6 <= right_ticket.count('$') < 10:
            match_length = left_ticket.count('$')
            print(f'ticket \"{ticket}\" - {match_length}$')
        elif 6 <= left_ticket.count('^') < 10 and 6 <= right_ticket.count('^') < 10:
            match_length = left_ticket.count('^')
            print(f'ticket \"{ticket}\" - {match_length}^')
        elif ticket.count('@') == 20:
            match_length = ticket.count('@') // 2
            print(f'ticket \"{ticket}\" - {match_length}@ Jackpot!')
        elif ticket.count('#') == 20:
            match_length = ticket.count('#') // 2
            print(f'ticket \"{ticket}\" - {match_length}# Jackpot!')
        elif ticket.count('$') == 20:
            match_length = ticket.count('$') // 2
            print(f'ticket \"{ticket}\" - {match_length}$ Jackpot!')
        elif ticket.count('^') == 20:
            match_length = ticket.count('^') // 2
            print(f'ticket \"{ticket}\" - {match_length}^ Jackpot!')
        else:
            print(f'ticket \"{ticket}\" - no match')
