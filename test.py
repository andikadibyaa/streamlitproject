import streamlit as st
import pandas as pd
import altair as alt


data = pd.read_csv("output_file.csv")
st.title("Exploring User Trends: Seasons")
st.markdown(
    "An interactive dashboard to explore user trends based on the most popular seasons."
)
season_grouped = data.groupby('season')
casual_by_season = season_grouped['casual'].sum().reset_index()
registered_by_season = season_grouped['registered'].sum().reset_index()
max_casual_season = casual_by_season.loc[casual_by_season['casual'].idxmax()]['season']
max_registered_season = registered_by_season.loc[registered_by_season['registered'].idxmax()]['season']
selected_casual = st.checkbox('Select Casual Users')
selected_registered = st.checkbox('Select Registered Users')
plt = alt.Chart()

bar_color = 'darkblue'

if selected_casual:
    if selected_registered:
        # Plot Registered Users by Season
        plt = alt.Chart(registered_by_season).mark_bar(color=bar_color).encode(
            x='season:N',
            y='registered:Q',
            tooltip=['season:N', 'registered:Q']
        ).properties(
            title='Most Popular Season for Registered Users',
            background='#808080'  # Background color: gray
        )
        st.markdown("The most popular season for registered users is **{}**.".format(max_registered_season))
    else:
        # Plot Casual Users by Season
        plt = alt.Chart(casual_by_season).mark_bar(color=bar_color).encode(
            x='season:N',
            y='casual:Q',
            tooltip=['season:N', 'casual:Q']
        ).properties(
            title='Most Popular Season for Casual Users',
            background='#808080'  # Background color: gray
        )
        st.markdown("The most popular season for casual users is **{}**.".format(max_casual_season))

else:
    if selected_registered:
        # Plot Registered Users by Season
        plt = alt.Chart(registered_by_season).mark_bar(color=bar_color).encode(
            x='season:N',
            y='registered:Q',
            tooltip=['season:N', 'registered:Q']
        ).properties(
            title='Most Popular Season for Registered Users',
            background='#808080'  # Background color: gray
        )
        st.markdown("The most popular season for registered users is **{}**.".format(max_registered_season))
    else:
        # Plot Casual Users by Season
        plt = alt.Chart(casual_by_season).mark_bar(color=bar_color).encode(
            x='season:N',
            y='casual:Q',
            tooltip=['season:N', 'casual:Q']
        ).properties(
            title='Most Popular Season for Casual Users',
            background='#808080'  # Background color: gray
        )
        st.markdown("The most popular season for casual users is **{}**.".format(max_casual_season))


st.altair_chart(plt, use_container_width=True)
st.caption('Copyright (c) Andika Dibya 2024')














