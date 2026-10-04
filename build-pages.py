from pathlib import Path
import re,json,html
root=Path('dist'); home=Path('content/home.html').read_text();projects=json.loads(Path('content/projects.json').read_text());slugs=['sonor','vanta-form','other-realities','form-digital'];cats=['brand','photography','ai','digital']
for p,s,c in zip(projects,slugs,cats):p.update(slug=s,category=c)
menu=re.search(r'<dialog id="menuDialog".*?</dialog>',home,re.S).group()
header=re.search(r'<header.*?</header>',home,re.S).group()
footer=re.search(r'<footer.*?</footer>',home,re.S).group()
links={'#home':'/','#work':'/work/','#about':'/about/','#practice':'/practice/','#journal':'/journal/','#contact':'/contact/'}
def convert(s):
 for a,b in links.items():s=s.replace('href="'+a+'"','href="'+b+'"')
 s=s.replace('src="assets/','src="/assets/')
 s=re.sub(r'<button([^>]*data-project="(\d+)"[^>]*)>(.*?)</button>',lambda m:'<a'+m[1]+' href="/work/'+slugs[int(m[2])]+'/">'+m[3]+'</a>',s,flags=re.S)
 s=re.sub(r'<button([^>]*id="contactOpen2?"[^>]*)>(.*?)</button>',lambda m:'<a'+m[1]+' href="/contact/">'+m[2]+'</a>',s,flags=re.S)
 return s
header=convert(header);footer=convert(footer);menu=convert(menu)
menu=menu.replace('<nav>','<nav><a href="/">Home <small>00</small></a>')
head='<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#eeeae2"><title>{title} | Alex Mercer</title><meta name="description" content="{desc}"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css"><script src="/app.js" defer></script></head>'
def page(path,title,desc,body,extra=''):
 out=root/path/'index.html';out.parent.mkdir(parents=True,exist_ok=True)
 active='/' + path.split('/')[0] + '/' if path else '/'
 navmenu=menu.replace('href="'+active+'"','aria-current="page" href="'+active+'"')
 s=head.format(title=html.escape(title),desc=html.escape(desc,quote=True))+'<body class="inner-page '+extra+'"><a class="skip" href="#main">Skip to content</a>'+header+'<main id="main">'+body+footer+'</main>'+navmenu+'</body></html>'
 out.write_text(s)
