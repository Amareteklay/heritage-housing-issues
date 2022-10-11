import streamlit as st

def page_summary_body():
    """
    Displays contents of the project summary page
    """
    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargons**\n\n"
        f"* **Sales price** of a house refers to the current market price of a house with certain attributes.\n"
        f"* **Inherrited house** is a house that the client inheritted from grandparents.\n"
        f"* **Summed price** was determined by adding the sales prices of the four inheritted houses.\n\n"
        )
    
     # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The project dataset comes from housing price database from Ames, Iowa. It is available in [Kaggle via Code Institute](https://www.kaggle.com/codeinstitute/housing-prices-data), and includes sales price (the target) and features that show a house's age (year built, year remodeled), property size (first floor area, second floor area, garaze area) and quality assessments."
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Amareteklay/heritage-housing-issues).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"**Project Business Requirements**\n"
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how house attributes correlate with sale prices."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price.\n"
        f"* 2 - The client is interested in predicting the house sale prices from her 4 inherited houses,"
        f" and any other house in Ames, Iowa."
        )

        