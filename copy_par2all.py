#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

prj_lst=[
"par1_merge.json",
"par1_txt_eps.json",
"par1_txt.json",
"par1_xml.json",
"par1.json"
]


def copy(fpath1,man1,man2):
    fpath2=fpath1.replace(man1,man2)
    print(fpath1,fpath2)
    with open(fpath1,'r') as f:
        txt=f.read()
    s=txt.replace(man1,man2)
    with open(fpath2,"w+") as f:
        f.write(s)
    os.chmod(fpath2,0o666)

for p in prj_lst:
    fpath1=f'prj/{p}'
    copy(fpath1,'par1','tor1')
    copy(fpath1,'par1','tou1')
    copy(fpath1,'par1','ven1')
