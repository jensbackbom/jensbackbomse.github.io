# -*- coding: utf-8 -*-

import re
import random
import unicodedata

def transliterate(string):
    """
    Replace non-ASCII characters with an ASCII approximation. If no
    approximation exists, the non-ASCII character is ignored. The string must
    be ``unicode``.

    Examples::

        >>> transliterate('älämölö')
        'alamolo'
        >>> transliterate('Ærøskøbing')
        'rskbing'

    """
    normalized = unicodedata.normalize('NFKD', string)
    return normalized.encode('ascii', 'ignore').decode('ascii')

def parameterize(string, separator='-'):
    """
    Replace special characters in a string so that it may be used as part of a
    'pretty' URL.

    Example::

        >>> parameterize(u"Donald E. Knuth")
        'donald-e-knuth'

    """
    string = transliterate(string)
    # Turn unwanted chars into the separator
    string = re.sub(r"(?i)[^a-z0-9\-_]+", separator, string)
    if separator:
        re_sep = re.escape(separator)
        # No more than one of the separator in a row.
        string = re.sub(r'%s{2,}' % re_sep, separator, string)
        # Remove leading/trailing separator.
        string = re.sub(r"(?i)^{sep}|{sep}$".format(sep=re_sep), '', string)

    return string.lower()



services=[
	{
    "gender": u"Ett",
	"name":u"CRM-system",
	"intro":u"Företagets kundregister är ett av de viktigaste IT-systemen, och den totala marknaden för CRM-system är gigantisk. Det bör finnas stora möjligheter att skräddarsy ett CRM-system för specifika branscher, och ändå kunna bygga ett relativt stort bolag!",
	"business_model":u"Årsavgift per användare.",
	"price_per_unit": 4000,
	"competitors":u"Salesforce, Hubspot, Pipedrive m fl.",
	"competitor_market_size":"",
    "exceptions": ["VD:ar", "CTO:er", "marknadschefer"],
    "role": False
	},
	{
    "gender": u"Ett",
	"name":u"community",
	"intro":u"Betalda medlemscommunities har börjat växa till sig som affärsmodell de senaste åren, och det finns förmodligen en marknad för att göra detta mot nischade målgrupper.",
	"business_model":u"Årssavgift per användare.",
	"price_per_unit": 10000,
	"competitors":u"VD-nätverk såsom Close, EGN etc.",
	"competitor_market_size":"",
    "exceptions": [],
    "role": True
	},
	{
    "gender": u"Ett",
	"name":u"personalundersökningsverktyg",
	"intro":u"Det blir allt vanligare att företag gör regelbundna personalundersökningar, dels en större årlig undersökning där man frågar allmäna saker kring anställningen, men även regelbundna mikroundersökningar för att kolla hur personalen mår. Kanske finns det en marknad för nischade undersökningar, där deltagande företag kan få skräddarsydd, branschanpassad statistik.",
	"business_model":u"Årssavgift per användare.",
	"price_per_unit": 1500,
	"competitors":u"bolag såsom WinningTemp, &Frankly m fl.",
	"competitor_market_size":"",
    "exceptions": ["VD:ar", "CTO:er", "marknadschefer"],
    "role": False
	},
	{
    "gender": u"Ett",
	"name":u"modernt utbildningsföretag",
    "preposition":"riktat mot",
	"intro":u"Alla yrkeskategorier behöver fortbildning, men många e-learningtjänster är hopplöst generella och statiska. Om man gör det bransch- eller rollspecifikt med kohort-baserade liveutbildningar över Zoom så borde det gå att öka relevansen avsevärt!",
	"business_model":u"Årssavgift per användare.",
	"price_per_unit": 15000,
	"competitors":u"bolag i stil med LinkedIn learning, Udemy m fl.",
	"competitor_market_size":"",
    "exceptions": [],
    "role": True
	},
    {
    "gender": u"En",
    "name":u"e-handelsplattform",
    "intro":u"Digitaliseringen av samhället pågår för fullt, men fortfarande utgör e-handel bara c:a 15% av fysisk handel. Lösningar såsom Shopify gör det möjligt för små företag att börja med e-handel, men det skulle eventuellt kunna finnas utrymme för branschspecifika varianter, ungefär som Etsy för hantverk.",
    "business_model":u"Årssavgift per användare (eller möjligen en transaktionsavgift).",
    "price_per_unit": 5000,
    "competitors":u"Shopify, Amazon, Etsy m fl.",
    "competitor_market_size":"",
    "exceptions": ["VD:ar", "CTO:er", "marknadschefer"],
    "role": True
    },
    {
    "gender": u"Ett",
    "name":u"prissättningsverktyg",
    "intro":u"För företag som har ett större antal produkter och säljer via flera kanaler är det värt att optimera sin prissättning.",
    "business_model":u"Årssavgift per användare",
    "price_per_unit": 10000,
    "competitors":u"I huvudsak Excel.",
    "competitor_market_size":"",
    "exceptions": ["VD:ar", "CTO:er", "marknadschefer"],
    "role": True
    },
    {
    "gender": u"En",
    "name":u"upphandlingsplattform",
    "intro":u"Om man är en stor organisation så kan man ofta förhandla sig till bättre priser tack vare stora inköpsvolymer, men även många små företag skulle kunna gå ihop och pressa priser tillsammans. Detta borde vara en lämplig tjänst att bygga branschspecifikt.",
    "business_model":u"Årssavgift per användare",
    "price_per_unit": 5000,
    "competitors":u"Aktörer såsom t.ex. Pressa.se.",
    "competitor_market_size":"",
    "exceptions": ["VD:ar", "CTO:er", "marknadschefer"],
    "role": True
    },
    {
    "gender": u"En",
    "name":u"franchisekedja",
    "preposition": "av",
    "intro":u"Det har skapats många kedjor inom t.ex. restaurang- och cafénäringen. Detta borde även gå att göra för flera tjänsteföretag!",
    "business_model":u"Medlemsavgift per användare",
    "price_per_unit": 20000,
    "competitors":u"Beror på bransch.",
    "competitor_market_size":"",
    "exceptions": ["hotell", "VD:ar", "CTO:er", "marknadschefer"],
    "role": True
    }
]

