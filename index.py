import pyperclip
import os
from email.message import EmailMessage
import smtplib
#Importerer biblioteket for dekorere terminalen med farger
from colorama import Fore, Back, Style, init

#Initialiserer fargene
init(autoreset=True)

def main():
    #Dekorasjon og introduksjon:
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + "  Velkommen til Katte-Spam-Mail programmet  ")
    print(Fore.MAGENTA + "          Laget av Thor A. Å.          ")
    print(Fore.GREEN + "               19.03.2025              ")
    print(Fore.YELLOW + "=" * 60)
    print("")

    max_value = 5000000  # Maksimal antall med emojier.
    antall = int(input(Fore.CYAN + f"Hvor mange katte-emojier ønsker du? (Skriv antall, maks: {max_value}): "))

    # Sjekker at input er gyldig iforhold til grensen.
    while antall > max_value:
        antall = int(input(Fore.YELLOW + f"Skriv ett tall som er mindre eller lik {max_value}: "))
    
    output = skrivFinduser(antall)
    print(Fore.GREEN + f"Gyldig input: {antall} emojier")
    
    # Spør om brukeren vil sende dette på e-post
    send_email_prompt = input(Fore.CYAN + "Vil du sende dette som en e-post? (ja eller nei): ").strip().lower()
    if send_email_prompt == "ja":
        send_email(output)
    else:
        print(Fore.YELLOW + "Epost ble ikke sendt.")

def skrivFinduser(n):
    output = ""  
    print(Fore.YELLOW + "=" * 60)
    for i in range(n):
        print(Fore.GREEN + "🐈", end=" ")  # Gir alle kattene på samme linje
        output += "🐈 "  
    
    print("\n")  # Ny linje etter utskrift
    print(Fore.YELLOW + "=" * 60)
    return output  # Returnerer strengen for evt. videre bruk

def send_email(content): #Funksjon som sender output til en oppgitt epost.
    print(Fore.MAGENTA + "\nSEND SOM EPOST VIA GMAIL")

    email_sender = '' #Her må du skrive mailen din!
    email_password = ' '  # Her må du skrive app-passordet du opprettet!
    
    email_receiver = input(Fore.CYAN + "Til: ")
    
    bekreft = input(Fore.YELLOW + "Vil du sende eposten? (ja eller nei): ").strip().lower()
    if bekreft != "ja":
        print(Fore.YELLOW + "Epost ble ikke sendt.")
        return
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em.set_content(content) #Her henter jeg emojiene (content).

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Starter TLS
            smtp.login(email_sender, email_password)  # Logger inn
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(Fore.GREEN + "\nEposten er sendt!")
    except Exception as e:
        print(Fore.RED + f"Feil ved sending av epost: {e}")

if __name__ == "__main__":
    main()
