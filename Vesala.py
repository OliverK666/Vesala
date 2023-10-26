import random
import matplotlib.pyplot as plt

class User:
    def __init__(self, id, name, surname, age, count, rating):
        self.name = name
        self.surname = surname
        self.age = age
        self.count = count
        self.rating = rating
        
        
    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}."
        
        
def commands():
    print("\nOvo je program koji ucitava korisnicke informacije i belezi njihove rezultate u igri vesala!\n")
    print("Na raspolaganju su Vam sledece komande: ")
    print("pomoc: prikaz mogucih komandi.")
    print("exit: izlazak iz programa.")
    print("dodaj: dodavanje novog korisnika.")
    print("login: koriscenje postojeceg korisnika.")
    print("prikazi: prikaz postojecih korisnika.")
    print("stats: prikaz statistika odredjenog korisnika.")
    print("najbolji: prikaz korisnika sa najnizim prosekom.")
    print("play: pokretanje igre vesala.\n")
    

def exists(name, surname):
    users = open("users.txt", "r")
    exists = False
    
    for line in users:
        checkName = line.split("|")[1]
        checkSurname = line.split("|")[2]
        
        if name == checkName and surname == checkSurname:
            exists = True
            break
        
    users.close()
    
    return exists

 
def usercount():
    users = open("users.txt", "r")
    n = 0
    
    for line in users:
        n += 1
        
    users.close()
        
    return n