target_groups=[
	{
	"name":u"tandläkare",
	"number":u"Det finns c:a 8 000 tandläkare i Sverige, men förmodligen kan man även ta betalt av andra yrkesroller inom tandvården. Totalt arbetar *25 000* personer i tandvården.",
	"swe_customers":25000,
	"number_source":u"http://www.tlv.se/"
	},
	{
	"name":u"hotell",
	"number":u"Det finns c:a 2 000 hotell i Sverige, och låt oss anta att det finns två säljare per hotell, dvs *4000* hotellsäljare.",
	"swe_customers":4000,
	"number_source":u"http://www.hotels.com/"
	},
	{
	"name":u"krögare",
	"number":u"Det finns c:a 20 000 restauranger i Sverige, och låt oss anta att det är en person per restaurang som blir användare.",
	"swe_customers":20000,
	"number_source":u"http://www.scb.se/"
	},
	{
	"name":u"advokater",
	"number":u"Det finns c:a 6 000 advokater i Sverige, och låt oss anta att det på varje advokat går två juniora jurister (som också kan bli användare).",
	"swe_customers":18000,
	"number_source":u"http://www.advokatsamfundet.se/"
	},
	{
	"name":u"fastighetsmäklare",
	"number":u"Det finns c:a 7 000 fastighetsmäklare i Sverige, och låt oss anta att det på varje mäklare går en halv mäklarassistent (som också kan bli användare).",
	"swe_customers":10500,
	"number_source":u"http://www.maklarsamfundet.se/"
	},
	{
	"name":u"IT-konsulter",
	"number":u"Det finns c:a 44 000 företag som säljer programvara och IT-tjänster i Sverige, och låt oss anta att varje företag i snitt har 4 potentiella användare.",
	"swe_customers":176000,
	"number_source":u"https://www.itot.se/om-oss/statistik/statistik-foretag//"
	},
	{
	"name":u"elektriker",
	"number":u"Det finns c:a 95 000 elinstallatörer och elektriker i Sverige.",
	"swe_customers":95000,
	"number_source":u"http://www.tidningenelektrikern.se/"
	},
	{
	"name":u"VD:ar",
	"number":u"Det finns 138 000 personer med titeln VD på LinkedIn i Sverige, men förmodligen är endast c:a 20 procent av dessa mottagliga för tjänsten.",
	"swe_customers":28000,
	"number_source":u"https://www.linkedin.com/",
    "role": True,
	},
	{
	"name":u"CTO:er",
	"number":u"Det finns 8 500 personer med titeln CTO på LinkedIn i Sverige, men detta är troligen en underskattning av den verkliga siffran så vi räknar med minst 10 000 st.",
	"swe_customers":10000,
	"number_source":u"https://www.linkedin.com/",
    "role": True,
	},
	{
	"name":u"marknadschefer",
	"number":u"Det finns c:a 13 000 personer med titeln CMO eller marknadschef på LinkedIn i Sverige.",
	"swe_customers":13000,
	"number_source":u"https://www.linkedin.com/",
    "role": True,
	},
	{
	"name":u"arkitekter",
	"number":u"Det finns c:a 13 000 arkitekter i Sverige.",
	"swe_customers":13000,
	"number_source":u"https://www.arkitekten.se/",
	},
	{
	"name":u"tillverkande industri",
	"number":u"Det finns c:a 10 000 industriföretag med fler än 4 anställda i Sverige.",
	"swe_customers":10000,
	"number_source":u"https://www.tillvaxtverket.se/",
	},
	{
	"name":u"åkerier",
	"number":u"Det finns c:a 10 000 åkeriföretag i Sverige.",
	"swe_customers":10000,
	"number_source":u"https://www.akerier.se/",
	},
	{
	"name":u"redovisningskonsulter",
	"number":u"Det finns c:a 3 000 auktoriserade redovisningskonsulter i Sverige, så det totala antalet (inkl icke-auktoriserade) är förmodligen åtminstone 10 000 st.",
	"swe_customers":10000,
	"number_source":u"https://www.revisionsvarlden.se/",
	}


]

