
<mano> è il nome abbreviato del manoscritto.
es.
PARIGI  => par
VENEZIA => ven
TOUr    => tor
TOLOSA  => tou
======================

buid_tei.sh <mano>
esegue 
source ./setteimed.sh
teimprj.py eps2<mano>.json
teimprj.py fl_<mano>.json
-------------------------
** c(alternativa) oandi separati:

buid_eps <mano>
eaegue
source ./setteimed.sh
teimprj.py eps2<mano>.json

buid_flsh <mano>
esegue 
source ./setteimed.sh
teimprj.py fl_<mano>.json

=========================
azione dei diversi scripts
=========================
source ./setteimed.sh
setta le variabili ambiente

cd <mano>
teimprj.py eps2<mano>.json
fa il merge degli episodi
e scrive il file
flori<mano>.txt

es.
file
ep2par.json
per il merge degli episodi:
{
    "merge": {
        "out": "floripar1.txt",
        "files": [
            "./eps/fl_par1_ep12.txt",
            "./eps/fl_par1_ep13.txt",
            "./eps/fl_par1_ep14.txt",
            "./eps/fl_par1_ep15.txt",
            "./eps/fl_par1_ep16.txt",
            "./eps/fl_par1_ep17.txt",
            "./eps/fl_par1_ep18.txt",
            "./eps/fl_par1_ep19.txt",
            "./eps/fl_par1_ep20.txt",
            "./eps/fl_par1_ep21.txt",
            "./eps/fl_par1_ep22.txt",
            "./eps/fl_par1_ep23.txt",
            "./eps/fl_par1_ep24.txt",
            "./eps/fl_par1_ep25.txt",
            "./eps/fl_par1_ep26.txt",
            "./eps/fl_par1_ep27.txt",
            "./eps/fl_par1_ep28.txt"
        ]
    }
}
--------------------------------
teimprj.py fl_<mano>.json
produce il file
flori<mano>.xml
Il file va in ./flsite/xml/<mano>
Da utilizzare per produrre html in flsite.

es.
file
fl_par.json
per le trasformazione dai tag TEIMED ai tag TEI-XML
{
    "exe": [
        "teimxml.py -i floripar1.txt -t ../fl_teimed_tags.csv -o flori1.txt",
        "teimlineword.py -i flori1.txt -o flori2.xml -s G -n 'pb:1,cb:1,lg:1,l:1'",
        "teimxmllint.py -i flori2.xml -o flori3.xml ",
        "teimspan.py -i flori3.xml -o flori4.xml",
        "teimnote.py -i flori4.xml -o flori5.xml -n ../fl_note.csv",
        "teimxmllint.py -i flori5.xml -o floripar.xml "
    ]
}
===================================
script python per la trasformazione TEIMED => XML-TEI
---------------------------------------------
teimxml.py
usage: teimxml.py [-h] [-t] -i  -o
optional arguments:
  -h, --help  show this help message and exit
  -t          [-t <file tags>] default:tags.csv
  -i          -i <file input>
  -o          -o <file output>

sostituisce entities con tag leggendo da tag.csv
---------------------------------------------
teimlineword.py
usage: teimlineword.py [-h] -i  -o  -s  [-n]
optional arguments:
  -h, --help  show this help message and exit
  -i          -i <file input>
  -o          -o <file output>
  -s          -s <sigla mano scritto> (prefisso id)
  -n          -n <'pb:1,cb:1,lg:1,l:1,ptr:1'> (start id elementi)

aggiuge i tag <l> e <w>
numera pb,cb,lg,l,w,ptr
è possibile settare il numero iniziale per pb,cb,lg,lptr
-s <sigla> setta la sega davanti all'id delle righe e delle
parole per manoscritti diversi
PARIGI  => G
TOUR    => K
TOLOSA  => T
VENEZIA => I
----------------------------------------------
teimspan.py
usage: teimspan.py [-h] [-t] -i  -o
optional arguments:
  -h, --help  show this help message and exit
  -t          [-t <file tags span>]
  -i          -i <file input>
  -o          -o <file output>

gestione span

definite in un file esterno oppure definite nel testo
----------------------------------------------
teimnote.py
usage: teimnote.py [-h] -n  -i  -o
optional arguments:
  -h, --help  show this help message and exit
  -n          -n <file note>
  -i          -i <file input>
  -o          -o <file output>

legge le note da un file csv e le aggiunge al file xml
----------------------------------------------
teimdict.py
usage: teimdict.py [-h] -i  -o
optional arguments:
  -h, --help  show this help message and exit
  -i          -i <file input>
  -o          -o <file output>

crrea dizionario
-------------------------------------------
teimxmllint.py -i
usage: teimdict.py [-h] -i  -o
optional arguments:
  -h, --help  show this help message and exit
  -i          -i <file input>
  -o          -o <file output>

formatta e controlla un file xml
--------------------------------------
teimprj.py filename.json
esegue un progetto definito in un  file json
