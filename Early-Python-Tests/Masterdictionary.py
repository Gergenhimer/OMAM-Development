
#master list
personaldict={
    'player':['pc','npc'],
    'occupation':{
        'servant':['personal chef','butler','housekeeper','driver'],
        'employed':{
            'artisan':['shipwright','smith','carpenter','builder','cooper','candlemaker','luthier','tailor','butcher','sea captain','conductor','railroad engineer','chef'],
            'educated':['professor','doctor','librarian','historian','lawyer','architect'],
            'apprentice':'under artisan',
            'laborer':['farmer','chimney sweep','lumberjack','day laborer','hunter','rancher','miner','sailor','factory worker'],
            'military':['general','colonel','soldier'],
            'entrepeneur':['small','medium','large']
            },
        'elite':{
            'royal':['sovereign','duke'],
            'noble':['earl','baron','knight'],
            'oligarch':['inherited from entrepeneur','robber baron','university president'],
            'legislator':['national','regional','local']
            },
        'talent':{
            'performer':{
                'small band':['guitarist','pianist','drummer','singer'],
                'orchestral':['violinist','violist','cellist','bassist','trumpeter','trombonist','cowbellist'],
                'other':['dancer','acrobat','juggler','magician']
                },
            'artist':['painter','sculptor','writer']
            },
        },
    'gender':['male', 'female','other'],
    'income':['impoverished','lower class','middle class','upper class','fabulously wealthy'],
    'age':['young','adult','middle aged','elderly']
}
employerdict = { #slots in list indicate heirarchy. First owns the company, then people beneath that, then people beneath that. slots may include lists of strings.
    'house':{'elite',''
        },
    'small business':{
        },
    'medium business':{
        'shipbuilder':[['shipwright','entrepeneur'],'shipwright',['carpenter','builder'],'apprentice'],
        'cooperage':[['cooper','entrepeneur'],['cooper','carpenter'],'apprentice'],
        'smithy':['smith','apprentice'],
        'construction company':[['']]
        },
    'large business':{
        'mining company':['robber baron','miner','day laborer'],
        'factory':['robber baron','factory worker'],
        'railroad company':['robber baron','conductor','railroad engineer','chef'],
        'university':['university president','professor','librarian','historian'],
        'shipping company':['robber baron','sea captain','sailor']
        }

    
    
    
    
    }
relationshipdict={
        'family':{
            'parental':['parent','child'],
            'pibnib':['pibling','nibling'],
            'sibling':['sibling','sibling'],
            'cousin':['cousin','cousin'],
            'grandparental':['grandparent','grandchild']
            },
        'coworkers':{'colleague':['colleague','colleague'],
                     'hierarchy':['boss','employee'],
                     'master-servant':['master','servant']
                     },
        'rivals':['professional','romantic'],
        'lovers':['partner','spouse','lover','friend with benefits','pursuer','persued'],
        'old friends':['childhood','gradeschool','university','long-time colleague','hobby friend'],
        'exes':['lover','old friend'],
        'co-habitators':['family','roommate','fellow servant']
        'none':['never heard of them','know their reputation','share an acquaintance']
        }
genderdict={
    'pibling':['uncle','aunt'],
    'sibling':['brother','sister'],
    'parent':['father','mother'],
    'sovereign':['king','queen'],
    'duke':['duke','duchess'],
    'earl':['earl','countess'],
    'baron':['baron','baroness'],
    'knight':['knight','dame']
    
    }
def makeemptycharacter(characterindex,playerchar):  #create empty
    
    
    
    
    
    
    
    
  
