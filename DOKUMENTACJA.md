# 🌳 Drzewo decyzji ALT - Dokumentacja implementacji

## ✅ Status realizacji
Aplikacja została pomyślnie zaimplementowana i uruchomiona zgodnie z planem.

## 📋 Zrealizowane funkcjonalności

### 1. **Struktura drzewa decyzji**
- Implementacja pełnego drzewa decyzji W3C WAI dla atrybutu `alt`
- Logiczne przeprowadzenie użytkownika przez wszystkie pytania
- Dynamiczne wyświetlanie kolejnych kroków na podstawie odpowiedzi

### 2. **Pytania implementowane w aplikacji:**
1. **Czy obraz zawiera tekst?** (tak/nie)
   - Jeśli TAK → szczegółowe opcje dotyczące funkcji tekstu
   - Jeśli NIE → przejście do następnego pytania

2. **Jak funkcjonuje tekst w obrazie?** (tylko gdy obraz zawiera tekst)
   - Tekst jest obecny jako prawdziwy tekst w pobliżu
   - Tekst pokazywany tylko dla efektów wizualnych
   - Tekst ma specyficzną funkcję (ikona)
   - Tekst niedostępny w innej formie

3. **Czy obraz jest w linku/przycisku?** (tylko gdy nie zawiera tekstu)
   - Ocena czy obraz jest krytyczny dla zrozumienia funkcji

4. **Czy obraz wnosi znaczenie?**
   - Określenie czy obraz jest informacyjny czy dekoracyjny

5. **Jaki typ obrazu?** (gdy wnosi znaczenie)
   - Prosta grafika/fotografia
   - Wykres lub złożona informacja  
   - Redundantny do tekstu w pobliżu

6. **Czy obraz jest dekoracyjny?** (gdy nie wnosi znaczenia)

### 3. **Rekomendacje**
Każda ścieżka w drzewie prowadzi do konkretnej rekomendacji zawierającej:
- **Tytuł** - jasne określenie co robić
- **Kategoria** - typ obrazu zgodny z wytycznymi W3C
- **Opis** - szczegółowe wyjaśnienie
- **Przykład kodu HTML** - praktyczna implementacja
- **Link** - odnośnik do oficjalnej dokumentacji W3C

### 4. **Dostępność (WCAG 2.1)**
✅ **Nawigacja klawiaturą** - wszystkie elementy dostępne przez Tab  
✅ **Wysokie kontrasty** - kolory spełniające wymagania AA  
✅ **Semantyczne etykiety** - prawidłowe oznaczenie kontrolek  
✅ **Responsywność** - działanie na różnych urządzeniach  
✅ **Fokus** - widoczne oznaczenie aktywnego elementu  

### 5. **Interfejs użytkownika**
- **Panel boczny** z instrukcjami i przyciskiem resetowania
- **Główny obszar** z pytaniami i przyciskami radio
- **Strona wyników** z rekomendacją i podsumowaniem odpowiedzi
- **Emojis i ikony** dla lepszej orientacji wizualnej

## 🚀 Instrukcja uruchomienia

### Sposób 1: Przez VS Code Task
1. Otwórz projekt w VS Code
2. Naciśnij `Ctrl+Shift+P`
3. Wpisz "Tasks: Run Task"
4. Wybierz "Uruchom aplikację Streamlit"

### Sposób 2: Przez terminal
```bash
cd "c:\Users\jacza\alttree"
streamlit run app.py
```

### Sposób 3: Przez Python bezpośrednio
```bash
python -m streamlit run app.py
```

## 📁 Struktura projektu
```
alttree/
├── .streamlit/
│   └── config.toml          # Konfiguracja Streamlit
├── app.py                   # Główna aplikacja
├── requirements.txt         # Wymagane pakiety
├── style.css               # Style CSS dla WCAG
├── README_APP.md           # Dokumentacja aplikacji
├── readme.md               # Opis projektu (oryginalny)
└── .vscode/
    └── tasks.json          # Zadania VS Code
```

## 🔧 Technologie użyte
- **Python 3.13** - język programowania
- **Streamlit 1.28+** - framework webowy
- **Session State** - zarządzanie stanem aplikacji
- **WCAG 2.1** - standardy dostępności

## 🎯 Zgodność z wymaganiami
✅ **Streamlit** - aplikacja zbudowana w wymaganym frameworku  
✅ **Drzewo decyzji ALT** - pełna implementacja według W3C WAI  
✅ **Język polski** - wszystkie teksty w języku polskim  
✅ **WCAG** - interfejs zgodny z wytycznymi dostępności  
✅ **Interaktywność** - pytania tak/nie z dynamicznymi ścieżkami  

## 📱 Dostęp do aplikacji
Po uruchomieniu aplikacja będzie dostępna pod adresem:
**http://localhost:8501**

## 🔄 Możliwości rozwoju
- Dodanie więcej przykładów kodu
- Implementacja testów jednostkowych
- Dodanie eksportu rekomendacji do PDF
- Integracja z narzędziami do testowania dostępności
- Tryb ciemny dla lepszej dostępności

---
*Aplikacja została zrealizowana zgodnie z planem i wszystkimi wymaganiami projektowymi.*
