from datetime import datetime

# Mapa liter
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

# Strzały Pitagorasa
pitagoras_arrow_definitions = {
    (1, 2, 3): "Strzała Intelektu – jasność myśli, analityczne podejście",
    (4, 5, 6): "Strzała Planowania – dobra organizacja, praktyczność",
    (7, 8, 9): "Strzała Emocji – intensywność emocjonalna, empatia",
    (1, 4, 7): "Strzała Praktyczności – twarde stąpanie po ziemi",
    (2, 5, 8): "Strzała Równowagi – harmonia ciała, umysłu i ducha",
    (3, 6, 9): "Strzała Ducha – duchowość, twórczość i empatia",
    (1, 5, 9): "Strzała Determinacji – silna wola i wytrwałość",
    (3, 5, 7): "Strzała Wizji – wyobraźnia, wizjonerstwo, kreatywność"
}

# Interpretacje lekcji karmicznych
karmic_lesson_meanings = {
    1: "Lekcja niezależności, asertywności i wyrażania siebie.",
    2: "Lekcja współpracy, cierpliwości i dyplomacji.",
    3: "Lekcja wyrażania emocji, radości i twórczości.",
    4: "Lekcja organizacji, systematyczności i pracy nad sobą.",
    5: "Lekcja elastyczności, wolności i panowania nad chaosem.",
    6: "Lekcja odpowiedzialności, opiekuńczości i rodziny.",
    7: "Lekcja zaufania, duchowości i wewnętrznego rozwoju.",
    8: "Lekcja władzy, zarządzania i stosunku do pieniędzy.",
    9: "Lekcja współczucia, altruizmu i akceptacji końców."
}

# Interpretacje numerologiczne (kontekstowe)
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
        11: "Masz potencjał przewodnika duchowego i inspiratora.",
        22: "Potrafisz realizować wielkie cele materialne dla dobra ogółu.",
        33: "Jesteś mistrzem uzdrawiania i bezwarunkowej miłości."
    },
    "Liczba Osobowości": {
        1: "Postrzegany jesteś jako niezależny i zdeterminowany.",
        2: "Sprawiasz wrażenie spokojnego i ugodowego.",
        3: "Inni widzą Cię jako osobę towarzyską i twórczą.",
        4: "Jesteś odbierany jako solidny, uporządkowany i praktyczny.",
        5: "Emanujesz energią, zmianą i otwartością.",
        6: "Wzbudzasz zaufanie jako osoba ciepła i opiekuńcza.",
        7: "Twoja osobowość jest tajemnicza, refleksyjna i poważna.",
        8: "Wyglądasz na kogoś pewnego siebie, ambitnego i konkretnego.",
        9: "Emanujesz duchowością, współczuciem i głębią.",
        11: "Widziany jesteś jako osoba natchniona i wizjonerska.",
        22: "Prezentujesz się jako silny strateg i lider budujący coś większego.",
        33: "Twoja obecność przynosi poczucie miłości, uzdrawiania i misji."
    },
    "Liczba Duszy": {
        1: "Wewnętrzna potrzeba niezależności i bycia liderem.",
        2: "Pragnienie harmonii, spokoju i współpracy.",
        3: "Głębokie potrzeby ekspresji, twórczości i radości.",
        4: "Potrzeba stabilizacji, porządku i bezpieczeństwa.",
        5: "Wewnętrzne pragnienie wolności i różnorodności doświadczeń.",
        6: "Silna potrzeba dawania miłości, opieki i poczucia obowiązku.",
        7: "Duchowe i intelektualne poszukiwania wewnętrzne.",
        8: "Pragnienie kontroli, osiągnięć i siły materialnej.",
        9: "Potrzeba służenia innym i niesienia pomocy.",
        11: "Potrzeba rozwijania intuicji i wyższej świadomości.",
        22: "Wewnętrzne dążenie do realizacji wielkich wizji.",
        33: "Potrzeba poświęcenia się dla dobra innych i duchowego przewodnictwa."
    },
    "Liczba Imienia": {
        1: "Masz wrodzony potencjał przywódczy i determinację.",
        2: "Twoja osobowość wyraża się przez współpracę i dyplomację.",
        3: "Jesteś twórczy, ekspresyjny i z łatwością komunikujesz się z innymi.",
        4: "Jesteś zorganizowany, praktyczny i lojalny.",
        5: "Elastyczny, energiczny i kochający zmiany.",
        6: "Twoja natura to troska, rodzina i obowiązek.",
        7: "Masz w sobie głębię duchową, analityczny umysł i samotnicze skłonności.",
        8: "Dążysz do sukcesu, jesteś zorganizowany i odpowiedzialny.",
        9: "Jesteś pełen empatii, mądrości i chcesz pomagać innym.",
        11: "Nosisz w sobie wibrację inspiracji, duchowej misji i geniuszu.",
        22: "Masz potencjał realizatora wielkich idei w praktyce.",
        33: "Twoja droga to służba innym, miłość bez granic i duchowa opieka."
    }
}

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

