import streamlit as st

def load_css(file_name):
    """Wczytuje plik CSS i dodaje go do aplikacji."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def initialize_session_state():
    """Inicjalizacja stanu sesji."""
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 'start'
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'recommendation' not in st.session_state:
        st.session_state.recommendation = None

def reset_decision_tree():
    """Resetuje drzewo decyzji do stanu początkowego."""
    st.session_state.current_step = 'start'
    st.session_state.answers = {}
    st.session_state.recommendation = None

def get_recommendation(answers):
    """Zwraca rekomendację na podstawie odpowiedzi."""
    
    # Logika drzewa decyzji
    if answers.get('contains_text') == 'tak':
        if answers.get('text_function') == 'tekst_obok':
            return {
                'title': 'Użyj pustego atrybutu alt',
                'description': 'Gdy tekst z obrazu jest również obecny jako prawdziwy tekst w pobliżu, użyj pustego atrybutu alt="".',
                'category': 'Obrazy dekoracyjne',
                'example': '<img src="logo.png" alt="">',
                'link': 'https://www.w3.org/WAI/tutorials/images/decorative/'
            }
        elif answers.get('text_function') == 'efekt_wizualny':
            return {
                'title': 'Użyj pustego atrybutu alt',
                'description': 'Gdy tekst jest pokazywany tylko dla efektów wizualnych, użyj pustego atrybutu alt="".',
                'category': 'Obrazy dekoracyjne',
                'example': '<img src="fancy-text.png" alt="">',
                'link': 'https://www.w3.org/WAI/tutorials/images/decorative/'
            }
        elif answers.get('text_function') == 'funkcja_specyficzna':
            return {
                'title': 'Opisz funkcję obrazu',
                'description': 'Gdy tekst ma specyficzną funkcję (np. ikona), użyj atrybutu alt do komunikowania funkcji obrazu.',
                'category': 'Obrazy funkcjonalne',
                'example': '<img src="search-icon.png" alt="Szukaj">',
                'link': 'https://www.w3.org/WAI/tutorials/images/functional/'
            }
        elif answers.get('text_function') == 'tekst_niedostepny':
            return {
                'title': 'Dodaj tekst z obrazu do alt',
                'description': 'Gdy tekst z obrazu nie jest dostępny w innej formie, użyj atrybutu alt do włączenia tekstu z obrazu.',
                'category': 'Obrazy tekstowe',
                'example': '<img src="important-text.png" alt="W dniach 1-4 września nasze biuro jest nieczynne.">',
                'link': 'https://www.w3.org/WAI/tutorials/images/textual/'
            }
        elif answers.get('text_function') == 'etykieta_tekstowa':
            if answers.get('link_button') == 'tak':
                return {
                    'title': 'Przepisz dokładnie etykietę do atrybutu alt',
                    'description': 'Jeśli grafika jest etykietą tekstową i jest używana jako link lub przycisk, wartość atrybutu alt powinna być dokładnie taka sama jak tekst na grafice.',
                    'category': 'Obrazy tekstowe (etykieta w linku/przycisku)',
                    'example': '<a href="bip.html"><img src="bip.png" alt="BIP"></a>',
                    'link': 'https://www.w3.org/WAI/tutorials/images/functional/'
                }
            else:
                return {
                    'title': 'Dodaj tekst z grafiki jako alt',
                    'description': 'Jeśli grafika jest etykietą tekstową, np. "BIP", użyj tego tekstu jako wartości atrybutu alt.',
                    'category': 'Obrazy tekstowe (etykieta)',
                    'example': '<img src="bip.png" alt="BIP">',
                    'link': 'https://www.w3.org/WAI/tutorials/images/textual/'
                }
    
    # Kontynuuj jeśli obraz nie zawiera tekstu
    if answers.get('contains_text') == 'nie':
        if answers.get('link_button') == 'tak':
            return {
                'title': 'Opisz cel linku lub akcję',
                'description': 'Użyj atrybutu alt do komunikowania miejsca docelowego linku lub wykonywanej akcji.',
                'category': 'Obrazy funkcjonalne',
                'example': '<img src="download.png" alt="Pobierz raport PDF">',
                'link': 'https://www.w3.org/WAI/tutorials/images/functional/'
            }
        
        if answers.get('link_button') == 'nie' and answers.get('contributes_meaning') == 'tak':
            if answers.get('image_type') == 'prosta_grafika':
                return {
                    'title': 'Krótki opis obrazu',
                    'description': 'Użyj krótkiego opisu obrazu w atrybucie alt, który przekazuje znaczenie.',
                    'category': 'Obrazy informacyjne',
                    'example': '<img src="chart.png" alt="Wykres pokazujący wzrost sprzedaży o 25%">',
                    'link': 'https://www.w3.org/WAI/tutorials/images/informative/'
                }
            elif answers.get('image_type') == 'graf_zlozony':
                return {
                    'title': 'Dodaj informacje gdzie indziej',
                    'description': 'Opisz tekstowo informacje zawarte w obrazie gdzieś indziej na stronie.',
                    'category': 'Obrazy złożone',
                    'example': '<img src="complex-chart.png" alt="Szczegółowy wykres - opis poniżej">',
                    'link': 'https://www.w3.org/WAI/tutorials/images/complex/'
                }
            elif answers.get('image_type') == 'redundantny':
                return {
                    'title': 'Użyj pustego atrybutu alt',
                    'description': 'Gdy obraz pokazuje taką samą treść, co tekst w pobliżu, użyj pustego atrybutu alt="".',
                    'category': 'Obrazy funkcjonalne (redundantne)',
                    'example': '<img src="logo.png" alt="">',
                    'link': 'https://www.w3.org/WAI/tutorials/images/functional/'
                }
        
        if answers.get('contributes_meaning') == 'nie' and answers.get('decorative') == 'tak':
            return {
                'title': 'Użyj pustego atrybutu alt',
                'description': 'Dla obrazów czysto dekoracyjnych lub nie przeznaczonych do oglądania przez użytkowników, użyj pustego atrybutu alt="".',
                'category': 'Obrazy dekoracyjne',
                'example': '<img src="decoration.png" alt="">',
                'link': 'https://www.w3.org/WAI/tutorials/images/decorative/'
            }
    
    # Domyślna rekomendacja
    return {
        'title': 'Przeczytaj dokumentację i zdecyduj',
        'description': 'To drzewo decyzji nie obejmuje wszystkich przypadków. Aby uzyskać szczegółowe informacje o dostarczaniu alternatyw tekstowych, zapoznaj się z samouczkiem dotyczącym obrazów.',
        'category': 'Przypadek nieobjęty',
        'example': '',
        'link': 'https://www.w3.org/WAI/tutorials/images/'
    }

def render_question(question_id, title, options):
    """Renderuje pytanie z opcjami tak/nie lub wyborem."""
    st.subheader(title)
    
    # Użyj radio buttons dla lepszej dostępności
    answer = st.radio(
        label=title,
        options=options,
        key=f"radio_{question_id}",
        label_visibility="collapsed",
        index=None  # Brak domyślnego wyboru
    )
    
    # Dodaj przycisk "Dalej" tylko gdy użytkownik dokonał wyboru
    if answer is not None:
        if st.button("➡️ Dalej", key=f"next_{question_id}", type="primary"):
            return answer
    
    return None

def main():
    """Główna funkcja aplikacji."""
    
    # Konfiguracja strony
    st.set_page_config(
        page_title="Drzewo decyzji ALT",
        page_icon="🌳",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Wczytanie stylów CSS
    load_css("style.css")
    
    # Inicjalizacja stanu sesji
    initialize_session_state()
    
    # Nagłówek
    st.title("🌳 Drzewo decyzji ALT")
    st.markdown("*Interaktywne narzędzie do określania odpowiedniego atrybutu alt dla obrazów*")
    
    # Informacje w bocznym panelu
    with st.sidebar:
        st.header("ℹ️ Informacje")
        st.markdown("""
        To narzędzie pomoże Ci określić odpowiednią wartość atrybutu `alt` 
        dla elementów `<img>` zgodnie z wytycznymi dostępności W3C WAI.
        
        **Instrukcje:**
        1. Odpowiedz na pytania krok po kroku
        2. Wybieraj opcje najlepiej opisujące Twój obraz
        3. Kliknij "Dalej" aby przejść do następnego pytania
        4. Otrzymasz konkretną rekomendację
        """)
        
        # Pokaż postęp
        steps = ['start', 'text_function', 'link_button', 'contributes_meaning', 'image_type', 'decorative', 'result']
        current_index = steps.index(st.session_state.current_step) if st.session_state.current_step in steps else 0
        
        if st.session_state.current_step != 'start':
            st.markdown(f"**Postęp:** {current_index}/{len(steps)-1}")
            st.progress(current_index / (len(steps)-1))
        
        if st.button("🔄 Rozpocznij od nowa", type="secondary"):
            reset_decision_tree()
            st.rerun()
        
        # Przycisk cofnij (gdy nie jesteśmy na początku)
        if st.session_state.current_step != 'start' and st.session_state.current_step != 'result':
            if st.button("⬅️ Cofnij", type="secondary"):
                # Logika cofania się
                if st.session_state.current_step == 'text_function':
                    st.session_state.current_step = 'start'
                elif st.session_state.current_step == 'link_button':
                    st.session_state.current_step = 'start'
                elif st.session_state.current_step == 'contributes_meaning':
                    st.session_state.current_step = 'link_button'
                elif st.session_state.current_step == 'image_type':
                    st.session_state.current_step = 'contributes_meaning'
                elif st.session_state.current_step == 'decorative':
                    st.session_state.current_step = 'contributes_meaning'
                
                # Usuń ostatnią odpowiedź
                if st.session_state.answers:
                    last_key = list(st.session_state.answers.keys())[-1]
                    del st.session_state.answers[last_key]
                
                st.rerun()
    
    # Główna logika aplikacji
    if st.session_state.current_step == 'start':
        st.markdown("### Rozpocznij analizę obrazu")
        st.markdown("Odpowiedz na poniższe pytania, aby otrzymać rekomendację dotyczącą atrybutu alt.")
        
        answer = render_question(
            "contains_text",
            "Czy obraz zawiera głównie tekst?",
            ["tak", "nie"]
        )
        
        if answer:
            st.session_state.answers['contains_text'] = answer
            if answer == 'tak':
                st.session_state.current_step = 'text_function'
            else:
                st.session_state.current_step = 'link_button'
            st.rerun()
    
    elif st.session_state.current_step == 'text_function':
        answer = render_question(
            "text_function",
            "Czym jest ten tekst w obrazie?",
            [
                "tekst_obok - tekst jest także obecny jako prawdziwy tekst w pobliżu",
                "efekt_wizualny - tekst jest pokazywany tylko dla efektów wizualnych, na przykład stos książek z tytułami na grzbietach", 
                "funkcja_specyficzna - tekst ma specyficzną funkcję (np. ikona)",
                "tekst_niedostepny - tekst z obrazu nie jest dostępny w tekście obok",
                "etykieta_tekstowa - grafika jest etykietą tekstową, na przykład 'BIP'"
            ]
        )
        
        if answer:
            st.session_state.answers['text_function'] = answer.split(' - ')[0]
            st.session_state.recommendation = get_recommendation(st.session_state.answers)
            st.session_state.current_step = 'result'
            st.rerun()
    
    elif st.session_state.current_step == 'link_button':
        answer = render_question(
            "link_button",
            "Czy obraz jest używany w linku lub przycisku?",
            ["tak", "nie"]
        )
        
        if answer:
            st.session_state.answers['link_button'] = answer
            if answer == 'tak':
                st.session_state.recommendation = get_recommendation(st.session_state.answers)
                st.session_state.current_step = 'result'
            else:
                st.session_state.current_step = 'contributes_meaning'
            st.rerun()
    
    elif st.session_state.current_step == 'contributes_meaning':
        answer = render_question(
            "contributes_meaning",
            "Czy obraz dodaje jakieś informacje, których nie ma w tekście obok?",
            ["tak", "nie"]
        )
        
        if answer:
            st.session_state.answers['contributes_meaning'] = answer
            if answer == 'tak':
                st.session_state.current_step = 'image_type'
            else:
                st.session_state.current_step = 'decorative'
            st.rerun()
    
    elif st.session_state.current_step == 'image_type':
        answer = render_question(
            "image_type",
            "Jaki to jest rodzaj obrazu?",
            [
                "prosta_grafika - prosta grafika lub fotografia",
                "graf_zlozony - wykres lub złożona informacja",
                "powtórzony - pokazuje treść powtarzającą informacje z tekstu w pobliżu"
            ]
        )
        
        if answer:
            st.session_state.answers['image_type'] = answer.split(' - ')[0]
            st.session_state.recommendation = get_recommendation(st.session_state.answers)
            st.session_state.current_step = 'result'
            st.rerun()
    
    elif st.session_state.current_step == 'decorative':
        answer = render_question(
            "decorative",
            "Czy obraz jest czysto dekoracyjny lub nieprzeznaczony do oglądania przez użytkowników?",
            ["tak", "nie"]
        )
        
        if answer:
            st.session_state.answers['decorative'] = answer
            st.session_state.recommendation = get_recommendation(st.session_state.answers)
            st.session_state.current_step = 'result'
            st.rerun()
    
    elif st.session_state.current_step == 'result':
        if st.session_state.recommendation:
            rec = st.session_state.recommendation
            
            # Wyświetl rekomendację
            st.success("✅ Rekomendacja została wygenerowana!")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"### {rec['title']}")
                st.markdown(f"**Kategoria:** {rec['category']}")
                st.markdown(rec['description'])
                
                if rec['example']:
                    st.markdown("**Przykład:**")
                    st.code(rec['example'], language='html')
                
                if rec['link']:
                    st.markdown(f"[📚 Więcej informacji]({rec['link']})")
            
            with col2:
                st.markdown("### 📋 Podsumowanie odpowiedzi")
                for key, value in st.session_state.answers.items():
                    st.markdown(f"**{key}:** {value}")
            
            # Przycisk do rozpoczęcia od nowa
            if st.button("🔄 Analizuj kolejny obraz", type="primary"):
                reset_decision_tree()
                st.rerun()
    
    # Stopka z informacjami o dostępności
    st.markdown("---")
    st.markdown("Byłem tu. Jacek Zadrożny")

if __name__ == "__main__":
    main()
