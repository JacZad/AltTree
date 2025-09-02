# Drzewo decyzji ALT - Aplikacja Streamlit

Ta aplikacja implementuje interaktywne drzewo decyzji dla atrybutu `alt` w elementach `<img>` zgodnie z wytycznymi W3C WAI.

## Instalacja

1. Zainstaluj wymagane pakiety:

```bash
pip install -r requirements.txt
```

2. Uruchom aplikację:

```bash
streamlit run app.py
```

## Funkcjonalność

Aplikacja prowadzi użytkownika przez serie pytań pomagających określić odpowiednią wartość atrybutu `alt` dla obrazów:

1. Czy obraz zawiera tekst?
2. Czy obraz jest używany w linku lub przycisku?
3. Czy obraz wnosi znaczenie do strony?
4. Czy obraz jest wyłącznie dekoracyjny?

**Nowe funkcje:**
- **Przycisk "Dalej"** - użytkownik musi potwierdzić wybór przed przejściem dalej
- **Pasek postępu** - pokazuje jak daleko jest w procesie decyzyjnym
- **Przycisk "Cofnij"** - możliwość powrotu do poprzedniego pytania
- **Brak domyślnych wyborów** - użytkownik musi świadomie dokonać wyboru

Na podstawie odpowiedzi aplikacja dostarcza konkretne rekomendacje zgodne z wytycznymi dostępności.

## Zgodność z WCAG

Aplikacja została zaprojektowana z uwzględnieniem wytycznych WCAG 2.1:

- Dostępność za pomocą klawiatury
- Odpowiedni kontrast kolorów
- Czytelne etykiety
- Semantyczna struktura HTML
