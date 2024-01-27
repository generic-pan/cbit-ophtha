import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Optho Image Viewer 👋")

    st.sidebar.success("Select a vision model from above.")

    st.markdown(
        """
        **👈 Select a vision AI model from the sidebar** to see some examples
        of what OpthoImageAI can do!
        ### Want to learn more?
        - Check ou [our website](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
    """)

      # Create a horizontal toolbar with placeholder buttons
    toolbar = st.container()
    with toolbar:
        st.button("Button 1")
        st.button("Button 2")
        st.button("Button 3")
        st. button("Button 4")
        # Add as many buttons as needed

    # Create four columns for image panels
    col1, col2, col3, col4 = st.columns(4)

    # Define a function to create an image panel in a column
    def create_image_panel(column):
        uploaded_file = column.file_uploader("Upload Image Here", type=["jpg", "jpeg", "png", "svg"], key=column)
        if uploaded_file is not None:
            column.image(uploaded_file, caption="Uploaded Image")

    # Create image panels in each column
    create_image_panel(col1)
    create_image_panel(col2)
    create_image_panel(col3)
    create_image_panel(col4)



if __name__ == "__main__":
    run()
