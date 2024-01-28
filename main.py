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
    model_system = model_data[0]
    if model_system:
        c.subheader(model_system, help=model_data[5])

    # Display Classifiers
        # Display F1
    
    c.markdown(f""" **Device**: {model_data[2]}  
                   **Modality**: {model_data[1]}  
                    **Accuracy**: {model_data[3]}  
                    **Demographics**: {model_data[4]}""")




    # Display URL
    url = "https://google.com"
    if url:
        c.markdown(f"🔗 [Link]({url})")

    # Toggle switch for on/off
    if toggle_switch_key is not None:
        toggle_switch = c.toggle('Purchase', key=toggle_switch_key)
        if(toggle_switch_key < 3):
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
        st.write("# Image Viewer")
        st.selectbox("Choose an option:", ["Glaucoma", "AMD"])
        st.write("# ")
        initial_image_path = image_files[0] if image_files else None
        image_placeholder = st.empty()  # Create an empty slot to display images

        if initial_image_path:
            image_placeholder.image(initial_image_path, caption="Image 01", use_column_width=True)

        col1, col2, col3 , col4, col5 = st.columns([1,1,1,1,1])

        # Button to switch images
        if col3.button("Run Image", key="run_button"):
            # Show a quick progress bar
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            progress_bar.empty()  # Remove the progress bar

            # Switch to the second image
            next_image_path = image_files[1] if len(image_files) > 1 else None
            if next_image_path:
                image_placeholder.image(next_image_path, caption="Scanned for glaucoma", use_column_width=True)
        st.write("#  ")
        k1, k2, k3 = st.columns([1,1,1])
        k2.write("###### &nbsp;&nbsp;Were these results helpful?")
        k2.write("82 of 96 doctors found this helpful")
        col1, col2, col3 , col4, col5, col6, col7, col8, col9, col10 = st.columns([1,1,1,1,1,1,1,1,1,1])
        with col5:
            st.button("👍")
        with col6:
            st.button("👎")
    with marketTab:
        st.write("# Marketplace")

    with marketTab:
        col1, col2, col3 = st.columns([2, 1, 1])
        search = col1.text_input("Search", placeholder='e.g. "image" or "text" or "card"')
        if search:
            print(f"Search term: {search}")
        sorting = col2.selectbox(
            "Sort by", ["⬇️ Sort by accuracy", "⬇️ Sort by F1", "⬇️ Sort by Recent"]
        )
        filtering = col3.selectbox(
            "Filter by", ["Under 18", "18-29", "30-49", "49+", "White", "Black", "Asian", "Hispanic"]
        )
        columns = 3
        st.markdown('#')
        # Create three sample cards arranged in a grid
        c1, c2, c3 = st.columns([1,1,1])
        data = [
    ["Glaucoma", "Retinal Photograph", "Optos", "0.93", "18-29, White, United States", "Classifiers: CNN + SVM"],
    ["AMD", "Retinal Photograph", "Optos", "0.96", "30-49, Hispanic, Mexico", "Classifiers: RN + GB"],
    ["Glaucoma", "OCT Nerve", "Zeiss Cirrus", "0.84", "30-49, Asian, Turkey", "Classifiers: CNN + SVM"],
    ["AMD", "OCT Macula", "Heidelberg Spectralis", "0.93", "18-29, White, United States", "Classifiers: VGG + RNN"],
    ["Diabetic Retinopathy", "Retinal Photograph", "Optos", "0.92", "49+, Black, United States", "Classifiers: RNN"],
    ["Diabetic Macular Edema", "OCT Macula", "Heidelberg Spectralis", "0.99", "18-29, White, United States", "Classifiers: CNN"],
]


        for ind, entry in enumerate(data):
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
