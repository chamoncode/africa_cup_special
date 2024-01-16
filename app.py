"""
This script allows you to get the results of the African Cup of Nations 2024 Round By Round
From the Eurosport website: 
https://www.eurosport.fr/football/coupe-d-afrique-des-nations/calendrier-resultats.shtml
"""


import requests
import streamlit as st
from bs4 import BeautifulSoup
from polling2 import poll

URL = "https://www.eurosport.fr/football/coupe-d-afrique-des-nations/calendrier-resultats.shtml"

response = poll(lambda: requests.get(URL, timeout=10), step=60, poll_forever=True)

# Get the HTML content from the response
html_content = response.text

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all divs with attribute data-testid="team-match-score-atom-container"
divs = soup.find_all("div", attrs={"data-testid": "team-match-score-atom-container"})

# Make the fixtures table
fixtures_table = []

for div in divs:
    # Get the children divs
    children = div.findChildren("div", recursive=False)
    # Append the fixture info to the fixtures table
    fixtures_table.append(
        {
            "Team A": children[0].text,
            "Score": f"{children[1].text} - {children[2].text}",
            "Team B": children[3].text,
        }
    )

st.title("African Cup of Nations 2024")
st.write("Current Round")

st.dataframe(
    fixtures_table,
    hide_index=True,
    height=458,
    use_container_width=True,
)