def intro(kicker,title,desc):return f'<section class="page-intro"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="page-lead">{desc}</p></section>'
def card(p,i):return f'<a class="archive-card" href="/work/{p["slug"]}/" data-category="{p["category"]}"><div><img src="/{p["cover"]}" alt="{p["title"]} project" loading="lazy"><span>0{i+1} / 2026</span></div><h2>{p["title"]}</h2><p>{p["role"]}</p></a>'
# Homepage remains its own cinematic introduction.
h=convert(home)
h=re.sub(r'<dialog id="projectDialog".*?</dialog>','',h,flags=re.S);h=re.sub(r'<dialog id="contactDialog".*?</dialog>','',h,flags=re.S)
h=re.sub(r'<dialog id="menuDialog".*?</dialog>',menu,h,flags=re.S)
h=h.replace('href="style.css"','href="/style.css"').replace('src="app.js"','src="/app.js"').replace('href="favicon.svg"','href="/favicon.svg"')
h=h.replace('href="/work/">SCROLL TO EXPLORE','href="#work">SCROLL TO EXPLORE')
h=h.replace('<span>SCROLL THROUGH THE COLLECTION</span>','<a href="/work/">VIEW ALL PROJECTS</a>')
h=h.replace('<p>Design is my foundation. Photography keeps me looking. Code and AI open up new ways to make the impossible feel real.</p>','<div><p>Design is my foundation. Photography keeps me looking. Code and AI open up new ways to make the impossible feel real.</p><a class="inline-link" href="/about/">More about me</a></div>')
h=h.replace('class="journal-wide" href="/work/vanta-form/"','class="journal-wide" href="/journal/finding-form/"').replace('data-project="2" href="/work/other-realities/"><img src="/assets/ai-art.png" alt="Experimental','data-project="2" href="/journal/different-reality/"><img src="/assets/ai-art.png" alt="Experimental')
root.joinpath('index.html').write_text(h)
# Work archive.
body=intro('01 / SELECTED WORK','IDEAS MADE<br><em>VISIBLE.</em>','Identity, image-making and digital experiences. A collection of things made with intention.')
body+='<section class="archive-section"><div class="archive-filters" role="group" aria-label="Filter projects">'+''.join(f'<button data-filter="{v}" aria-pressed="{str(i==0).lower()}" class="{"active" if i==0 else ""}">{label}</button>' for i,(v,label) in enumerate([('all','All work'),('brand','Brand design'),('photography','Photography'),('ai','AI & art direction'),('digital','Digital')]))+'</div><p id="filterStatus" class="filter-status" role="status">4 projects</p><div class="archive-grid">'+''.join(card(p,i) for i,p in enumerate(projects))+'</div></section>'
page('work','Selected Work','Explore brand identities, photography, AI experiments and digital design by Alex Mercer.',body)
# About.
body=intro('02 / THE PERSON BEHIND THE WORK','CURIOUS BY<br><em>DESIGN.</em>','A creative practice shaped by observation, experimentation and a belief that the best work should make you feel something.')
body+='<section class="biography"><div class="bio-portrait"><span aria-hidden="true">AM</span><img src="/assets/designer.png" alt="Alex Mercer, fictional creative designer"></div><div class="bio-copy"><p class="eyebrow">ALEX MERCER / INDEPENDENT CREATIVE</p><h2>Thinking clearly.<br>Making boldly.</h2><p>I’m a multidisciplinary creative designer working across brand identity, photography, art direction and the web. I enjoy finding the simple idea inside a complicated brief, then giving it a distinctive visual life.</p><p>My process moves between a sketchbook, a camera and a screen. Sometimes the answer is a carefully chosen typeface. Sometimes it’s an unexpected image. The medium changes, but the intention stays the same: make the work meaningful.</p><p>I use AI as part of an exploratory process, guided by art direction and a considered point of view. Curiosity opens the door. Judgment decides what belongs.</p><span class="signature">Alex M.</span></div></section><section class="beliefs"><p class="eyebrow">A FEW THINGS I BELIEVE</p><div><article><span>01</span><h3>Start with a reason.</h3><p>A clear idea gives every design decision something to stand on.</p></article><article><span>02</span><h3>Stay open.</h3><p>The next useful thought might come from somewhere outside the brief.</p></article><article><span>03</span><h3>Care about the details.</h3><p>The small decisions shape how the whole experience feels.</p></article></div><a class="pill accent" href="/practice/">Explore my practice</a></section>'
page('about','About','Meet Alex Mercer, an independent creative designer working across design, photography and digital experiences.',body)
# Practice page.
body=intro('03 / HOW I WORK','MANY TOOLS.<br><em>ONE POINT OF VIEW.</em>','From the first question to the final detail, every discipline is a different way to bring an idea into focus.')
services=[('Brand design','A distinctive visual language, grounded in a clear idea.','Positioning & creative direction|Visual identity & typography|Brand guidelines & applications'),('Photography','Images that communicate through light, composition and character.','Campaign concepts|Portrait & editorial direction|Image selection & visual storytelling'),('AI & art direction','A space for visual exploration and carefully directed possibilities.','Concept development|AI-assisted image exploration|Visual worlds & campaign studies'),('Digital experiences','Websites with a point of view and a thoughtful path through the content.','UI & responsive web design|Interaction & motion direction|Creative front-end development')]
body+='<section class="services-list">'
for i,(title,desc,items) in enumerate(services):
 p=projects[i];body+=f'<article class="service-row"><span class="service-number">0{i+1}</span><div><h2>{title}</h2><p>{desc}</p><ul>'+''.join('<li>'+x+'</li>' for x in items.split('|'))+f'</ul><a class="inline-link" href="/work/{p["slug"]}/">View a related project</a></div><a href="/work/{p["slug"]}/"><img src="/{p["cover"]}" alt="{p["title"]} project" loading="lazy"></a></article>'
body+='</section><section class="process dark"><p class="eyebrow">THE PROCESS</p><h2>GOOD QUESTIONS.<br>BETTER OUTCOMES.</h2><div class="process-grid"><article><span>01 / DISCOVER</span><h3>Find the real question.</h3><p>Understand the audience, the ambition and what the work needs to change.</p></article><article><span>02 / EXPLORE</span><h3>Give the idea room.</h3><p>Build a direction through references, sketches and focused experiments.</p></article><article><span>03 / REFINE</span><h3>Make every choice count.</h3><p>Test the idea in context, refine the details and bring the system together.</p></article></div></section>'
page('practice','Practice','Brand design, photography, AI art direction and digital design services.',body)
# Projects, each directly linkable with editorial detail and mixed image formats.
for i,p in enumerate(projects):
 nxt=projects[(i+1)%4]
 body=f'<section class="case-header"><a class="pill back-to-projects" href="/work/">Back to projects</a><p class="eyebrow">{p["type"]}</p><h1>{p["title"]}</h1><p class="page-lead">{p["lead"]}</p><div class="case-meta"><span>{p["role"]}</span><span>2026</span><span>SELF-INITIATED CONCEPT</span></div></section><div class="case-cover"><img src="/{p["cover"]}" alt="{p["title"]} project overview" fetchpriority="high"></div><section class="case-story"><h2>The idea.</h2><p>{p["story"]}</p></section>'
 body+='<section class="project-work-grid" aria-label="Project images">'
 for n,g in enumerate(p['gallery']):
  solo=' gallery-solo' if g['orientation']=='portrait' and (n==len(p['gallery'])-1 and (n==0 or p['gallery'][n-1]['orientation']!='portrait')) else ''
  body+=f'<figure class="gallery-{g["orientation"]}{solo}"><img src="/{g["src"]}" alt="{html.escape(g["alt"],quote=True)}" width="{g.get("width", 1000)}" height="{g.get("height", 1500 if g["orientation"]=="portrait" else 750)}" loading="lazy"><figcaption><span>0{n+2}</span>{html.escape(g["caption"])}</figcaption></figure>'
 body+='</section><div class="project-return"><a class="pill back-to-projects" href="/work/">Back to projects</a></div>'
 body+=f'<section class="case-end"><p class="eyebrow">KEEP EXPLORING</p><a href="/work/{nxt["slug"]}/"><span>Next project</span><h2>{nxt["title"]}</h2><img src="/{nxt["cover"]}" alt="{nxt["title"]} preview" loading="lazy"></a></section>'
 page('work/'+p['slug'],p['title'],p['lead'],body,'case-page')
