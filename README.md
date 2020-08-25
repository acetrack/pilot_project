# pilot_project
version: python 3.6.3

vitualenv 설정
<pre>
console)python3.6 -m venv venv
</pre>

requirements.txt를 통해서 pakages 설치
<pre>
venv)pip install -r requirements.txt
</pre>

sqlite DB 첫 설정을 위해서
<pre>
venv)python manage.py makemigrations
venv)python manage.py migrate
venv)python manage.py createsuperuser

server 실행
</pre>

static file들을 사용하기 위해서 (./static_root/ 밑으로 모든 static file을 이동시켜줌)
<pre>
venv)python manage.py collectstatic
</pre>

django-allauth를 사용하기 위해서...
<pre>
현재 google만 가능한 상태
Client ID: XXXXXX (문의해 주세요)
Secret Key: XXXXX (문의해 주세요)
</pre>