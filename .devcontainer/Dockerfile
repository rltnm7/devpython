FROM python:3.9.0-alpine3.12

# git, openjdk (SonarLint用) とpytest関連モジュールをインストール
RUN apk update \
 && apk add --no-cache git=2.34.1-r0 \
 && apk add --no-cache openjdk17-jre=17.0.2_p8-r0 \
 && pip install --upgrade pip --no-cache-dir

# psycopg2をインストールしたい場合 (手動でやってもOK)
RUN apk add --no-cache postgresql-libs \
 && apk add --no-cache --virtual .build-deps gcc=10.3.1_git20211027-r0 musl-dev=1.2.2-r7 postgresql13-dev=13.5-r1 \
 && pip install psycopg2==2.9.3 --no-cache-dir \
 && apk --purge del .build-deps
