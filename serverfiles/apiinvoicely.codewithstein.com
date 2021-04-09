upstream invoicely_app_server {
    server unix:/webapps/invoicely/environment_3_8_2/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name apiinvoicely.codewithstein.com;
    return 301 https://apiinvoicely.codewithstein.com$request_uri;
}

server {
    listen 443 ssl;
    server_name apiinvoicely.codewithstein.com;

    client_max_body_size 4G;

    access_log /webapps/environment_3_8_2/logs/nginx-django-access.log;
    error_log /webapps/environment_3_8_2/logs/nginx-django-error.log;

    ssl_certificate /etc/letsencrypt/live/apiinvoicely.codewithstein.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/apiinvoicely.codewithstein.com/privkey.pem;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

    location /static/ {
        alias /webapps/invoicely/environment_3_8_2/invoicely/static/;
    }

    location /media/ {
        alias /webapps/invoicely/environment_3_8_2/invoicely/media/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_set_header Host $http_host;

        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://invoicely_app_server;
        }
    }
}
