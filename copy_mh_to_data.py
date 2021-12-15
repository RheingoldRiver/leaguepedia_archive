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
    
x = 0
length = len(response)

for item in response:
    x += 1
    match_in_tab = int(item["N MatchInTab"])
    tab_in_page = int(item["N TabInPage"])
    game_in_match = item["N GameInMatch"]
    match_history = item["MatchHistory"].strip()
    data_page_title = item["DataPage"]
    data_page = site.client.pages[item["DataPage"]]
    data_text = data_page.text()
    data_wikitext = mwparserfromhell.parse(data_text)
    tab_counters = 0
    match_counters = 0
    print(f"\nProcessing {str(data_page_title)}, Tab {str(tab_in_page)}, Match {str(match_in_tab)}, Game {str(game_in_match)}, MH {str(match_history)}, Item {str(x)} from {str(length)}")
    for template in data_wikitext.filter_templates():
        if template.name.matches("MatchSchedule/Start"):
            if tab_counters != tab_in_page:
                tab_counters += 1
            else:
                print("Not Found!")
                with open("errors.txt", "w+", "utf8") as f:
                    f.write("Error with " + str(item["GameId"] + " in " + item["DataPage"] + "\n"))
        elif template.name.matches("MatchSchedule"):
            if tab_counters != tab_in_page:
                continue
            else:
                match_counters += 1
                if match_counters == match_in_tab and tab_counters == tab_in_page:
                    gametemplate = template.get("game{}".format(str(game_in_match))).value
                    gametemplate = gametemplate.filter_templates()[0]
                    gametemplate.add("mh", match_history)
                    data_page.edit(str(data_wikitext), summary = "Automatically adding MH from Scoreboards")
                    print("Success with {0}".format(item["GameId"]))
                    break