def calculate_arrow_counts(digits):
    counts = {i: 0 for i in range(1, 10)}
    for d in digits:
        if d in counts:
            counts[d] += 1
    return counts

def detect_pitagoras_arrows(counts):
    found = []
    missing = []
    for line in pitagoras_arrow_definitions:
        if all(counts[d] > 0 for d in line):
            found.append(pitagoras_arrow_definitions[line])
        elif all(counts[d] == 0 for d in line):
            missing.append("Brak " + pitagoras_arrow_definitions[line])
    return found, missing

def karmic_lessons(name):
    digits = [letter_to_number.get(c, 0) for c in name.upper() if c.isalpha()]
    return [n for n in range(1, 10) if n not in digits]

def karmic_lesson_grid(lessons):
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display = "\n📐 Siatka Lekcji Karmicznych:\n"
    for row in grid:
        display += "  ".join(f"{n}:{'✖' if n in lessons else '✔'}" for n in row) + "\n"
    return display

def interpret_karmic_lessons(lessons):
    if not lessons:
        return ["Brak – wszystkie wibracje obecne"]
    return [f"{n}: {karmic_lesson_meanings[n]}" for n in lessons]

def get_contextual_meaning(n, aspect):
    return number_meanings_contextual.get(aspect, {}).get(n, "Brak interpretacji.")

if __name__ == "__main__":
    print("=== NUMEROLOGIA AI Z PITAGORASEM I LEKCJAMI KARMICZNYMI ===")
    name = input("Podaj imię i nazwisko: ")
    date = input("Podaj datę urodzenia (YYYY-MM-DD): ")

    try:
        year, month, day = map(int, date.split("-"))
    except ValueError:
        print("Błędny format.")
        exit()

    life = calculate_life_path(day, month, year)
    exp = name_number(name)
    soul = soul_number(name)
    persona = personality_number(name)
    personal = personal_year(day, month)
    karma = karmic_lessons(name)

    digits = extract_digits_from_date(day, month, year)
    counts = calculate_arrow_counts(digits)
    found, missing = detect_pitagoras_arrows(counts)

    print(f"\n📌 Liczba Życia: {life}")
    print("Znaczenie:", get_contextual_meaning(life, "Liczba Życia"))

    print(f"\n🧠 Liczba Imienia: {exp}")
    print("Znaczenie:", get_contextual_meaning(exp, "Liczba Imienia"))

    print(f"\n💓 Liczba Duszy: {soul}")
    print("Znaczenie:", get_contextual_meaning(soul, "Liczba Duszy"))

    print(f"\n🎭 Liczba Osobowości: {persona}")
    print("Znaczenie:", get_contextual_meaning(persona, "Liczba Osobowości"))

    print(f"\n📅 Rok osobisty: {personal}")
    print("Znaczenie:", get_contextual_meaning(personal, "Liczba Życia"))

    print(f"\n⚖️ Lekcje karmiczne:")
    print(karmic_lesson_grid(karma))
    for line in interpret_karmic_lessons(karma):
        print(" -", line)

    print("\n📐 Strzały Pitagorasa (z daty urodzenia):")
    for i in range(1, 10):
        print(f"  {i}: {'●' * counts[i] if counts[i] > 0 else '–'}")

    print("\n✅ Obecne strzały:")
    for line in found:
        print(" -", line)

    print("\n❌ Brakujące strzały:")
    for line in missing:
        print(" -", line)
