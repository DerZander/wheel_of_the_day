# Wheel of Life

Dieses Tool ist ein interaktiver Lebens-Kompass, mit dem du verschiedene Lebensbereiche bewerten kannst. Die Bereiche und ihre Optionen sind in `wheel_of_life.py` definiert. Die App visualisiert deine Auswahl als Radar-Chart.

## Features
- Für jeden Lebensbereich (z.B. Freizeit, Finanzen, Gesundheit) gibt es mehrere Optionen mit positiver oder negativer Gewichtung.
- Du kannst für jeden Tag oder Zeitraum ankreuzen, was du erlebt oder erreicht hast.
- Die Punkte werden pro Bereich normiert (maximal 10, negative Werte werden abgezogen).
- Die Ergebnisse werden als übersichtliches Radardiagramm angezeigt.

## Dateien
- **kompass.py**: Streamlit-App, die die Benutzeroberfläche und die Visualisierung bereitstellt.
- **wheel_of_life.py**: Enthält das Dictionary mit allen Bereichen und deren Optionen (inklusive Emojis und Gewichtungen).

## Installation
1. Stelle sicher, dass Python 3.8+ installiert ist.
2. Installiere die benötigten Pakete:
   ```
   pip install streamlit plotly
   ```

## Nutzung
Starte die App mit:
```
streamlit run kompass.py
```

## Anpassung
- Du kannst die Bereiche und Optionen in `wheel_of_life.py` beliebig anpassen (z.B. weitere Bereiche, andere Gewichtungen, neue Emojis).
- Die App ist so gestaltet, dass sie sich automatisch an die Inhalte von `wheel_of_life.py` anpasst.

## Beispiel-Screenshot
![{5495BB94-1E98-4F90-B6D5-63BC1B98E5BC}](https://github.com/user-attachments/assets/35b2bd89-9644-4805-94fc-da839c3708ae)


---
Viel Spaß beim Reflektieren und Visualisieren deines Lebens-Kompasses!
