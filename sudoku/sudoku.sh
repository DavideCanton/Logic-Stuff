if [ $# -ne 2 ]
then
	echo "Parametri non validi"
    exit 1
fi

if [ ! -f $1.logic ]
then
	python3 schema_to_logic.py -l $1 > $1.logic
fi
clingo3 $1.logic sudoku.logic > $$.l
if [ $? -eq 20 ]
then
    echo "Sudoku irrisolvibile!"
    exit 1
fi
python3 schema_to_logic.py -s $$.l > $2
rm $$.l
