
Run like this:

> git clone rms_pkgs into sibling level directory
> python -m venv .venv
> source turn_on_env.sh
> pip install -r requirements.txt
> python computeROC.py ~/tmp ./testInputForROC/just_Covid_negativesThrombOrNotWithCore98.txt

input file assumptions:
# header
# zero or one, threshold value, sorted. 

is_thrombosis	Total FIXa (pM) 
1	46113.54

To control how many thresholds are printed (numbers may bleed into each other otherwise) check out
print_x_thresh param, documented in computeROCcommandLine.txt