# Journal and real individual article routes.
articles=[{'slug':'finding-form','title':'Finding form in the everyday','tag':'PHOTOGRAPHY / FIELD NOTES 01','img':'assets/campaign.png','lead':'A wall, a shadow, a pause. Looking for a visual story before reaching for the camera.','paras':[('Start by noticing','Before deciding on a frame, I look for relationships: the line of a shoulder against a building, a dark silhouette inside a pool of light, a small gesture that changes the mood. The location becomes part of the image’s structure.'),('Let the space contribute','For the Vanta Form study, concrete architecture offered a useful counterpoint to the clothing. Hard edges made the fabric feel softer. Large empty areas gave the silhouettes space. The setting helped tell the story without competing with it.'),('Build a sequence','A strong image matters, but a sequence gives it context. I look for a balance of wide views and closer portraits, stillness and movement. Together they can describe a world that no single frame could hold.')]},{'slug':'different-reality','title':'A different kind of reality','tag':'EXPERIMENTS / FIELD NOTES 02','img':'assets/ai-art.png','lead':'Using AI to explore an idea while keeping a clear creative point of view.','paras':[('Define the tension','The starting point for Other Realities was a material contrast: hard chrome, translucent glass and a quiet landscape. Defining that relationship first gave the exploration a direction beyond simply making something unusual.'),('Direct, then edit','Image generation can produce possibilities quickly. The more useful work is deciding which choices support the idea: where the light comes from, how the object sits in space, what the colour is doing. Selection and refinement are part of the creative process.'),('Stay honest about the medium','This is an AI-assisted visual study, not a photograph of a physical sculpture. Being clear about that context leaves room to appreciate the image as an exploration of form, light and imagined materials.')]}]
body=intro('04 / FIELD NOTES','OUTSIDE<br><em>THE BRIEF.</em>','Observations from the process. A place for images, experiments and the ideas that happen between projects.')+'<section class="notes-grid">'
for a in articles:body+=f'<a href="/journal/{a["slug"]}/"><img src="/{a["img"]}" alt="{a["title"]}" loading="lazy"><p class="eyebrow">{a["tag"]}</p><h2>{a["title"]}</h2><p>{a["lead"]}</p><span class="inline-link">Read the note</span></a>'
body+='</section>';page('journal','Field Notes','Notes on photography, creative process and AI image making.',body)
for i,a in enumerate(articles):
 body='<section class="article-header"><a class="back-link" href="/journal/">All field notes</a><p class="eyebrow">'+a['tag']+'</p><h1>'+a['title']+'</h1><p class="page-lead">'+a['lead']+'</p></section><img class="article-image" src="/'+a['img']+'" alt="'+a['title']+'"><article class="article-body">'
 for title,para in a['paras']:body+='<h2>'+title+'</h2><p>'+para+'</p>'
 body+='<a class="pill accent" href="/work/'+('vanta-form' if i==0 else 'other-realities')+'/">Explore the project</a></article>'
 page('journal/'+a['slug'],a['title'],a['lead'],body)
# Contact has an honest usable local brief workflow, no invented mailbox.
body=intro('05 / LET’S TALK','SOMETHING<br><em>IN MIND?</em>','Good collaborations start with a clear idea. Put a few thoughts together for your next project.')
body+='<section class="contact-layout"><div><h2>Make a little<br>room for possibility.</h2><p>Brand identity, a campaign, a digital experience, or something that does not fit neatly into a category.</p><div class="contact-note"><span class="eyebrow">TEMPLATE PREVIEW</span><p>Alex Mercer is a fictional designer. This form prepares a project brief on your device. It does not send a message. Add your real email or booking link when customising the template.</p></div></div><form id="briefForm"><label for="briefName">Your name</label><input id="briefName" name="name" autocomplete="name" placeholder="What should I call you?" required><label for="briefEmail">Your email</label><input id="briefEmail" name="email" type="email" autocomplete="email" placeholder="you@example.com" required><label for="briefType">What are you thinking?</label><select id="briefType" name="type"><option>Brand design</option><option>Photography</option><option>AI & art direction</option><option>Digital experience</option><option>A bit of everything</option></select><label for="briefMessage">A little about the project</label><textarea id="briefMessage" name="message" rows="5" placeholder="The idea, the ambition, and any timing you have in mind…" required></textarea><button class="pill accent" type="submit">Download project brief</button><p id="briefStatus" role="status"></p></form></section>'
page('contact','Contact','Prepare a creative project brief for brand, photography, art direction or digital design.',body)
print('Built',len(list(root.rglob('*.html'))),'pages')
