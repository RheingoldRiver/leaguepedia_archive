import logging
from time import sleep

from lol_esports_parser import get_riot_game
from mwcleric.auth_credentials import AuthCredentials
from mwparserfromhell.nodes import Template
from mwparserfromhell.nodes.extras import Parameter
from mwrogue.esports_client import EsportsClient
from mwrogue.template_modifier import TemplateModifierBase
from requests import HTTPError

credentials = AuthCredentials(user_file="bot")
site = EsportsClient('lol', credentials=credentials)
summary = 'Add primary rune tree'

# there's tons of warnings about old patch versions that we don't care about,
# it's just gonna slow execution so disable warnings
logging.disable(logging.WARNING)


class TemplateModifier(TemplateModifierBase):
    def update_template(self, template: Template):
        # i just added more and more checks to avoid crashing on LPL games over time
        if any([_ in self.current_page.name for _ in ['LPL', 'LDL', 'Demacia']]):
            return
        for param in template.params:
            if '|primary=' in str(param.value):
                return
        if not template.has('statslink'):
            return
        mh = template.get('statslink').value.strip()
        if 'lpl.qq' in mh:
            return
        if 'wanplus' in mh:
            return
        if not mh:
            return
        # sigh ok hopefully we actually have a valid mh now
        print(f'Parsing mh {mh} on page {self.current_page.name}')
        try:
            result = get_riot_game(mh, add_names=True)
        except HTTPError:
            sleep(10)
            result = get_riot_game(mh, add_names=True)
        for param in template.params:
            param: Parameter
            if param.name.startswith('blue') or param.name.startswith('red'):
                # hax, sorry
                team = 'BLUE' if param.name.startswith('blue') else 'RED'
                player = int(param.name[-1]) - 1

                w = param.value
                for tl in w.filter_templates():
                    tl: Template
                    if not tl.name.matches('Scoreboard/Player'):
                        continue
                    primary = result['teams'][team]['players'][player]['primaryRuneTreeName']
                    tl.add('primary', primary, before='secondary')


TemplateModifier(site, 'Scoreboard/Season 8',
                 page_list=site.pages_using('Scoreboard/Player/Runes'),
                 startat_page='Open Tour Benelux/2021 Season/Spring Split/Scoreboards/Week 2',
                 summary=summary).run()
