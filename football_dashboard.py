import streamlit as st # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load Data
standings_df = pd.read_csv('standings_data.csv')
scorers_df = pd.read_csv('scorers_data.csv')

# Streamlit App Title
st.title('Football Data Dashboard ⚽')

# Sidebar for Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    'Choose a Dataset to Explore:',
    ['Competition Standings', 'Top Scorers']
)

# Competition Standings Page
if option == 'Competition Standings':
    st.header('Competition Standings')
    
    # Show raw data
    if st.checkbox('Show Raw Standings Data'):
        st.write(standings_df)
    
    # Top 10 Teams by Points
    st.subheader('Top 10 Teams by Points')
    top_10 = standings_df.sort_values(by='Points', ascending=False).head(10)
    st.bar_chart(top_10.set_index('Team')['Points'])
    
    # Top Defensive Teams
    st.subheader('Top 5 Defensive Teams')
    top_defensive = standings_df.sort_values(by='Goals Against').head(5)
    st.bar_chart(top_defensive.set_index('Team')['Goals Against'])
    
    # Top Attacking Teams
    st.subheader('Top 5 Attacking Teams')
    top_attacking = standings_df.sort_values(by='Goals For', ascending=False).head(5)
    st.bar_chart(top_attacking.set_index('Team')['Goals For'])

    # Efficiency Analysis
    st.subheader('Top 5 Teams by Points per Game')
    standings_df['Points per Game'] = standings_df['Points'] / standings_df['Played Games']
    top_efficiency = standings_df.sort_values(by='Points per Game', ascending=False).head(5)
    st.bar_chart(top_efficiency.set_index('Team')['Points per Game'])


# Top Scorers Page
elif option == 'Top Scorers':
    st.header('Top Scorers')
    
    # Show raw data
    if st.checkbox('Show Raw Scorers Data'):
        st.write(scorers_df)
    
    # Top 5 Scorers by Goals
    st.subheader('Top 5 Scorers by Goals')
    top_5_scorers = scorers_df.sort_values(by='Goals', ascending=False).head(5)
    st.bar_chart(top_5_scorers.set_index('Player')['Goals'])
    
    # Top 5 Assisters
    st.subheader('Top 5 Assisters')
    top_assisters = scorers_df.sort_values(by='Assists', ascending=False).head(5)
    st.bar_chart(top_assisters.set_index('Player')['Assists'])
    
    # Goals per Match
    st.subheader('Top 5 Players by Goals per Match')
    scorers_df['Goals per Match'] = scorers_df['Goals'] / scorers_df['Matches Played']
    top_efficiency = scorers_df.sort_values(by='Goals per Match', ascending=False).head(5)
    st.bar_chart(top_efficiency.set_index('Player')['Goals per Match'])

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit")