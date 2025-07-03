import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from wheel_of_life import wheel_of_life

def page_wheel_of_life():
    st.title("Wheel of Life")
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
    page_wheel_of_life()
