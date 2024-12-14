echo " BUILD START"
python3.10 -m pip install --upgrade -r requirements.txt
python3.10 manage.py collectstatic
echo " BUILD END"