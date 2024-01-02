echo "BUILD START"
pip install -r requirements.txt
python3.9 manage.py mcollectstatic --noinput --clear
echo "BUILD END"