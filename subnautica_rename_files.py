from copy import copy

from mwcleric.fandom_client import FandomClient
from mwcleric.auth_credentials import AuthCredentials
from mwcleric.page_modifier import PageModifierBase
from mwparserfromhell.nodes import Tag, Template

credentials = AuthCredentials(user_file="me")
site = FandomClient('subnautica-belowzero', credentials=credentials)
summary = 'Updating wiki for incoming merger'

pages = {
    "Advanced Wiring Kit": "Advanced Wiring Kit (Below Zero)",
    # snip
    "X Compartment": "X Compartment (Below Zero)",
}

templates = {
    "Template:!": "Template:! (BZ)",
    # snip
    "Template:Warning": "Template:Warning (BZ)",
}

files = {
    "File:2015-04-14 00101.jpg": "File:2015-04-14 00101 (BZ).jpg",
    # snip
    "File:ZoeyConstellaFinal.png": "File:ZoeyConstellaFinal (BZ).png",
}

# make a copy object that contains all of the elements of pages, templates, and files, instead of changing
# any one of these objects in place
to_move = {}
to_move.update(pages)
to_move.update(templates)
to_move.update(files)


def move_pages():
    startat_page = 'File:Arctic Peeper Fauna.png'
    passed_startat = False
    for source, dest in to_move.items():
        if source == startat_page:
            passed_startat = True
        if not passed_startat:
            continue
        source_page = site.client.pages[source]
        if source_page.exists:
            text = source_page.text()
            if 'redirect' in text.lower():
                print("omg it's a redirect! {}".format(source))
                continue
            # site.move(source_page, dest, no_redirect=True, reason=summary)


class PageModifier(PageModifierBase):
    def update_plaintext(self, text):
        # We're assuming there's no underscores in any page or file or template name in the entire wiki
        
        # embedded files - File: is already part of the page name
        for source, dest in files.items():
            text = text.replace('[[{}'.format(source), '[[{}'.format(dest))
        # links to files
        for source, dest in files.items():
            text = text.replace('[[:{}'.format(source), '[[:{}'.format(dest))
        
        # links to pages (no display text)
        for source, dest in pages.items():
            text = text.replace('[[{}]]'.format(source), '[[{}|{}]]'.format(dest, source))
        # links to pages (display text)
        for source, dest in pages.items():
            text = text.replace('[[{}|'.format(source), '[[{}|'.format(dest))
        # links to pages (display text with pipes)
        for source, dest in pages.items():
            text = text.replace('[[{}{{{{!}}}}'.format(source), '[[{}{{{{!}}}}'.format(dest))
        return text
    
    def update_wikitext(self, wikitext):
        
        infoboxes = ['Flora', 'Fauna', 'Biome', 'Craftable']
        infoboxes_copy = copy(infoboxes)
        for infobox in infoboxes:
            infoboxes_copy.append(infobox + ' (BZ)')
        infoboxes = copy(infoboxes_copy)
        for infobox in infoboxes_copy:
            infoboxes.append('Template:' + infobox)
        
        for template in wikitext.filter_templates():
            template: Template
            template_name = template.name
            
            # case of replacing images in infobox
            if any([template_name.matches(x) for x in infoboxes]):
                self.update_image(template, 'image1')
                self.update_image(template, 'image2')
                self.update_image(template, 'image3')
            
            if any([template_name.matches(x) for x in
                    ['Recipe2', 'Template:Recipe2', 'Recipe2 (BZ)', 'Template:Recipe2 (BZ)']]):
                self.update_page(template, 1)
                self.update_page(template, 'page')
            
            # case of replacing embedded templates
            for source, dest in templates.items():
                if template_name.matches(source) or template_name.matches(source.replace('Template:', '')):
                    template.name = dest.replace('Template:', '')
        
        # case of updating galleries
        for tag in wikitext.filter_tags():
            tag: Tag
            if not tag.tag == 'gallery':
                continue
            contents = str(tag.contents)
            lines = contents.split('\n')
            for i, line in enumerate(lines):
                # let's not randomly add File: if we're not *actually* updating a file link here ok
                matched = False
                please_remove_file = False
                if not line.startswith('File:'):
                    please_remove_file = True
                    line = 'File:' + line
                for source, dest in files.items():
                    if line.startswith(source):
                        if please_remove_file:
                            dest = dest.replace('File:', '')
                        line = line.replace(source, dest)
                        matched = True
                if matched:
                    lines[i] = line
            tag.contents = '\n'.join(lines)
    
    @staticmethod
    def update_image(template, param_name):
        if not template.has(param_name):
            return
        cur_value = template.get(param_name).value.strip()
        for source, dest in files.items():
            # they could've put either File:Filename or just Filename as the param value
            if cur_value == source:
                template.add(param_name, dest)
                return
            # we'll break up the cases so we do minimal disruption
            if cur_value == source.replace('File:', ''):
                template.add(param_name, dest.replace('File:', ''))
                return
    
    @staticmethod
    def update_page(template, param_name):
        if not template.has(param_name):
            return
        cur_value = template.get(param_name).value.strip()
        for source, dest in pages.items():
            if cur_value == source:
                template.add(param_name, dest)
                return


if __name__ == '__main__':
    # PageModifier(site, page_list=site.client.allpages(),
    #              summary=summary).run()
    move_pages()
