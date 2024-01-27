import streamlit as st
from streamlit.logger import get_logger
import st_pop_up_component as sp
import time

LOGGER = get_logger(__name__)

import streamlit as st

if 'selected_models' not in st.session_state:
    st.session_state.selected_models = []

def update_selected_models():
    if toggle_switch.value:
        st.session_state.selected_models.append(model_data["Model System"])
    else:
        st.session_state.selected_models.remove(model_data["Model System"])

def card(c, model_data, toggle_switch_key=None, on_change=update_selected_models):
    """
    Function to create a card with model performance data.
    """
    # Display Model/Triage System
    model_system = model_data.get("Model System", "")
    if model_system:
        c.subheader(model_system)

    # Display Classifiers
        # Display F1
    f1 = model_data.get("F1", "")

    # Display Accuracy
    accuracy = model_data.get("Accuracy", "")
    classifiers = model_data.get("Classifiers", "")
    if classifiers:
        c.markdown(f""" **Classifiers**: {classifiers}  
                   **F1**: {f1}  
                    **Accuracy**: {accuracy}""")




    # Display URL
    url = model_data.get("URL", "")
    if url:
        c.markdown(f"🔗 [Link]({url})")

    # Toggle switch for on/off
    if toggle_switch_key is not None:
        toggle_switch = c.toggle('Purchase', key=toggle_switch_key)
        c.divider()

def run():
    ind = 0
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    viewTab, marketTab = st.tabs(["Viewer", "Marketplace"])
    with viewTab:
        image_files = ['1.jpg', '2.jpg']
        st.write("# Optho Image Viewer 👋")
        st.selectbox("Choose an option:", ["Zou (2018) et al.", "Latha (2022) et al."])
        initial_image_path = image_files[0] if image_files else None
        image_placeholder = st.empty()  # Create an empty slot to display images

        if initial_image_path:
            image_placeholder.image(initial_image_path, caption="Image 01", use_column_width=True)

        # Button to switch images
        if st.button("RUN", key="run_button"):
            # Show a quick progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            progress_bar.empty()  # Remove the progress bar

            # Switch to the second image
            next_image_path = image_files[1] if len(image_files) > 1 else None
            if next_image_path:
                image_placeholder.image(next_image_path, caption="Image 02", use_column_width=True)

    with marketTab:
        st.write("# Marketplace")

    with marketTab:
        col1, col2 = st.columns([2, 1])
        search = col1.text_input("Search", placeholder='e.g. "image" or "text" or "card"')
        if search:
            print(f"Search term: {search}")
        sorting = col2.selectbox(
            "Sort by", ["⬇️ Sort by accuracy", "⬇️ Sort by F1", "⬇️ Sort by Recent"]
        )
        columns = 3
        st.markdown('#')
        # Create three sample cards arranged in a grid
        c1, c2, c3 = st.columns([1,1,1])
        model_performance = [
        {
            "Model System": "Claro (2016) et al.",
            "Classifiers": "MLP, RC, RF, SVM-RBF",
            "AUC": "NR",
            "Recall": "0.835 to 0.930",
            "Precision": "0.827 to 0.930",
            "F1": "0.827 to 0.929",
            "Accuracy": "0.835 to 0.930",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b6"
        },
        {
            "Model System": "Zou (2018) et al.",
            "Classifiers": "SVM, RF",
            "AUC": "0.732, 0.733",
            "Recall": "NR",
            "Precision": "NR",
            "F1": "NR",
            "Accuracy": "0.74, 0.78",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b16"
        },
        {
            "Model System": "Goel (2021) et al.",
            "Classifiers": "CNN",
            "AUC": "0.831 to 0.997",
            "Recall": "0.773 to 0.969",
            "Precision": "0.571 to 0.963",
            "F1": "0.706 to 0.912",
            "Accuracy": "0.885 to 0.959",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b24"
        },
        {
            "Model System": "Jabbar (2022) et al.",
            "Classifiers": "ResNet, GoogleNet",
            "AUC": "0.924 to 0.971",
            "Recall": "0.854 to 0.953",
            "Precision": "0.937 to 0.990",
            "F1": "0.918 to 0.967",
            "Accuracy": "0.924 to 0.966",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b27"
        },
        {
            "Model System": "Latha (2022) et al.",
            "Classifiers": "ANFIS",
            "AUC": "NR",
            "Recall": "0.963",
            "Precision": "0.961",
            "F1": "NR",
            "Accuracy": "0.962",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b34"
        },
        {
            "Model System": "Thanki (2023)",
            "Classifiers": "kNN, SVM, DT, RF, NB",
            "AUC": "0.836 to 1.000",
            "Recall": "0.543 to 1.000",
            "Precision": "0.722 to 0.986",
            "F1": "0.838 to 0.993",
            "Accuracy": "0.653 to 0.990",
            "URL": "https://www.sciencedirect.com/science/article/pii/S2772442523000072#b34"
        }
    ]

        for ind, entry in enumerate(model_performance):
            if ind % columns == 0:
                c = c1
            elif ind % columns == 1:
                c = c2
            else:
                c = c3
            card(c, entry, toggle_switch_key=ind)
            ind += 1

if __name__ == "__main__":
    run()
