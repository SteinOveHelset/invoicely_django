server {
    listen 80;
    server_name invoicely.codewithstein.com;
    return 301 https://invoicely.codewithstein.com$request_uri;
}

server {
    listen 443 ssl;
    server_name invoicely.codewithstein.com;

    client_max_body_size 4G;

    error_log  /webapps/invoicely/environment_3_8_2/logs/nginx-vue-error.log;
    access_log /webapps/invoicely/environment_3_8_2/logs/nginx-vue-access.log;

    ssl_certificate /etc/letsencrypt/live/invoicely.codewithstein.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/invoicely.codewithstein.com/privkey.pem;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

    charset utf-8;
    root /webapps/invoicely/dist_invoicely;
    index index.html index.htm;

    location / {
        root /webapps/invoicely/dist_invoicely;
        try_files $uri /index.html;
    }
}
