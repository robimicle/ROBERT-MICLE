articol = """
Acesta este un exemplu de articol de știri. În acest articol, vom discuta despre importanța educației.
Să ne amintim că educația este cheia succesului în viață!
"""


lungime = len(articol)
parte1 = articol[:lungime // 2]
parte2 = articol[lungime // 2:]

parte1 = parte1.strip()
parte1 = parte1.upper()

parte2 = parte2[::-1]
parte2 = parte2.capitalize()
parte2 = ''.join(c for c in parte2 if c.isalnum() or c.isspace())

rezultat = parte1 + " " + parte2
print(rezultat)
