import streamlit as st

def calculate_combined_probability(
    team1_red, team1_2ndY, team1_pk_won, team1_pk_con, team1_matches,
    vs_team1_red, vs_team1_2ndY, vs_team1_pk_won, vs_team1_pk_con, vs_team1_matches,
    team2_red, team2_2ndY, team2_pk_won, team2_pk_con, team2_matches,
    vs_team2_red, vs_team2_2ndY, vs_team2_pk_won, vs_team2_pk_con, vs_team2_matches
):
    red1 = (team1_red + team1_2ndY) / team1_matches
    pen1 = (team1_pk_won + team1_pk_con) / team1_matches
    red2 = (team2_red + team2_2ndY) / team2_matches
    pen2 = (team2_pk_won + team2_pk_con) / team2_matches

    red_vs1 = (vs_team1_red + vs_team1_2ndY) / vs_team1_matches
    pen_vs1 = (vs_team1_pk_won + vs_team1_pk_con) / vs_team1_matches
    red_vs2 = (vs_team2_red + vs_team2_2ndY) / vs_team2_matches
    pen_vs2 = (vs_team2_pk_won + vs_team2_pk_con) / vs_team2_matches

    red_comb1 = (red1 + red_vs1) / 2
    pen_comb1 = (pen1 + pen_vs1) / 2
    red_comb2 = (red2 + red_vs2) / 2
    pen_comb2 = (pen2 + pen_vs2) / 2

    p_no_red = (1 - red_comb1) * (1 - red_comb2)
    p_no_pen = (1 - pen_comb1) * (1 - pen_comb2)
    p_clean = p_no_red * p_no_pen

    return {
        "RedCardRate_Team1_Combined": red_comb1,
        "RedCardRate_Team2_Combined": red_comb2,
        "PenaltyRate_Team1_Combined": pen_comb1,
        "PenaltyRate_Team2_Combined": pen_comb2,
        "P_NoRedCard": p_no_red,
        "P_NoPenalty": p_no_pen,
        "P_CleanMatch (No RC or PK)": p_clean
    }

st.title("⚽ Combined Probability Estimator: No Red Card & No Penalty")

def input_section(label):
    st.header(label)
    red = st.number_input(f"{label} - Red Cards", min_value=0)
    y2 = st.number_input(f"{label} - Second Yellows", min_value=0)
    pk_won = st.number_input(f"{label} - Penalties Won", min_value=0)
    pk_con = st.number_input(f"{label} - Penalties Conceded", min_value=0)
    matches = st.number_input(f"{label} - Matches Played", min_value=1)
    return red, y2, pk_won, pk_con, matches

t1 = input_section("Team 1")
v1 = input_section("Opponent vs Team 1")
t2 = input_section("Team 2")
v2 = input_section("Opponent vs Team 2")

if st.button("Calculate"):
    result = calculate_combined_probability(*t1, *v1, *t2, *v2)
    st.subheader("📊 Results")
    for key, value in result.items():
        st.write(f"**{key}**: {value:.4f}")
