import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

# --- MAPA LITER ---
letter_to_number = {
    **dict.fromkeys(['A', 'J', 'S'], 1),
    **dict.fromkeys(['B', 'K', 'T'], 2),
    **dict.fromkeys(['C', 'L', 'U'], 3),
    **dict.fromkeys(['D', 'M', 'V'], 4),
    **dict.fromkeys(['E', 'N', 'W'], 5),
    **dict.fromkeys(['F', 'O', 'X'], 6),
    **dict.fromkeys(['G', 'P', 'Y'], 7),
    **dict.fromkeys(['H', 'Q', 'Z'], 8),
    **dict.fromkeys(['I', 'R'], 9),
}

# --- LEKCJE KARMICZNE ---
karmic_lesson_meanings = {
    1: "NIEZALEŻNOŚĆ, ASERTYWNOŚĆ\n - masz trudności w podejmowaniu decyzji, odczuwasz brak wiary w siebie, zdarza Ci się uległość wobec innych",
    2: "WSPÓŁPRACA, DYPLOMACJA\n - masz trudności w pracy zespołowej i skłonność do konfliktów, bywasz nadwrażliwy",
    3: "EKSPRESJA, TWÓRCZOŚĆ\n - masz trudności z wyrażaniem emocji, zahamowania w mowie i sztuce",
    4: "DYSCYPLINA, ORGANIZACJA\n - zauważasz chaos w życiu codziennym, masz problemy z konsekwencją i strukturą",
    5: "WOLNOŚĆ, ELASTYCZNOŚĆ\n - odczuwasz strach przed zmianami, kontrolujesz siebie lub innych",
    6: "ODPOWIEDZIALNOŚĆ, RODZINA\n - unikasz zobowiązań, masz lęk przed bliskością lub opieką",
    7: "DUCHOWOŚĆ, INTROSPEKCJA\n - cierpisz na brak zaufania do siebie, jesteś powierzchowny, unikasz samotności",
    8: "WŁADZA, PIENIĄDZE\n - masz problemy z zarządzaniem finansami, unikasz odpowiedzialności za sukces",
    9: "ALTRUIZM, ZAKOŃCZENIA\n - masz trudności w opuszczaniu przeszłości, zdarza Ci się brak empatii i zaborczość"
}

# --- PROGNOZY ROCZNE ---
personal_year_predictions = {
    1: "Nowe początki, inicjatywy, samodzielność.",
    2: "Współpraca, cierpliwość, relacje, przygotowanie.",
    3: "Ekspresja, radość, kreatywność, towarzyskość.",
    4: "Praca, struktura, obowiązki, cierpliwość.",
    5: "Zmiany, wolność, przygody, elastyczność.",
    6: "Rodzina, odpowiedzialność, domowe sprawy, harmonia.",
    7: "Introspekcja, duchowość, analiza, wyciszenie.",
    8: "Ambicje, sukces zawodowy, zarządzanie finansami.",
    9: "Zakończenia, podsumowania, służba innym, transformacja."
}