"""
  	  <li>hairdressers</li>
  	  <li>construction firms</li>
  	  <li>web designers</li>
  	  <li>game developers</li>
  	  <li>camping venues</li>
  	  <li>sports associations</li>
  	  <li>oil companies</li>
  	  <li>horse breeders</li>
  	  <li>hospitals</li>
  	  <li>tourism agencies</li>
  	  <li>manufacturers</li>
  	  <li>grocery stores</li>
  	  <li>ad agencies</li>
  	  <li>IT consultants</li>
  	  <li>fast food outlets</li>
  	  <li>retail businesses</li>
      <li>small businesses</li>
      <li>Instagrammers</li>
      <li>Twitter users</li>
      <li>Substack users</li>
      <li>Gumroad creators</li>
      <li>E-mail marketers</li>
      <li>developers</li>
      <li>recruiters</li>
      <li>COOs</li>
      <li>CMOs</li>

  	  <li>set their prices</li>
  	  <li>manage suppliers</li>
  	  <li>sell excess capacity</li>
  	  <li>benchmark their costs</li>
  	  <li>benchmark their prices</li>
  	  <li>lower their costs</li>
  	  <li>find co-founders</li>
  	  <li>invest their profits</li>
  	  <li>manage pensions</li>
      <li>find more customers</li>
  	  <li>localize their service</li>
      <li>expand to new markets</li>
  	  <li>find right suppliers</li>
  	  <li>identify unhappy customers</li>
  	  <li>survey their customers</li>
  	  <li>reach more customers</li>
  	  <li>pick marketing channels</li>
  	  <li>get Twitter followers</li>
  	  <li>build a community</li>
  	  <li>become more creative</li>
      <li>hide their side hustle</li>
      <li>reach 1000 true fans</li>
      <li>monetize their audience</li>
      <li>grow their e-mail list</li>

"""

basecontent=u"""---
layout: page
title: "Affärsidé: {headline}"
---
{intro}

**Antal möjliga kunder i Sverige:** {customers_in_sweden}(källa: [{number_source}]({number_source}))

**Marknadspotential i Sverige:** {market_size_sweden} (vi räknar med en årsintäkt per användare på {fee} kr)

**Konkurrenter:** {competitors} {competitor_fill}

#### Några andra affärsidéer riktade mot samma målgrupp:
{random_ideas}


#### Några andra möjliga målgrupper för samma idé:
{random_target_groups}

#### Andra inlägg jag skrivit på detta tema:
- {link_one}
- {link_two}
- {link_three}

"""