def findword():
    words = open("words.txt", "r")
    line = next(words)
    
    for num, aline in enumerate(words, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

def diff(word):
    Dict = {'a': 1, 'b': 4, 'c': 2, 'd': 3, 'e': 1, 'f': 4, 'g': 4, 'h': 3, 'i': 1, 'j': 5, 'k': 5, 'l': 2, 'm': 3,
            'n': 2, 'o': 1, 'p': 3, 'q': 5, 'r': 1, 's': 2, 't': 2, 'u': 3, 'v': 5, 'w': 4, 'x': 5, 'y': 4, 'z': 5}
    difficulty = 0    
    word = set(word)
    word.remove('\n')
    
    for letter in word:
        difficulty += Dict[letter]
    
    return difficulty


def hangman(n):
    if n == 0:
        print("  +---+  ")
        print("  |   |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("=========")
        
    elif n == 1:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print("      |  ")
        print("      |  ")
        print("      |  ")
        print("=========")
        
    elif n == 2:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print("  |   |  ")
        print("      |  ")
        print("      |  ")
        print("=========")
        
    elif n == 3:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|   |  ")
        print("      |  ")
        print("      |  ")
        print("=========")
        
    elif n == 4:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\  |  ")
        print("      |  ")
        print("      |  ")
        print("=========")
        
    elif n == 5:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\  |  ")
        print(" /    |  ")
        print("      |  ")
        print("=========")
        
    elif n == 6:
        print("  +---+  ")
        print("  |   |  ")
        print("  O   |  ")
        print(" /|\  |  ")
        print(" /\   |  ")
        print("      |  ")
        print("=========")
           
    
def welcome():       
    ans = ""
    loggedIn = False
    global user
    
    while ans != "exit":
        ans = input("\nSta zelite da radite? (Za listu komandi napisite pomoc): ")
        
        if ans == "pomoc":
            commands()
            
        elif ans == "dodaj":
            name = input("\nUnesite ime novog korisnika: ")
            surname = input("Unesite prezime novog korisnika: ")
            age = input("Unesite godine novog korisnika: ")
            
            if not exists(name, surname):
                users = open("users.txt", "a")
                users.write(str(usercount()) + "|" + name + "|" + surname + "|" + str(age) + "|0|0|\n")
                user = User(usercount(), name, surname, age, 0, 0)
            
            else:
                print("\nKorisnika kog ste uneli vec postoji!")
                
            users.close()
                
            
        elif ans == "login":
            users = open("users.txt", "r")
            name = input("\nUnesite ime postojeceg korisnika: ")
            surname = input("Unesite prezime postojeceg korisnika: ")
            
            if exists(name, surname):
                for line in users:
                    checkName = line.split("|")[1]
                    checkSurname = line.split("|")[2]
                    
                    if name == checkName and surname == checkSurname:
                        age = int(line.split("|")[3])
                        count = int(line.split("|")[4])
                        rating = float(line.split("|")[5])
                        user = User(id, name, surname, age, count, rating)
                        loggedIn = True
                    
                users.close()
                print("\nDobrodosli, " + name + " " + surname)
                
            else:
                print("\nKorisnika kog ste uneli ne postoji!")
                
        
        elif ans == "prikazi":
            users = open("users.txt", "r")
            print("\nU trenutnoj bazi podataka postoje sledeci korisnici: ")
            
            for line in users:
                print(line.split("|")[1] + " " + line.split("|")[2])
                
            users.close()
                
        elif ans == "stats":
            users = open("users.txt", "r")
            name = input("\nUnesite ime korisnika: ")
            surname = input("Unesite prezime korisnika: ")
            
            if exists(name, surname):
                for line in users:
                    checkName = line.split("|")[1]
                    checkSurname = line.split("|")[2]
                    
                    if name == checkName and surname == checkSurname:
                        age = int(line.split("|")[3])
                        count = int(line.split("|")[4])
                        rating = float(line.split("|")[5])
                        
                        print("\nKorisnik " + name + " " + surname + " ima " + str(age) + " godina, " + "odigrao je " + str(count) + " partija i rating mu je " + str(rating))
                    
                users.close()
            
            else:
                print("\nDobrodosli, " + name + " " + surname)
                
        elif ans == "najbolji":
            maxi = -1
            users = open("users.txt", "r")
            
            for line in users:
                rating = line.split("|")[5]
                
                if float(rating) > maxi:
                    name = line.split("|")[1]
                    surname = line.split("|")[2]
                    maxi = float(rating)
                    
            if maxi == -1:
                print("\nTrenutno nema korisnika!")
                
            else:
                print("\nNajvisi rating ima " + name + " " + surname + " sa rating-om od " + str(maxi))
                
        elif ans == "play":
            if loggedIn:
                play()
                ans = "exit"
            
            else:
                print("Da biste igrali morate prvo izabrati korisnika!")
 
               
def play():
    with open("users.txt", 'r') as file:
        data = file.read()
        data.replace("\n", "")
        data.join("")
        data = data.split("|")
    
    user.count += 1
    word = findword()
    difficulty = diff(word)
    i = 1
    n = 0
    answer = ["_"] * (len(word) - 1)
    guessed = []
    
    while i < len(word):
        i += 1
        print("_", end =" ")
        
    print()
    
    while "_" in answer and n < 6:
        hangman(n)
        print("\nDo sada ste iskoristili sledeca slova: ", end = "")
        print(guessed)
        
        guess = input("\nPogadjajte slovo: ")
        i = 0
        correct = False
        
        for letter in word:
            if guess == letter:
                answer[i] = guess
                correct = True
            i += 1
            
        if correct:
            print("\nPogodatak!\n")
            
        else:
            guessed.append(guess)
            print("\nPromasaj!\n")
            n += 1
            
        print(answer)
        print()
    
    if not "_" in answer:
        print("Pogodili ste rec " + word + " u " + str(n) + " koraka!\n")
        user.rating = ((user.count - 1) * user.rating + difficulty) / user.count
    
    else:
        print("Niste uspeli da pogodite rec: " + word)
        user.rating = ((user.count - 1) * user.rating + 0) / user.count
        
    print("Rec koju ste pogadjali bila je tezine " + str(difficulty))
        
    for i in range((len(data) - 1)):
        if user.name == data[i] and user.surname == data[i+1]:
            data[i+3] = user.count
            data[i+4] = user.rating
            
    i = 0
    
    with open("users.txt", 'w') as file:
        for x in data:
            file.write(str(x))
            if i != len(data) - 1:
                file.write("|")
            i += 1
    
    names = []
    scores = []
            
    with open("users.txt", 'r') as file:
        for line in file:
            names.append(str(line.split("|")[1]) + str(line.split("|")[2][0]))
            scores.append(round(float(line.split("|")[5]), 2))
    
    plt.bar(names, scores)
    plt.xlabel("Imena")
    plt.ylabel("Prosek broja pogadjanja")
    plt.title("Statistike za igru vesala")
    plt.show()
    
    cont = input("Da li zelite da nastavite sa unosom? (da/ne): ")
    
    if cont == "da":
        welcome()
        
              
    
welcome()
        