# --- INTERPRETACJE ---
number_meanings_contextual = {
    "Liczba Życia": {
        1: "Twoje życie to ścieżka lidera, samodzielność i ambicja.",
        2: "Twoje życie wymaga współpracy, empatii i dyplomacji.",
        3: "Masz naturalny dar ekspresji, radości i kreatywności.",
        4: "Twoje życie opiera się na strukturze, pracy i wytrwałości.",
        5: "Jesteś stworzony do zmian, przygód i wolności.",
        6: "Twoja misja to odpowiedzialność, rodzina i troska o innych.",
        7: "Masz drogę duchową, skłonność do introspekcji i analizy.",
        8: "Twoja ścieżka życiowa dotyczy sukcesu materialnego i organizacji.",
        9: "Twoją misją jest altruizm, humanitaryzm i służba.",
        11: "Jesteś nauczycielem duchowym, cechuje Cię intuicja, inspiracja i przewodnictwo duchowe. Twoje życie jest pełne intensywnych doświadczeń i potrzeby pomagania innym przez światło wewnętrzne.",
        22: "Masz ogromny potencjał materializacji wizji oraz zdolność do tworzenia struktur dla dobra wielu.",
        33: "Odczuwalna jest wibracja bezwarunkowej miłości, współczucia i służby. Życie poświęcasz innym, często przez trudne osobiste doświadczenia."     
    },
    "Liczba Imienia": {
        1: "Jesteś liderem, urodzonym do podejmowania decyzji.",
        2: "Jesteś mediatorem, wspierasz innych w harmonii.",
        3: "Masz talent do wyrażania siebie i kreatywności.",
        4: "Jesteś rzetelny, dokładny i systematyczny.",
        5: "Uwielbiasz zmiany, ruch i różnorodność.",
        6: "Cechuje Cię odpowiedzialność i potrzeba troski o innych.",
        7: "Masz głęboki umysł i filozoficzne podejście do życia.",
        8: "Masz dryg do interesów i zarządzania.",
        9: "Jesteś idealistą, chętnie niesiesz pomoc innym.",
        11: "Masz potencjał inspirować przez słowo i obecność. Możesz być natchnieniem dla innych bez użycia siły.",
        22: "Twoje imię niesie wibrację przywództwa i organizacji wielkich idei, nawet jeśli wydajesz się cichy.",
        33: "Twoje imię rezonuje z energią uzdrawiania, ciepła i służby, nawet jeśli nie jesteś tego świadom."
    },
    "Liczba Duszy": {
        1: "Pragniesz niezależności i bycia rozpoznawanym.",
        2: "Twoja dusza dąży do harmonii i współpracy.",
        3: "Pragniesz radości, ekspresji i bycia wysłuchanym.",
        4: "Potrzebujesz stabilizacji, rutyny i porządku.",
        5: "Twoja dusza pragnie wolności i nowych doświadczeń.",
        6: "Masz potrzebę opiekowania się i kochania innych.",
        7: "Dążysz do duchowości i wewnętrznego spokoju.",
        8: "Pragniesz sukcesu, autorytetu i bezpieczeństwa.",
        9: "Twoja dusza pragnie pomagać i służyć ludzkości.",
        11: "Twoja dusza pragnie wyższego celu, transcendencji i przekraczania ego.",
        22: "Wewnątrz nosisz potrzebę tworzenia czegoś większego niż Ty sam – dla dobra ogółu.",
        33: "Głęboka potrzeba bezwarunkowej miłości, harmonii i uzdrawiania emocjonalnego siebie i innych."
    },
    "Liczba Osobowości": {
        1: "Jesteś postrzegany jako pewny siebie lider.",
        2: "Sprawiasz wrażenie uprzejmej i taktowniej osoby.",
        3: "Wydajesz się radosny, towarzyski i kreatywny.",
        4: "Emanujesz solidnością i odpowiedzialnością.",
        5: "Jesteś dynamiczny i otwarty na nowe.",
        6: "Postrzegany jesteś jako troskliwy i rodzinny.",
        7: "Wydajesz się tajemniczy i intelektualny.",
        8: "Robisz wrażenie silnego i zorganizowanego.",
        9: "Jesteś odbierany jako współczujący i mądry.",
        11: "Jesteś postrzegany jako osoba charyzmatyczna, nieuchwytna, duchowa. Inni mogą czuć Twoją aurę nawet bez słów.",
        22: "Robisz wrażenie osoby potężnej, stabilnej, zorganizowanej, nawet jeśli w środku jesteś wrażliwy.",
        33: "Jesteś odbierany jako uzdrowiciel, opiekun, ktoś, kto emanuje spokojem i empatią."
    }
}

# --- FUNKCJE NUMEROLOGICZNE ---
def reduce_number(n):
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(d) for d in str(n))
    return n

def calculate_life_path(day, month, year):
    return reduce_number(reduce_number(day) + reduce_number(month) + reduce_number(year))

