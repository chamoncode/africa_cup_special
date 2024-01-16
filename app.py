"""
This script allows you to get the results of the African Cup of Nations 2024 Round By Round
From the Eurosport website: 
https://www.eurosport.fr/football/coupe-d-afrique-des-nations/calendrier-resultats.shtml
"""


from datetime import datetime as dt

import requests
import streamlit as st
from bs4 import BeautifulSoup
from polling2 import poll

URL = "https://www.eurosport.fr/football/coupe-d-afrique-des-nations/calendrier-resultats.shtml"


def get_clock_info(info):
    """
    Get the clock info from the clock_info span
    """
    if info:
        try:
            return dt.strptime(info.text, "%H:%M").strftime("%H:%M")
        except ValueError:
            return "⏱️" + info.text
    return "✔️"


response = poll(lambda: requests.get(URL, timeout=10), step=30, poll_forever=True)

# Get the HTML content from the response
html_content = response.text

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with attribute data-testid equals "team-match-score-atom-container" or "template-section-title"
divs = soup.find_all(
    "div",
    attrs={
        "data-testid": ["team-match-score-atom-container", "template-section-title"]
    },
)

# Make the fixtures table
fixtures_table = []

MATCH_DAY = None  # The current match day dd/mm/yyyy
for div in divs:
    if div.get("data-testid") == "template-section-title":
        # Append the round title to the fixtures table
        MATCH_DAY = dt.strptime(div.text, "%d/%m/%Y").date()
    # Get the children divs
    else:
        children = div.findChildren("div", recursive=False)

        clock_info = div.findParent("div").findChild(
            "span",
            recursive=True,
            attrs={"data-testid": "atom-match-card-content-info"},
        )

        # Append the fixture info to the fixtures table
        fixtures_table.append(
            {
                "Match Day": MATCH_DAY,
                "Time": get_clock_info(clock_info),
                "Team A": children[0].text,
                "Score": f"{children[1].text} - {children[2].text}",
                "Team B": children[3].text,
            }
        )
        MATCH_DAY = ""

st.title("African Cup of Nations 2024")
st.write("Current Round")

st.dataframe(
    fixtures_table,
    hide_index=True,
    height=458,
    use_container_width=True,
)
