# -*- coding: utf-8 -*-
{
    'name': 'Lot/Sno Cost',
    'category': 'Website/Website',
    'summary': 'Added lot cost in addition to standard, fifo, avco',
    'version': '1.0',
    'depends': ['stock_account','product','stock'],
    'data':[
        'costing_view.xml','lotcost_list_detail_view.xml','stock_inventory_lotcost_view.xml'
        ],
    'installable': True,
    'auto_install': True,
    'description':"This module adds extra lotcost method along with other costing methods",
}