def name_number(name):
    return reduce_number(sum(letter_to_number.get(c, 0) for c in name.upper() if c.isalpha()))

def soul_number(name):
    return reduce_number(sum(letter_to_number.get(c, 0) for c in name.upper() if c in 'AEIOUY'))

def personality_number(name):
    return reduce_number(sum(letter_to_number.get(c, 0) for c in name.upper() if c.isalpha() and c not in 'AEIOUY'))

def personal_year(day, month, year=None):
    if not year:
        year = datetime.now().year
    return reduce_number(reduce_number(day) + reduce_number(month) + reduce_number(year))

def extract_digits_from_date(day, month, year):
    return [int(d) for d in f"{day:02d}{month:02d}{year}"]

def get_contextual_meaning(n, aspect):
    return number_meanings_contextual.get(aspect, {}).get(n, "Brak interpretacji.")

def get_personal_year_forecast(year_num):
    return personal_year_predictions.get(year_num, "Brak prognozy.")

# --- GUI ---
class NumerologyApp:
    def __init__(self, master):
        self.master = master
        master.title("Numerologia AI – Profil Osobisty")
        master.geometry("700x600")
        master.configure(bg="#f9f2ec")

        tk.Label(master, text="Imię i nazwisko:", bg="#f9f2ec", font=("Georgia", 12)).pack(pady=(10, 0))
        self.name_entry = tk.Entry(master, font=("Georgia", 12), width=40)
        self.name_entry.pack(pady=5)

        tk.Label(master, text="Data urodzenia (YYYY-MM-DD):", bg="#f9f2ec", font=("Georgia", 12)).pack(pady=(10, 0))
        self.dob_entry = tk.Entry(master, font=("Georgia", 12), width=20)
        self.dob_entry.pack(pady=5)

        self.generate_btn = tk.Button(master, text="Generuj raport", font=("Georgia", 12, "bold"), bg="#d1c4e9", command=self.generate_report)
        self.generate_btn.pack(pady=20)

        self.output = tk.Text(master, wrap="word", font=("Georgia", 11), bg="#fffdf7", height=20)
        self.output.pack(padx=10, pady=10, fill="both", expand=True)

        self.save_btn = tk.Button(master, text="Zapisz raport do pliku", font=("Georgia", 11), bg="#b2dfdb", command=self.save_report)
        self.save_btn.pack(pady=(0, 10))

    def generate_report(self):
        name = self.name_entry.get()
        date = self.dob_entry.get()

        try:
            year, month, day = map(int, date.split("-"))
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawną datę w formacie RRRR-MM-DD")
            return

        life = calculate_life_path(day, month, year)
        exp = name_number(name)
        soul = soul_number(name)
        persona = personality_number(name)
        personal = personal_year(day, month)
        digits = extract_digits_from_date(day, month, year)

        report = f"Imię i nazwisko: {name}\nData urodzenia: {date}\n\n"
        report += f"📌 Liczba Życia: {life}\n{get_contextual_meaning(life, 'Liczba Życia')}\n\n"
        report += f"🧠 Liczba Imienia: {exp}\n{get_contextual_meaning(exp, 'Liczba Imienia')}\n\n"
        report += f"💓 Liczba Duszy: {soul}\n{get_contextual_meaning(soul, 'Liczba Duszy')}\n\n"
        report += f"🎭 Liczba Osobowości: {persona}\n{get_contextual_meaning(persona, 'Liczba Osobowości')}\n\n"        
        report += f"📅 Rok osobisty: {personal}\n🔮 Prognoza na ten rok: {get_personal_year_forecast(personal)}\n\n"

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, report)

    def save_report(self):
        report_text = self.output.get("1.0", tk.END).strip()
        if not report_text:
            messagebox.showinfo("Brak danych", "Najpierw wygeneruj raport")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(report_text)
            messagebox.showinfo("Zapisano", f"Raport zapisany do {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumerologyApp(root)
    root.mainloop()
