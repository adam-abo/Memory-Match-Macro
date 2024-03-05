def identify(items, collected):
    known_items = {}
    with open('/Users/adamabouelela/Desktop/Memory-Match-Macro/RGB Values.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line by colon ':' to separate key and value
            value, key = line.strip().split(':')
            if key != 'Empty':
                known_items[key] = value.strip()

    for item in items:
        quantity = item[3]
        item = item[:3]

        if str(item).replace(' ', '') in known_items:
            item = known_items[str(item).replace(' ', '')]

        if item in collected:
            collected[item] += quantity
        else:
            collected[item] = quantity               
    return collected

def writeSummary(items, games = {}):
    with open('/Users/adamabouelela/Desktop/Memory-Match-Macro/Session Summary.rtf', 'w') as f:
        f.write('{\\rtf1\\ansi\\ansicpg1252\\cocoartf2759\n\\cocoatextscaling0\\cocoaplatform0{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica-Bold;\\f1\\fswiss\\fcharset0 Helvetica;}\n{\\colortbl;\\red255\\green255\\blue255;}\n{\\*\\expandedcolortbl;;}\n{\\*\\listtable{\\list\\listtemplateid1\\listhybrid{\\listlevel\\levelnfc23\\levelnfcn23\\leveljc0\\leveljcn0\\levelfollow0\\levelstartat1\\levelspace360\\levelindent0{\\*\\levelmarker \\{hyphen\\}}{\\leveltext\\leveltemplateid1\\\'01\\uc0\\u8259 ;}{\\levelnumbers;}\\fi-360\\li720\\lin720 }{\\listlevel\\levelnfc23\\levelnfcn23\\leveljc0\\leveljcn0\\levelfollow0\\levelstartat1\\levelspace360\\levelindent0{\\*\\levelmarker \\{hyphen\\}}{\\leveltext\\leveltemplateid2\\\'01\\uc0\\u8259 ;}{\\levelnumbers;}\\fi-360\\li1440\\lin1440 }{\\listname ;}\\listid1}\n{\\list\\listtemplateid2\\listhybrid{\\listlevel\\levelnfc23\\levelnfcn23\\leveljc0\\leveljcn0\\levelfollow0\\levelstartat1\\levelspace360\\levelindent0{\\*\\levelmarker \\{hyphen\\}}{\\leveltext\\leveltemplateid101\\\'01\\uc0\\u8259 ;}{\\levelnumbers;}\\fi-360\\li720\\lin720 }{\\listlevel\\levelnfc23\\levelnfcn23\\leveljc0\\leveljcn0\\levelfollow0\\levelstartat1\\levelspace360\\levelindent0{\\*\\levelmarker \\{hyphen\\}}{\\leveltext\\leveltemplateid102\\\'01\\uc0\\u8259 ;}{\\levelnumbers;}\\fi-360\\li1440\\lin1440 }{\\listname ;}\\listid2}}\n{\\*\\listoverridetable{\\listoverride\\listid1\\listoverridecount0\\ls1}{\\listoverride\\listid2\\listoverridecount0\\ls2}}\n\\margl1440\\margr1440\\vieww17500\\viewh12440\\viewkind0\n\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\n\\f0\\b\\fs36 \\cf0 \\ul \\ulc0 ')
        f.write('Macro Session Summary:') # Header
        f.write('\n\\f1\\b0\\fs30 \\ulnone \\\n\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\n\\fs32 \\cf0 	\\ul ')
        f.write('Total Items Collected:') # Mini-header
        f.write('\\ulnone \\\n\\pard\\tx940\\tx1440\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\li1440\\fi-1440\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\\ls1\\ilvl1\n\\fs30 \\cf0 ')
        
        for key, value in items.items(): # Items Collected
            f.write('{\\listtext	\\uc0\\u8259 	}' + f'{key}: {value}' + '\\\n')

        f.write('\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\\cf0 	\\\n\n\\fs32 	\\ul ')
        f.write('Games Played:') # Mini-header 2
        f.write('\\\n\\pard\\tx940\\tx1440\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\li1440\\fi-1440\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\\ls2\\ilvl1\n\\fs30 \\cf0 \\ulnone ')
        
        for key, value in games.items(): # Games Played
            f.write('{\\listtext	\\uc0\\u8259 	}' + f'{key}: {value}' + '\\\n')

        f.write('\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\sl360\\slmult1\\pardirnatural\\partightenfactor0\n\\cf0 }')

writeSummary({}, {})