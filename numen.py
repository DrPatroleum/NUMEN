# Finalny pełny kod zintegrowany z prognozą roczną i kompatybilnością partnerską

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

# Prognozy roczne
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

# Kompatybilność partnerska
compatibility_matrix = {
    (1, 1): "Silna, ale może dojść do konfliktu o przywództwo.",
    (1, 2): "Uzupełniający się związek – lider i wspierający partner.",
    (1, 3): "Dużo energii i twórczości – świetna dynamika.",
    (2, 2): "Harmonia i bliskość, ale może brakować akcji.",
    (2, 3): "Delikatność i zabawa – związek pełen lekkości.",
    (3, 3): "Radość, lekkość i zabawa – wymarzone połączenie dusz artystycznych.",
}

# Interpretacje numerologiczne (fragment)
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
    }
}

# Funkcje numerologiczne
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

def get_personal_year_forecast(year_num):
    return personal_year_predictions.get(year_num, "Brak prognozy.")

def get_life_path_compatibility(life1, life2):
    key = tuple(sorted((life1, life2)))
    return compatibility_matrix.get(key, "Brak danych o tej parze liczbowej.")

# Główne uruchomienie
if __name__ == "__main__":
    print("=== NUMEROLOGIA AI: RAPORT ROZSZERZONY ===")
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
    print(f"💓 Liczba Duszy: {soul}")
    print(f"🎭 Liczba Osobowości: {persona}")
    print(f"\n📅 Rok osobisty: {personal}")
    print("🔮 Prognoza:", get_personal_year_forecast(personal))

    print(f"\n⚖️ Lekcje karmiczne:")
    print(karmic_lesson_grid(karma))
    for line in interpret_karmic_lessons(karma):
        print(" -", line)

    print("\n📐 Strzały Pitagorasa:")
    for i in range(1, 10):
        print(f"  {i}: {'●' * counts[i] if counts[i] > 0 else '–'}")
    print("\n✅ Obecne strzały:")
    for line in found:
        print(" -", line)
    print("\n❌ Brakujące strzały:")
    for line in missing:
        print(" -", line)

    # Kompatybilność partnerska
    print("\n💞 KOMPATYBILNOŚĆ PARTNERSKA")
    partner_name = input("Podaj imię i nazwisko partnera: ")
    partner_date = input("Podaj datę urodzenia partnera (YYYY-MM-DD): ")
    try:
        p_year, p_month, p_day = map(int, partner_date.split("-"))
        partner_life = calculate_life_path(p_day, p_month, p_year)
        print(f"\n❤️ Liczba Życia partnera ({partner_name}): {partner_life}")
        print("🤝 Interpretacja związku:")
        print(get_life_path_compatibility(life, partner_life))
    except ValueError:
        print("❌ Błędny format daty partnera.")
