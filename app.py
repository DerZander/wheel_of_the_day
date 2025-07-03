import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

wheel_of_life = {
    "Freizeit": {
        "🎮 Konnte zoocken": 1,
        "🎬 Konnte Filme schauen": 1,
        "📺 Konnte Serien schauen": 1,
        "🎵 Konnte Musik hören": 1,
        "🌳 Konnte Zeit in der Natur verbringen": 2,
        "📱 Nur am Handy verbracht": -2,
        "😑 Langeweile gehabt": -1,
    },
    "Arbeit & Karriere": {
        "💼 Konnte arbeiten": 2,
        "📚 Konnte lernen": 2,
        "🎨 Konnte kreativ sein": 2,
        "✅ Konnte Projekte abschließen": 2,
        "🧘 Konnte entspannen": 1,
        "⏳ Arbeit aufgeschoben": -2,
        "❌ Fehler gemacht": -1,
    },
    "Persönliche Wachstum": {
        "📖 Konnte lesen": 2,
        "📚 Konnte lernen": 2,
        "✍️ Konnte schreiben": 2,
        "🎨 Konnte kreativ sein": 2,
        "🤔 Konnte reflektieren": 2,
        "⏰ Keine Zeit für Entwicklung": -2,
        "😕 Unzufrieden mit Fortschritt": -1,
    },
    "Wohlbefinden": {
        "🧘 Konnte entspannen": 2,
        "🧘‍♂️ Konnte meditieren": 2,
        "😴 Konnte ausreichend schlafen": 2,
        "🎨 Konnte kreativ sein": 2,
        "📖 Konnte lesen": 2,
        "😰 Gestresst gefühlt": -2,
        "🌙 Zu wenig Schlaf": -1,
    },
    "Gesundheit & Fitness": {
        "🏃‍♂️ Konnte joggen": 2,
        "🧘‍♀️ Konnte Yoga machen": 2,
        "🧘 Konnte meditieren": 2,
        "🥗 Konnte gesund essen": 2,
        "📋 Essen getrackt": 2,
        "🍔 Fast Food gegessen": -2,
        "🛋️ Kein Sport gemacht": -1,
    },
    "Komfortzone": {
        "🆕 Konnte neue Dinge ausprobieren": 2,
        "💪 Konnte mich Herausforderungen stellen": 2,
        "😨 Konnte Ängste überwinden": 2,
        "🗣️ Konnte Feedback annehmen": 2,
        "🔄 Konnte aus Fehlern lernen": 2,
        "🙈 Neues vermieden": -2,
        "😟 Aus Angst zurückgezogen": -1,
    },
    "Werte gelebt": {
        "🤝 Ehrlich gewesen": 2,
        "🤲 Hilfsbereit gewesen": 2,
        "🧑‍💼 Verantwortung übernommen": 2,
        "🙏 Respektvoll gehandelt": 2,
        "🌱 Nachhaltig gehandelt": 2,
        "🚫 Werte ignoriert": -2,
        "🙃 Unaufrichtig gewesen": -1,
    },
    "Beziehung & Liebe": {
        "💋 Guten Morgen Kuss gegeben": 2,
        "💋 Guten Abend Kuss gegeben": 2,
        "❤️ Zeit mit Partner verbracht": 2,
        "💬 Offen kommuniziert": 2,
        "😄 Spaß gehabt": 2,
        "💔 Streit gehabt": -2,
        "🙄 Wenig Aufmerksamkeit geschenkt": -1,
    },
    "Sozialleben": {
        "👫 Konnte Freunde treffen": 2,
        "👨‍👩‍👧‍👦 Konnte Familie treffen": 2,
        "🧑‍🤝‍🧑 Konnte neue Leute kennenlernen": 2,
        "🗣️ Gute Gespräche geführt": 2,
        "🤗 Jemandem geholfen": 2,
        "😡 Streit mit Freunden": -2,
        "😔 Einsam gefühlt": -1,
    },
    "Finanzen": {
        "🤑 Kein Geld ausgegeben": 5,
        "💳 Konnte Rechnungen bezahlen": 2,
        "💰 Konnte Geld sparen": 2,
        "📈 Konnte Geld investieren": 2,
        "💵 Konnte Geld verdienen": 2,
        "📊 Ausgaben getrackt": 2,
        "💸 Geld verschwendet": -3,
    },
}

def page_kompass():
    st.title("Wheel of Life Kompass")
    st.write("Setze für jede Option ein Häkchen. Die Punkte werden entsprechend der Option gezählt (max. 10 pro Bereich, negative Werte werden abgezogen):")

    with st.sidebar:
        values = []
        bereiche = list(wheel_of_life.keys())
        for t in bereiche:
            with st.expander(t, expanded=False):
                checked_sum = 0
                negative_sum = 0
                for opt, val in wheel_of_life[t].items():
                    checked = st.checkbox(opt, key=f"cb_{t}_{opt}")
                    if checked:
                        if val > 0:
                            checked_sum += val
                        else:
                            negative_sum += val
                # Normierung: max. 10 Punkte für alle positiven Werte
                max_positive = sum([v for v in wheel_of_life[t].values() if v > 0])
                if max_positive > 0:
                    norm_points = (checked_sum / max_positive) * 10
                else:
                    norm_points = 0
                total_points = norm_points + negative_sum
                # Werte auf 0 bis 10 begrenzen
                total_points = max(0, min(10, total_points))
                values.append(total_points)

    # Radardiagramm
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # schließt das Rad
        theta=bereiche + [bereiche[0]],
        fill='toself',
        name='Wheel of Life',
        marker_color='royalblue'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10])
        ),
        showlegend=False,
        title="Dein Wheel of Life (Radar Chart)"
    )
    st.plotly_chart(fig)


if __name__ == "__main__":
    page_kompass()