landing_page_content=u"""---
layout: page
title: {total_number} gratis affärsidéer för dig som vill starta eget
---
Jag har gjort en sammanställning av {total_number} gratis affärsidéer med tillhörande recept för hur man kommer igång med dem. Se nedan för några exempel som du sedan kan klicka dig vidare från. Håll till godo!

#### Exempel:
{list_of_ideas}

#### Andra inlägg jag skrivit på detta tema:
- {link_one}
- {link_two}
- {link_three}

"""

for service in services:
	for target_group in [tg for tg in target_groups if not tg["name"] in service["exceptions"]]:
		headline=u"{gender} {service} {prep} {target_group}".format(
            gender=service["gender"],
			service=service["name"],
            prep=service["preposition"] if "preposition" in service else u"för",
			target_group=target_group["name"]
		)
		filename=parameterize(headline)
		file = open("{filename}.md".format(filename=filename), "w")
		content = basecontent.format(
			headline=headline,
            competitor_fill=random.choice([
                u"Har ännu inte undersökt om det finns direkta konkurrenter inom nischen.",
                u"Det kan säkert finnas mer nischade aktörer som man behöver se upp med.",
                u"Hemmagjorda lösningar kan säkert förekomma också."
                ]),
            competitors=service["competitors"],
            fee=service["price_per_unit"],
            number_source=target_group["number_source"],
			intro=service["intro"],
            random_ideas=", ".join([u"[{a} {b}](/affarsideer/{c}/)".format(a=i["gender"],b=i["name"], c=parameterize(u"{g} {s} {prep} {target_group}".format(
                g=i["gender"],
    			s=i["name"],
                prep=i["preposition"] if "preposition" in i else u"för",
    			target_group=target_group["name"]
    		))) for i in random.sample(services, 3) if not i["name"]==service["name"] and not target_group["name"] in i["exceptions"]]),
            random_target_groups=", ".join([u"[{a}](/affarsideer/{c}/)".format(a=i["name"], c=parameterize(u"{g} {s} {prep} {target_group}".format(
                g=service["gender"],
    			s=service["name"],
                prep=service["preposition"] if "preposition" in service else u"för",
    			target_group=i["name"]
    		))) for i in random.sample(target_groups, 5) if not i["name"]==target_group["name"] and not i["name"] in service["exceptions"]]),
			customers_in_sweden=target_group["number"],
			market_size_sweden=u"{size} Mkr per år".format(size=service["price_per_unit"]*target_group["swe_customers"]/1000000),
            link_one=u"[Hur man hittar affärsidéer]({% post_url 2020-11-08-hur-man-hittar-affarsideer %})",
            link_two=u"[10 sätt att blåsa en minoritetsägare]({% post_url 2020-10-13-10-satt-att-blasa-aktieagare %}) (när du väl startar företaget)",
            link_three=u"[Checklista för B2B SaaS-bolag]({% post_url 2020-12-02-checklista-for-b2b-saas-bolag %})",
			)

		file.write(content.encode("utf8"))
		file.close()

file = open("gratis-ideer.md".format(filename=filename), "w")
services_subset=services
target_group_subset=random.sample(target_groups, len(services))
random.shuffle(services_subset)
random.shuffle(target_group_subset)
services_subset=[u"{p} {t} {prep}".format(p=s["gender"], t=s["name"], prep=s["preposition"] if "preposition" in s else u"för") for s in services_subset]
target_group_subset=[u"{t}".format(t=s["name"]) for s in target_group_subset]
random_combinations=list(zip(services_subset, target_group_subset))
content=landing_page_content.format(
    total_number=len(services)*len(target_groups),
    list_of_ideas="""
""".join([u"- [{s} {t}](/affarsideer/{c}/)".format(s=i[0], t=i[1], c=parameterize(u"{s} {t}".format(
        s=i[0], t=i[1]
    ))) for i in random_combinations]),
    link_one=u"[Hur man hittar affärsidéer]({% post_url 2020-11-08-hur-man-hittar-affarsideer %})",
    link_two=u"[10 sätt att blåsa en minoritetsägare]({% post_url 2020-10-13-10-satt-att-blasa-aktieagare %}) (när du väl startar företaget)",
    link_three=u"[Checklista för B2B SaaS-bolag]({% post_url 2020-12-02-checklista-for-b2b-saas-bolag %})",
)
file.write(content.encode("utf8"))
file.close()
