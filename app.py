import json
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Load wheel_of_life from JSON and store in session_state
if "wheel_of_life" not in st.session_state:
    with open("wheel_of_life.json", "r", encoding="utf-8") as f:
        st.session_state["wheel_of_life"] = json.load(f)

def page_wheel_of_life():
    st.title("Wheel of Life")
    st.write("Check each option that applies. Points are counted according to the option (max. 10 per category, negative values are subtracted):")

    with st.sidebar:
        values = []
        wheel_of_life = st.session_state["wheel_of_life"]
        categories = list(wheel_of_life.keys())
        for cat in categories:
            with st.expander(cat, expanded=False):
                checked_sum = 0
                negative_sum = 0
                for opt, val in wheel_of_life[cat].items():
                    checked = st.checkbox(opt, key=f"cb_{cat}_{opt}")
                    if checked:
                        if val > 0:
                            checked_sum += val
                        else:
                            negative_sum += val
                # Normalization: max. 10 points for all positive values
                max_positive = sum([v for v in wheel_of_life[cat].values() if v > 0])
                if max_positive > 0:
                    norm_points = (checked_sum / max_positive) * 10
                else:
                    norm_points = 0
                total_points = norm_points + negative_sum
                # Limit values between 0 and 10
                total_points = max(0, min(10, total_points))
                values.append(total_points)

    # Radar chart
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # close the radar
        theta=categories + [categories[0]],
        fill='toself',
        name='Wheel of Life',
        marker_color='royalblue'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 10])
        ),
        showlegend=False,
        title="Your Wheel of Life (Radar Chart)"
    )
    st.plotly_chart(fig)

def page_config():
    st.title("Configuration: Wheel of Life Categories and Options")
    data = st.session_state["wheel_of_life"]
    categories = list(data.keys())

    st.subheader("Add Category")
    new_category = st.text_input("Create new category", key="new_category")
    if st.button("Add category"):
        if new_category and new_category not in data:
            data[new_category] = {}
            st.session_state["wheel_of_life"] = data
            st.success(f"Category '{new_category}' added!")
            st.rerun()

    st.subheader("Edit Categories and Options")
    for category in categories:
        with st.expander(f"{category}"):
            # Add option
            new_option = st.text_input(f"New option for '{category}'", key=f"new_option_{category}")
            new_value = st.number_input(f"Value for new option", key=f"new_value_{category}", value=1)
            if st.button(f"Add option to '{category}'", key=f"add_option_{category}"):
                if new_option:
                    data[category][new_option] = new_value
                    st.session_state["wheel_of_life"] = data
                    st.success(f"Option '{new_option}' added!")
                    st.rerun()
            # Show and edit options
            to_delete = []
            for opt, val in data[category].items():
                col1, col2, col3 = st.columns([4,2,1])
                with col1:
                    new_opt = st.text_input("Option", value=opt, key=f"edit_{category}_{opt}")
                with col2:
                    new_val = st.number_input("Value", value=val, key=f"edit_val_{category}_{opt}")
                with col3:
                    if st.button("Delete", key=f"del_{category}_{opt}"):
                        to_delete.append(opt)
                # Save changes
                if new_opt != opt or new_val != val:
                    data[category].pop(opt)
                    data[category][new_opt] = new_val
                    st.session_state["wheel_of_life"] = data
                    st.success(f"Option '{opt}' changed!")
                    st.rerun()
            # Delete options
            for opt in to_delete:
                data[category].pop(opt)
                st.session_state["wheel_of_life"] = data
                st.success(f"Option '{opt}' deleted!")
                st.rerun()
            # Delete category
            if st.button(f"Delete category '{category}'", key=f"del_category_{category}"):
                data.pop(category)
                st.session_state["wheel_of_life"] = data
                st.success(f"Category '{category}' deleted!")
                st.rerun()

    st.subheader("Add default values")
    if st.button("Add default values", key="add_defaults"):
        with open("wheel_of_life.json", "r", encoding="utf-8") as f:
            default_data = json.load(f)
        added = False
        for category, opts in default_data.items():
            if category not in data:
                data[category] = opts.copy()
                added = True
            else:
                for opt, val in opts.items():
                    if opt not in data[category]:
                        data[category][opt] = val
                        added = True
        if added:
            st.session_state["wheel_of_life"] = data
            st.success("Default values have been added!")
            st.rerun()
        else:
            st.info("All default values are already present.")

if __name__ == "__main__":
    pages = [
        st.Page(page_wheel_of_life, title="Compass"),
        st.Page(page_config, title="Configuration")
    ]
    pg = st.navigation(pages)
    pg.run()
