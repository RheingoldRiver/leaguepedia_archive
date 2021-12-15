import mwparserfromhell
from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials

credentials = AuthCredentials(user_file="bot")
site = EsportsClient("lol", credentials=credentials)

response = site.cargo_client.query(
	tables = "MatchScheduleGame=MSG, ScoreboardGames=SG",
    join_on= "MSG.GameId=SG.GameId",
	fields = "MSG.GameId, SG.GameId, SG.MatchHistory, MSG._pageName=DataPage, MSG.N_MatchInTab, MSG.N_TabInPage, MSG.N_GameInMatch",
    where = "MSG.MatchHistory IS NULL AND SG.MatchHistory IS NOT NULL AND SG._pageName IS NOT NULL AND MSG._pageName IS NOT NULL AND SG.MatchHistory LIKE '%matchhistory%'",
    order_by = "DataPage"
)

datapages = []

for item in response:
    if item["DataPage"] not in datapages:
        datapages.append(item["DataPage"])

for datapage in datapages:
    items = {}
    data_page = site.client.pages[datapage]
    data_text = data_page.text()
    data_wikitext = mwparserfromhell.parse(data_text)
    for item in response:
        if item["DataPage"] != datapage:
            continue
        match_in_tab = str(item["N MatchInTab"])
        tab_in_page = str(item["N TabInPage"])
        game_in_match = str(item["N GameInMatch"])
        match_history = item["MatchHistory"].strip()
        tab_counters = 0
        match_counters = 0
        game_counters = 0
        items[f"{tab_in_page}_{match_in_tab}_{game_in_match}"] = str(match_history)
    for template in data_wikitext.filter_templates():
        if template.name.matches("MatchSchedule/Start"):
            tab_counters += 1
            match_counters = 0
        elif template.name.matches("MatchSchedule"):
            match_counters += 1
            game_counters = 0
        elif template.name.matches("MatchSchedule/Game"):
            game_counters += 1
            if f"{tab_counters}_{match_counters}_{game_counters}" in items:
                match_history_to_add = items.get(f"{tab_counters}_{match_counters}_{game_counters}")
                template.add("mh", match_history_to_add)
        else:
            continue
    data_page.edit(str(data_wikitext), summary = "Automatically adding MH from Scoreboards")
    print(f"Success with {datapage}")
