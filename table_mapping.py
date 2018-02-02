mappings = [
    {
        'table': 'erl_mineraloccurrenceview',
        'pids':{
            'IDENTIFIER': 'erl:MineralOccurrenceView',
            'MINE_URI': 'er:Mine',
            'SPECIFICATION_URI': 'er:MineralOccurrence'
        },
        'vocabs': [
            'MINERALOCCURRENCETYPE_URI',
            'REPRESENTATIVECOMMODITY_URI',
            'HOSTGEOLOGICUNIT_URI',
            'MINERALDEPOSITMODEL_URI',
            'REPRESENTATIVEAGE_URI',
            'REPRESENTATIVEYOUNGERAGE_URI',
            'REPRESENTATIVEOLDERAGE_URI'
        ]
    },{
        'table': 'erl_commodityresourceview',
        'pids': {
            'IDENTIFIER':'erl:CommodityResourceView',
            'MINERALOCCURRENCE_URI':'er:MineralOccurrence',
            'MINE_URI':'er:Mine',
            'SPECIFICATION_URI':'er:Commodity',
        },
        'vocabs': {
            'COMMODITYCLASSIFIER_URI',
            'RESERVESCATEGORY_URI',
            'RESOURCESCATEGORY_URI',
            'CLASSIFICATIONMETHODUSED_URI'
        }
    },{
        'table': 'erl_mineview',
        'pids': {
            'IDENTIFIER':'erl:MineView',
            'SPECIFICATION_URI':'er:Mine'

        },
        'vocabs': {
            'SOURCE',
            'STATUS_URI'
        }
    },{
        'table': 'er_commodity',
        'pids': {
            'IDENTIFIER':'er:Commodity',
            'SOURCE':'er:MineralOccurrence'
        },
        'vocabs': {
            'COMMODITY_HREF'
        }
    },{
        'table': 'er_commoditymeasure',
        'pids': {
            'COMMODITY_IDENTIFIER':'er:Commodity'
        },
        'vocabs': {
            'UOM_HREF'
        }
    },{
        'table': 'er_mine',
        'pids': {
            'IDENTIFIER':'er:Mine'
        },
        'vocabs': {
            'STATUS_HREF',
            'SOURCEREF_HREF',
            'OBSERVATIONMETHOD_ID'
        }
    },{
        'table': 'er_mineraloccurrence',
        'pids': {
            'IDENTIFIER':'',
            'PARENT_IDENTIFIER':''
        },
        'vocabs': {
            'TYPE_HREF',
            'SOURCEREF_HREF',
            'OBSERVATIONMETHOD_ID'
        }
    },{
        'table': 'er_reserve',
        'pids': {

        },
        'vocabs': {
            'UOM_HREF',
            'CATEGORY_HREF',
            'CLASSIFICATIONMETHOD',
            'SOURCEREF_HREF'
        }
    },{
        'table': 'er_resource',
        'pids': {

        },
        'vocabs': {
            'UOM_HREF',
            'CATEGORY_HREF',
            'CLASSIFICATIONMETHOD',
            'SOURCEREF_HREF'
        }
    }
]
