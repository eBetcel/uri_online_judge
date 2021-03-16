"""Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.

Input Sample	Output Sample
16 2

O JOGO DUROU 10 HORA(S)

0 0

O JOGO DUROU 24 HORA(S)

2 16

O JOGO DUROU 14 HORA(S)"""

minutes_in_a_day = 60 * 24

def time_to_minutes(start_hour, start_minute, end_hour, end_minute):
    start = start_hour * 60 + start_minute
    end = end_hour * 60 + end_minute

    if(start < end):
        duration_in_minutes = end - start

    else:
        duration_in_minutes = minutes_in_a_day - start + end

    return duration_in_minutes

time = input().split()

start_hour, start_minute, end_hour, end_minute = time

start_hour = int(start_hour)
start_minute = int(start_minute)
end_hour = int(end_hour)
end_minute = int(end_minute)

duration_in_minutes = time_to_minutes(start_hour, start_minute, end_hour, end_minute)

duration_hour = duration_in_minutes // 60
duration_minute = duration_in_minutes % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duration_hour, duration_minute)) 