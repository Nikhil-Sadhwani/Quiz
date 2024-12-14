echo " BUILD START"
pip install --upgrade -r requirements.txt
python3.10 manage.py collectstatic
echo " BUILD END"