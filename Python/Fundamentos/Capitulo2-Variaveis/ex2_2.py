#1
print(((4/3)*3.14)*5**3)

#2
capa = 24.95
desconto= (capa - (capa*0.4))
total = (desconto*60)+ 3.0 + (0.75*(60-1))
print(total)

#3
primeiro = 8*60+15
segundo = 7*60+12
total_segundos = (primeiro*2)+ (segundo*3)
print(total_segundos)
hora_saida1 = (6*3600) + (52*60)
print(hora_saida1+total_segundos)
total = (hora_saida1+total_segundos)/3600

# extra - Formataçaõ de strings
money = 5
tasty = "xtudo"
burger = "xsalads"
s1 = f"show me the {money}"
s1 = "show me the {}".format("money")
print(s1)
s2 = f"hmmm, this is a {tasty} {burger}"

pi = 3.1415926
precision = 2
print( "{:.{}f}".format( pi, precision ) )

s1 = "cats"
s2 = "dogs"
s3 = " %s and %s living together" % (s1, s2)
s4 = " {} and {} living together ".format(s1, s2)
print(s3)
print(s4)

verb = "runs"
print( f"The girl {verb.upper()} quickly." )

# data
starters = [
    [ 'Andre Iguodala', 4, 3, 7 ],
    [ 'Klay Thompson', 5, 0, 21 ],
    [ 'Stephen Curry', 5, 8, 36 ],
    [ 'Draymon Green', 9, 4, 11 ],
    [ 'Andrew Bogut', 3, 0, 2 ],
]

# define format row
row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} |".format

for p in starters:
    print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))