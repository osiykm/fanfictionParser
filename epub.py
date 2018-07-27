text = '''<div role="main" aria-label="story content" class="storytextp" id="storytextp" align="center" style="padding:0 0.5em 0 0.5em;">
<div class="storytext xcontrast_txt nocopy" id="storytext"><p><strong>*I don't own anything! All characters besides an OC I will add later belong to Kishimoto, the creator of the Naruto manga :)*</strong></p><p>Make me your apprentice!</p><p>"Naruto!" She couldn't get the noise of metal hitting skin, mixed with his scream, out of her head all day. Naruto had gotten hirt because of her, that's all Sakura could think of. His face and words echoed through her head as she made her way up the shadowed path to the Hokage's office, like a constant reminder of her failure on their last mission.</p><p>He had told her that he'd keep her safe. That she could count on him for anything. And she hated it, the knowledge that she was the reason he was hurt again. "Never again" she promised herself, dipping her head so that her hair shadowed her facial features. "Don't worry Naruto, because the next time we meet I'll be able to carry my own weight".</p><p>Sakura stopped at the large wood door separating her from the 5th Hokage nervously. No excuses Sakura! It's now or never, you have to do this, for Naruto...for Sasuke." Right. This was her chance. Without anymore hesitation, she pushed open the door and squared her shoulders bravely. Tsunade glanced up, raising an eyebrow at the genin's sudden appearance. "Sakura? Is something wrong?" she asked, eyeeyes narrowing with concern at the girls odd stance.</p><p>Sakura took a deep breath, before mustering all the confidence she could. "Tsunade-sama, I would like you to take me on as your apprentice!"</p>
</div>
</div>
'''
from ebooklib import epub

book = epub.EpubBook()

# set metadata
book.set_identifier('id123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Author Authorowski')
book.add_author('Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')

# create chapter
c1 = epub.EpubHtml(title='Intro', file_name='chap_01.xhtml', lang='hr')
c1.content=text

# add chapter
book.add_item(c1)

# define Table Of Contents
book.toc = [c1, c1, c1]

# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ['nav', c1]

# write to the file
epub.write_epub('test.epub', book, {})
