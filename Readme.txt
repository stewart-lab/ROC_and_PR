
Run like this:

> git clone rms_pkgs into sibling level directory
> python -m venv .venv
> source turn_on_env.sh
> pip install -r requirements.txt
> python computeROC.py ~/tmp ./testInputForROC/just_Covid_negativesThrombOrNotWithCore98.txt

input file assumptions:

is_thrombosis	blank	Total FIXa (pM)
1	x	46113.54

header
zero or one, dud variable for now, threshold value, sorted. 

