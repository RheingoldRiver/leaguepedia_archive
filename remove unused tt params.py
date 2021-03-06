from log_into_wiki import *
import mwparserfromhell

site = login('bot', 'lol')  # Set wiki
summary = 'remove unused params from tabs headers'  # Set summary

all_templates = [
	"2013 OGN Tabs",
	"2013 The Legends Circuit Tabs",
	"2014 EUCS Tabs",
	"2014 Latin America Cup Tabs",
	"2014 LNL Tabs",
	"2014 NACS Tabs",
	"2015 All-Star Melbourne Tabs",
	"2015 All-Star Tabs",
	"2015 IWCI Tabs",
	"2015 IWCT Tabs",
	"2015 LAN Cup Tabs",
	"2015 LAS Cup Tabs",
	"2015 Latin America Grand Final Tabs",
	"2015 LoL KeSPA Cup Tabs",
	"2015 LOL Ladies Battle Tabs",
	"2015 LongZhu Gaming Queen Invitational Tabs",
	"2015 TLC Tabs",
	"2016 ESL Brasil Premier League Tabs",
	"2016 ESL UK Premiership Tabs",
	"2016 GPL Tabs",
	"2016 LAN Cup Tabs",
	"2016 LAS Cup Tabs",
	"2016 LCK Tabs",
	"2016 LJL Challenger Tabs",
	"2016 LoL KeSPA Cup Tabs",
	"2016 LPL Tabs",
	"2016 LPPL Tabs",
	"2016 LSPL Tabs",
	"2016 Multiplay UK Masters Tabs",
	"2016 SLTV Challenger League Tabs",
	"2016 VCS Tabs",
	"2017 - 2018 EBL Tabs",
	"2017 ESL Brasil Premier League Tabs",
	"2017 ESL Premiership Tabs",
	"2017 LJL Challenger Tabs",
	"2017 VCS Tabs",
	"2018 Asian Games Tabs",
	"2018 ESL Premiership Tabs",
	"2018 LJL Challenger Tabs",
	"2018 Nordic Championship Tabs",
	"2019 Nordic Championship Tabs",
	"2019 Player One Elite Series Tabs",
	"4Players.de All or Nothing Tabs",
	"A1 League Tabs",
	"AAa Pro Challenge Tabs",
	"Absolute Amateur League Tabs",
	"Absolute Arena Tabs",
	"Absolute Pro League Tabs",
	"ADCL Tabs",
	"AGA 2018 Tabs",
	"AHGL Tabs",
	"All-Star 2014 Tabs",
	"All-Star 2016 Barcelona Tabs",
	"All-Star 2018 Tabs",
	"All-Star Los Angeles 2017 Tabs",
	"Amateur League Championship Series Tabs",
	"Aorus 2018 Tabs",
	"Argentina Game Show 2015 Tabs",
	"Argentina Game Show 2018 Tabs",
	"Asian Indoor-Martial Arts Games 2013 Tabs",
	"Assembly 2012-2015 Tabs",
	"Assembly 2016-2019 Tabs",
	"ASUS Republic of Gamers 2015 Tabs",
	"AsusTabs",
	"Azubu LoL The Champions All Stars Tabs",
	"Balkan Lan Masters 2017 Tabs",
	"Baron Nashor Cup Tabs",
	"Battle of the Atlantic 2013 Tabs",
	"BEL 2018 Tabs",
	"BEL 2019 Tabs",
	"BESL 2018 Tabs",
	"BGL 2014 Tabs",
	"BIG League 2019 Tabs",
	"Blackpills Cup Tabs",
	"BLSNA Tabs",
	"BMA 2015 Tabs",
	"BMC Cup Tabs",
	"BMC EU 2014 Tabs",
	"BMC NA 2014 Tabs",
	"BoU CIS Tabs",
	"BPL 2018 Tabs",
	"BPL 2019 Tabs",
	"Brasil Gaming League Arena Tabs",
	"Brasil Mega Arena 2016 Rio Tabs",
	"Brazil Game Show - International Challenge 2013 Tabs",
	"Brazilian Champion League 2014 Tabs",
	"BRCC 2016 Tabs",
	"BRCC 2017 Tabs",
	"BRCC 2018 Tabs",
	"BRCC 2019 Tabs",
	"BRNA Tabs",
	"BZNA Tabs",
	"Campus Gaming Party Berlin Tabs",
	"CBLOL 2015 Tabs",
	"CBLOL 2016 Tabs",
	"CBLOL 2017 Tabs",
	"CBLOL 2018 Tabs",
	"CBLOL 2019 Tabs",
	"CCA Masters 2017 Tabs",
	"CCSTabs",
	"CDiscount Tabs",
	"CDL LAN 2017 Tabs",
	"CDL LAS 2017 Tabs",
	"CDL Norte 2015 Tabs",
	"CDL Norte 2016 Tabs",
	"CDL Sur 2015 Tabs",
	"CDL Sur 2016 Tabs",
	"CDLN 2018 Tabs",
	"CEVO Champions Challenge Tabs",
	"CGA Major League 2013 Tabs",
	"Challenge France 2017 Tabs",
	"Challengers Korea 2015 Tabs",
	"Challengers Korea 2016 Tabs",
	"Challengers Korea 2017 Tabs",
	"Challengers Korea 2018 Tabs",
	"Challengers Korea 2019 Tabs",
	"Champion Flashcard Standalone Tabs",
	"Champions 2014 Tabs",
	"Circuito Tormenta 2018 Tabs",
	"Circus E-Sport Tour 2018 Tabs",
	"CIS Championship 2013 Tabs",
	"CL 2017 Tabs",
	"CL 2018 Tabs",
	"CLOL 2018 Tabs",
	"CLOL 2019 Tabs",
	"CLS 2017 Tabs",
	"CLS 2018 Tabs",
	"CN 2018 Tabs",
	"CNA 2019 Tabs",
	"CNC 2019 Tabs",
	"CNCO 2019 Tabs",
	"CNM 2019 Tabs",
	"Collegiate Star League March Madness Tabs",
	"Collegiate Star League: Trinity Tabs",
	"Community Tabs",
	"Copa Coliseo Tabs",
	"Copa Go4gold 2016 Tabs",
	"Corsair Vengeance Cup Tabs",
	"CPL Shenyang 2012 Tabs",
	"Cross Border Esport Tabs",
	"CSN playLEGENDS Cup Tabs",
	"Curse King Of The Hill Tabs",
	"Danish Esports League 2019 Tabs",
	"DCL Season 3 Tabs",
	"DCL Season 4 Tabs",
	"DDH 2019 Tabs",
	"Demacia Championship 2017 Tabs",
	"Demacia Cup 2015 Tabs",
	"Demacia Cup 2016 Tabs",
	"Demacia Cup 2017 Tabs",
	"Demacia Cup 2018 Tabs",
	"Demacia Cup 2018 Winter Tabs",
	"Demacia Cup Season 1 Tabs",
	"Demacia Cup Season 2 Tabs",
	"Desafio UniLoL 2017 Tabs",
	"Desafio UniLoL 2018 Tabs",
	"Dev Blog Tabs",
	"Division Cup 2 Tabs",
	"DivisionCup Exalty 1 Tabs",
	"DLCompare Pro Cup 1 Tabs",
	"DoigCup 2 Tabs",
	"DreamHack 2012 Tabs",
	"DreamHack 2013 Tabs",
	"DreamHack 2014 Tabs",
	"DreamHack 2015 Tabs",
	"DreamHack 2016 Tabs",
	"DreamHack 2017 Tabs",
	"E-Sport Festival 2015 Logitech G Tournament Tabs",
	"EBL 2019 Tabs",
	"Eclypsia Christmas Cup Tabs",
	"Eclypsia Rise of Legend Tabs",
	"ECS 2016 Tabs",
	"ECS 2017 Tabs",
	"ECS 2018 Tabs",
	"ECS 2019 Tabs",
	"EGaming Tabs",
	"Elite of Europe Tabs",
	"EmpireTV Challenge Tabs",
	"EMS Tabs",
	"Epic.LAN Tabs",
	"EPSGermany 2011 Tabs",
	"EPSGermany 2012 Tabs",
	"EPSGermany 2013 Tabs",
	"EPSGermany 2014 Tabs",
	"ESL Benelux 2016 Tabs",
	"ESL Benelux 2017 Tabs",
	"ESL Benelux 2018 Tabs",
	"ESL Benelux 5on5 Opening Cup Tabs",
	"ESL Championnat National 2015 Autumn Tabs",
	"ESL Championnat National 2016 Summer Tabs",
	"ESL CZ/SK 2018 Tabs",
	"ESL Dutch 2018 Tabs",
	"ESL European Challenger Circuit: Poland Tabs",
	"ESL Italia Championship 2017 Tabs",
	"ESL Italia Championship 2018 Tabs",
	"ESL Masters Spain Madrid Tabs",
	"ESL Masters Spain Malaga Tabs",
	"ESL Meisterschaft 2015 Tabs",
	"ESL Meisterschaft 2016 Tabs",
	"ESL Meisterschaft 2017 Tabs",
	"ESL Meisterschaft 2018 2nd Division Tabs",
	"ESL Meisterschaft 2018 Tabs",
	"ESL Meisterschaft 2019 2nd Division Tabs",
	"ESL Meisterschaft 2019 Tabs",
	"ESL Pro Series CIS Tabs",
	"ESL Proximus 2018 Tabs",
	"ESL SEE Tabs",
	"ESL Swisscom Hero League 2018 Tabs",
	"ESL UK Premiership 2015 Tabs",
	"ESL VIP Adria Tabs",
	"ESL Vodafone Championship 2019 Tabs",
	"ESL Vodafone Championship Serie B 2018 Tabs",
	"ESLA Pro Triple L Season 1 Tabs",
	"ESLMP 2017 Tabs",
	"ESLMP 2018 Tabs",
	"EU LCS 2014 Tabs",
	"EU LCS 2015 Tabs",
	"EU LCS 2016 Tabs",
	"EU LCS 2017 Tabs",
	"EU LCS 2018 Tabs",
	"EU LCS Season 3 Tabs",
	"EU Masters 2018 Tabs",
	"EU Masters 2019 Tabs",
	"EUCS 2015 Tabs",
	"EUCS 2016 Tabs",
	"EUCS 2017 Tabs",
	"FACEIT Challenger Invitational Tabs",
	"Fantasy LCS 2015 Tabs",
	"Fatal1ty Gaming Gear League of Legends Tournament Tabs",
	"Fight for Pride Promo Tabs",
	"Fight LoL EUW Tabs",
	"Finnish Esports League 2019 Tabs",
	"Forge of Champions 2018 Tabs",
	"G-League 2013 Tabs",
	"G-League 2014 Tabs",
	"G-League Season 2 Tabs",
	"GALAXY eSports Carnival Tabs",
	"GameAthlon Tabs",
	"GameForce Masters 2018 Tabs",
	"GameInfoPortalTabs",
	"Gamers Assembly 2012 Tabs",
	"Gamers Assembly 2015 Tabs",
	"Garena Talk Talk League 2014 Tabs",
	"Geek Days Lille 2017 Tabs",
	"GgLA Challenger Arena Tabs",
	"GIGABYTE Esports LAN Tabs",
	"GIGABYTE StarsWar League Tabs",
	"GL 2019 Tabs",
	"Glorious Arena Tabs",
	"Go4LoL Asia 2011 Tabs",
	"Go4LoL BR 2012 Tabs",
	"Go4LoL BR 2013 Tabs",
	"Go4LoL BR 2014 Tabs",
	"Go4LoL BR 2015 Tabs",
	"Go4LoL EU 2010 Tabs",
	"Go4LoL EU 2011 Tabs",
	"Go4LoL EU 2012 Tabs",
	"Go4LoL EU 2013 Tabs",
	"Go4LoL EU 2014 Tabs",
	"Go4LoL EU 2015 Tabs",
	"Go4LoL LAN 2015 Tabs",
	"Go4LoL LAS 2015 Tabs",
	"Go4LoL LAS 2016 Tabs",
	"Go4LoL LAS 2017 Tabs",
	"Go4LoL LAS 2018 Tabs",
	"Go4LoL NA 2011 Tabs",
	"Go4LoL NA 2012 Tabs",
	"Go4LoL NA 2013 Tabs",
	"Go4LoL NA 2014 Tabs",
	"Go4LoL NA 2015 Tabs",
	"Go4LoL Poland 2012 Tabs",
	"Go4LoL Poland 2013 Tabs",
	"Go4LoL Poland 2014 Tabs",
	"Go4LoL Pro Asia Tabs",
	"GPC 2018 Tabs",
	"GPL 2014 Tabs",
	"GPL 2015 Tabs",
	"GPL 2017 Tabs",
	"GPL 2018 Tabs",
	"GPLTabs",
	"HeartoWin Cup Tabs",
	"Hitpoint Masters 2014 Tabs",
	"Hitpoint Masters 2015 Tabs",
	"Hitpoint Masters 2016 Tabs",
	"Hitpoint Masters 2017 Tabs",
	"Hitpoint Masters 2018 Tabs",
	"Hitpoint Masters 2019 Tabs",
	"Hong Kong E-Sports Challenge Tabs",
	"Hong Kong Esports Tournament Tabs",
	"HTC Ascension Tabs",
	"Hyperplay 2018 Tabs",
	"Iberian Cup 2018 Tabs",
	"IEM Season 10 Tabs",
	"IEM Season 11 Tabs",
	"IEM Season 5 Tabs",
	"IEM Season 6 Tabs",
	"IEM Season 7 Tabs",
	"IEM Season 8 Tabs",
	"IEM Season 9 Tabs",
	"IeSF Tabs",
	"IET Tabs",
	"IGN ProLeague Challengers Tabs",
	"IGN ProLeague Elites Tabs",
	"In2LOL Kickoff EU Tournament Tabs",
	"In2LOL Kickoff NA Tournament Tabs",
	"In2LOL King Of The Hill Tabs",
	"Insomnia 2012 Tabs",
	"Insomnia 2013 Tabs",
	"Insomnia 2014 Tabs",
	"Insomnia 2015 Tabs",
	"Insomnia 2016 Tabs",
	"Insomnia 2017 Tabs",
	"Insomnia 2018 Tabs",
	"International e-Culture Festival Tabs",
	"International Invitational Tournament Tabs",
	"International Wildcard All-Star Barcelona 2016 Tabs",
	"IPL Face Off: San Francisco Showdown Tabs",
	"IPL LoLympics Tabs",
	"IPL Tabs",
	"IPLTabs",
	"Italian Gaming League 2016 Tabs",
	"Italian Gaming League 2017 Tabs",
	"IWCI 2016 Tabs",
	"IWCQ 2016 Tabs",
	"IWCT 2013 Tabs",
	"IWCT 2014 Tabs",
	"JCC 2018 Tabs",
	"JCG Premier League 2013 Tabs",
	"JCG Premier League 2014 Tabs",
	"JCG Premier League 2015 Tabs",
	"Kaos TV Challenger Series EUW Tabs",
	"Kaos TV Challenger Series NA Tabs",
	"Kayzr League 2018 Tabs",
	"Kayzr League 2019 Tabs",
	"KeSPA Cup 2017 Tabs",
	"KeSPA Cup 2018 Tabs",
	"King of SEA Tabs",
	"Kings of Europe Tabs",
	"Kung Fu Cup Tabs",
	"L.A.S.T. Tabs",
	"La Bruma 2019 Tabs",
	"La Grosse Ligue 2019 Tabs",
	"LAN ETS 2014 Tabs",
	"LAN ETS 2015 Tabs",
	"LAN ETS 2016 Tabs",
	"LAN ETS 2017 Tabs",
	"LAN ETS 2018 Tabs",
	"LAN ETS 2019 Tabs",
	"LCD 2017 Tabs",
	"LCD 2018 Tabs",
	"LCD 2019 Tabs",
	"LCK 2017 Tabs",
	"LCK 2018 Tabs",
	"LCK 2019 Tabs",
	"LCL 2016 Tabs",
	"LCL 2017 Tabs",
	"LCL 2018 Tabs",
	"LCL 2019 Tabs",
	"LCM 2018 Tabs",
	"LCS 2019 Tabs",
	"LCS Stream Music Tabs",
	"LDL 2018 Tabs",
	"LDL 2019 Tabs",
	"LDLC Nashor's Trophy Tabs",
	"League of Champions Tabs",
	"League of Draven Tabs",
	"League of Origin 2017 Tabs",
	"League of Origin 2018 Tabs",
	"League One Powered by D!ngIt Tabs",
	"Leaguecraft ggClassic Presented by Arqade Tabs",
	"Leaguecraft ggClassic Tabs",
	"Leaguepedia NA Invitational Tabs",
	"LEC 2019 Tabs",
	"Lega Prima 2016-2017 Tabs",
	"Lega Prima Season 1 Tabs",
	"Lega Prima Season 2 Tabs",
	"Lega Prima Season 3 Tabs",
	"Lega Prima Season 4 Tabs",
	"Lega Seconda Season 1 Tabs",
	"Lega Seconda Season 2 Tabs",
	"Lega Seconda Season 3 Tabs",
	"Legend Series Tabs",
	"LFL 2019 Tabs",
	"LGC 2017 Tabs",
	"LGC 2018 Tabs",
	"LGL 2019 Tabs",
	"LGS 2015 Tabs",
	"LGS 2016 Summer Tabs",
	"LGS 2017 Tabs",
	"LGS 2018 Tabs",
	"LHE 2019 Tabs",
	"Liga Exodo 2013 Tabs",
	"Liga Samsung (Ending 2013) Tabs",
	"Ligue PCS 2018-2019 Tabs",
	"LJL 2015 Tabs",
	"LJL 2016 Tabs",
	"LJL 2017 Tabs",
	"LJL 2018 Tabs",
	"LJL 2019 Tabs",
	"LJLTabs",
	"LLA 2019 Tabs",
	"LLN 2017 Tabs",
	"LLN 2018 Tabs",
	"LMF 2019 Tabs",
	"LMS 2015 Tabs",
	"LMS 2016 Tabs",
	"LMS 2017 Tabs",
	"LMS 2018 Tabs",
	"LMS 2019 Tabs",
	"LNU 2019 Tabs",
	"LOC 2019 Tabs",
	"Logitech G 2016 Tabs",
	"Logitech G 2017 Tabs",
	"Logitech G 2018 Tabs",
	"Logitech G Tabs 2015",
	"Logitech G Tournament 2014 Tabs",
	"Logitech G Tournament 2016 Tabs",
	"LoL Roadshow 2017 Tabs",
	"LoLPro ARAM Tournament Tabs",
	"LoLPro EUW 1v1 Challenge Tournament Tabs",
	"LoLPro NA 1v1 Challenge Tabs",
	"LoLPro NA Dominion Tabs",
	"LoLPro.com Curse Invitational Tabs",
	"Lone Star Clash Tabs",
	"LPL 2013 Tabs",
	"LPL 2014 Tabs",
	"LPL 2015 Tabs",
	"LPL 2017 Tabs",
	"LPL 2018 Tabs",
	"LPL 2019 Tabs",
	"LPLOL 2015 Tabs",
	"LPLOL 2016 Tabs",
	"LPLOL 2017 Tabs",
	"LPLOL 2018 2nd Division Tabs",
	"LPLOL 2018 Tabs",
	"LPLOL 2019 2nd Division Tabs",
	"LPLOL 2019 Tabs",
	"LSPL 2015 Tabs",
	"LSPL 2017 Tabs",
	"LSPLTabs",
	"LST 2019 Tabs",
	"LTL 2019 Tabs",
	"LVP 2018 Tabs",
	"LVP 2019 Tabs",
	"LVP CCS Season 10 Tabs",
	"LVP Season 10 Tabs",
	"LVP Season 11 Tabs",
	"LVP Season 12 Tabs",
	"LVP Season 13 Tabs",
	"LVP Season 6 Tabs",
	"LVP Season 7 Tabs",
	"LVP Season 8 Tabs",
	"LVP Segunda Season 12 Tabs",
	"LVP Segunda Season 13 Tabs",
	"LVP UKLC 2019 Tabs",
	"Malaysian League of Legends 2013 Tournament Tabs",
	"MEB League Tabs",
	"Milan Games Week League 2015 Tabs",
	"Milan Games Week League 2016 Tabs",
	"Millenium Predator Tournament 2015 Tabs",
	"MLG 2012 Tabs",
	"MLG 2013 Tabs",
	"MLG Prizefights Tabs",
	"MLGTabs",
	"MLP Legends Tabs",
	"MNEB Tabs",
	"MOBAFire Challenger Series Tabs",
	"MobaFire King of the Union Tabs",
	"MobaFire Take Your Best Shot Tabs",
	"Most Recent Games Tabs",
	"MSI 2015 Tabs",
	"MSI 2016 Tabs",
	"MSI 2017 Tabs",
	"MSI 2018 Tabs",
	"MSI 2019 Tabs",
	"Musimundo Game Week 2017 Tabs",
	"Musimundo Gaming Week 2018 Tabs",
	"NA Academy League 2018 Tabs",
	"NA Academy League 2019 Tabs",
	"NA LCS 2014 Tabs",
	"NA LCS 2015 Tabs",
	"NA LCS 2016 Tabs",
	"NA LCS 2017 Tabs",
	"NA LCS 2018 Tabs",
	"NA LCS Season 3 Tabs",
	"NACC 2015 Tabs",
	"NACL Kick-off Tabs",
	"NACL Season 1 Tabs",
	"NACL Season 2 Tabs",
	"NACS 2015 Tabs",
	"NACS 2016 Tabs",
	"NACS 2017 Tabs",
	"NASG 2016 Tabs",
	"NASG 2017 Tabs",
	"NASG 2018 Tabs",
	"National ESL Premier League Tabs",
	"National ESL Pro Series Tabs",
	"NEE Baltics 2017 Tabs",
	"NEST 2013 Tabs",
	"NEST 2014 Tabs",
	"NEST 2015 Tabs",
	"NEST 2016 Tabs",
	"NEST 2017 Tabs",
	"NEST 2018 Tabs",
	"Newegg Wanfest Tabs",
	"Nexus Fall League Tabs",
	"NLB 2012 Tabs",
	"NLB 2012-2013 Tabs",
	"NLB 2014 Tabs",
	"Norwegian Esports League 2019 Tabs",
	"NTL Tabs",
	"NVIDIA Game Festival Tabs",
	"Occitan Championship Series 2016 Tabs",
	"Oceanic Championship Season 3 Tabs",
	"Oceanic Regional Tournament 2014 Tabs",
	"OCS 2015 Tabs",
	"OCS 2016 Tabs",
	"OCS 2017 Tabs",
	"OCS 2018 Tabs",
	"OGN 2012 Tabs",
	"OGN 2015 Tabs",
	"OGN Club Masters Tabs",
	"OMEN by HP TROPHY Tabs",
	"OnGameNet LoL Invitational Tabs",
	"Open Tour France 2018 Tabs",
	"Open Tour France 2019 Tabs",
	"OPL 2015 Tabs",
	"OPL 2016 Tabs",
	"OPL 2017 Tabs",
	"OPL 2018 Tabs",
	"OPL 2019 Tabs",
	"Ozone Evolution Cup Tabs",
	"Ozone Masters League 2014 Summer Tabs",
	"PG Nationals 2018 Tabs",
	"PG Nationals 2019 Tabs",
	"PGL Legends of the Rift Season 1 Tabs",
	"PGS 2014 Tabs",
	"PGS 2015 Tabs",
	"PGS 2016 Tabs",
	"PGS 2017 Tabs",
	"PGS 2018 Tabs",
	"PGW 2012 Tabs",
	"Plantronics RuLoL League Tabs",
	"PLAY RaidCall Showmatch Tabs",
	"Playhem Showmatch Tabs",
	"PLE 2017 Tabs",
	"PLE 2018 Tabs",
	"PMU Challenge Tabs",
	"PPGL 2018 Tabs",
	"PPGL 2019 Tabs",
	"Premier Tour 2018 Tabs",
	"PROG4MER League Season 1 Tabs",
	"Pros Play for the Philippines Tabs",
	"Pryde Invitational Tabs",
	"PTL 2017 Tabs",
	"PTT-Ace Champion League Tabs",
	"RaidCall Dominance 1 Tabs",
	"RaidCall PLAY Tabs",
	"Razer Challenge 2015 Tabs",
	"Razor League Tabs",
	"RB Itemania Tabs",
	"Red Bull Factions 2018 Tabs",
	"Red Bull Strijders 2019 Tabs",
	"Reign of Gaming International Invitational Tabs",
	"Rift Rivals 2017 Tabs",
	"Rift Rivals 2018 Tabs",
	"Rift Rivals 2019 Tabs",
	"RioDeLaPlataTabs",
	"Riot Games Turkey 2013 Tabs",
	"Riot Official Showmatch - Brazil Server Opening Ceremony Tabs",
	"Riot Open 2016 Tabs",
	"Riot Open 2017 Tabs",
	"Rising Stars Invitational Tabs",
	"RO 2018 Tabs",
	"ROCCAT King of the Hill 2013-2014 Tabs",
	"ROCCAT King Of The Hill Tabs",
	"Roster Swaps 2015 Tabs",
	"Roster Swaps 2016 Midseason Tabs",
	"Roster Swaps 2016 Preseason Tabs",
	"Roster Swaps 2017 Midseason Tabs",
	"Roster Swaps 2017 Preseason Tabs",
	"Roster Swaps 2018 Midseason Tabs",
	"Roster Swaps 2018 Preseason Tabs",
	"Roster Swaps 2019 Preseason Tabs",
	"S3 Worlds Tabs",
	"S3BRTabs",
	"S3SEATabs",
	"SCA 2015 Tabs",
	"SCAN and NVIDIA EUW Invitational Tabs",
	"SCAN EUW Winter Invitational Tabs",
	"SCAN Invitational Tabs",
	"SCAN UK Legends League Tabs",
	"Season 3 China Regional Finals Tabs",
	"Season 3 LAT Regional Finals Tabs",
	"SESL 2018 Tabs",
	"SESL 2019 Tabs",
	"Singapore Legends 2017 Tabs",
	"Singapore Legends 2018 Tabs",
	"SK Telecom LTE-A LoL Masters 2014 Tabs",
	"SK Trophy Tabs",
	"SML 2015 Tabs",
	"Solomid EU Tournament Circuit Tabs",
	"Solomid NA Invitational Tabs",
	"SoloMid Series Tabs",
	"Sound Blaster Nations Championship Tabs",
	"StarSeries 2015 Tabs",
	"StarsWar Cup Tabs",
	"Summoner's Inn League 2nd Division Tabs",
	"Summoner's Inn League Tabs",
	"Superliga 2017 Tabs",
	"Superliga ABCDE 2017 Tabs",
	"Superliga ABCDE 2018 Tabs",
	"Swedish Esports League 2019 Tabs",
	"Taiwan Championship Legend 2018 Tabs",
	"Taiwan Season 3 Regional Finals Tabs",
	"Tales of the Lane Tabs",
	"Taoyuan District e-Sports Tabs",
	"TCL 2014 Tabs",
	"TCL 2015 Tabs",
	"TCL 2016 Tabs",
	"TCL 2017 Tabs",
	"TCL 2018 Tabs",
	"TCL 2019 Tabs",
	"TCS 2018 Tabs",
	"TDTV 2013 Tabs",
	"TDTVWeeklyTabs",
	"TeSL Tabs",
	"TGA 2012 Tabs",
	"TGA 2013 Tabs",
	"Thailand Grand Championship 2013 Tabs",
	"Thailand Pro League 2014 Tabs",
	"Thailand Pro League 2015 Tabs",
	"Thailand Pro League 2016 Tabs",
	"The Gathering 2012 Tabs",
	"The Rookie League Summer Edition 2013 Tabs",
	"The Siege Tabs",
	"The Solo King Tabs",
	"THOR Open 2012 Tabs",
	"TLC 2014 Tabs",
	"TLC 2016 Tabs",
	"TLC 2017 Tabs",
	"Torneo Nazionale Italiano 2016 Tabs",
	"Torneos Espacio Personal Tabs",
	"Tournament Portal Tabs",
	"TPL 2015 Tabs",
	"TPL 2016 Tabs",
	"TPL 2017 Tabs",
	"TPL 2018 Tabs",
	"Tristana's 32 The Tt Cup Tabs",
	"TteSports Challenge Summer Open Tabs",
	"Turkey Academy League 2019 Tabs",
	"Tyler1 Championship Series 2017 Tabs",
	"Tyler1 Championship Series 2018 Tabs",
	"UEG League Tabs",
	"ULoL 2016 Tabs",
	"ULOL 2017 Tabs",
	"Ultraliga 2019 Tabs",
	"Ultraliga Season 0 Tabs",
	"Underdogs 2016 Autumn Tabs",
	"Underdogs Spring Split 2017 Tabs",
	"Underdogs Summer Split 2017 Tabs",
	"UPL 2018 Tabs",
	"UPL 2019 Tabs",
	"UWC Tabs",
	"V4 Future Sports Festival Tabs",
	"VCS 2014 Tabs",
	"VCS 2015 Tabs",
	"VCS 2018 Tabs",
	"VCS 2019 Tabs",
	"VCS B 2014 Tabs",
	"VCS B 2018 Tabs",
	"VCS B 2019 Tabs",
	"VCSTabs",
	"WCA 2015 Tabs",
	"WCG 2011 Tabs",
	"WCG 2013 Tabs",
	"WCGTabs",
	"WellPlayed Cup Tabs",
	"Wichita eSports 2017 Tabs",
	"Wichita eSports 2018 Tabs",
	"Wichita eSports 2019 Tabs",
	"Women's Esports League Season 1 Tabs",
	"World Championship Season 1 Tabs",
	"World Championships Overview Tabs",
	"World Cyber Arena 2016 Tabs",
	"World e-Sports Masters Tabs",
	"World GameMaster Tournament Tabs",
	"Worlds 2014 Tabs",
	"Worlds 2015 Tabs",
	"Worlds 2016 Tabs",
	"Worlds 2017 Tabs",
	"Worlds 2018 Tabs",
	"Worlds 2019 Tabs",
	"Worlds 2020 Tabs",
	"Worlds 2021 Tabs",
	"Worlds Season 2 Tabs",
	"WVW National Elite Cup Tabs",
	"WWDIOC Tabs",
	"X5 Mega Arena Tabs",
	"XLG 2015 Tabs",
	"XLG SuperCup 2016 Tabs",
	"YouSee Ligaen Tabs",
]

limit = -1
# startat_page = 'asdf'
for this_template_name in all_templates:
	print('Starting template %s...' % this_template_name)
	this_template = site.pages['Template:' + this_template_name]  # Set template
	pages = this_template.embeddedin()
	
	lmt = 0
	for page in pages:
		text = page.text()
		wikitext = mwparserfromhell.parse(text)
		for template in wikitext.filter_templates():
			if template.name.matches(this_template_name):
				for param in template.params:
					template.remove(param.name)
		newtext = str(wikitext)
		if text != newtext:
			print('Saving page %s...' % page.name)
			page.save(newtext, summary=summary)
		else:
			print('Skipping page %s...' % page.name)