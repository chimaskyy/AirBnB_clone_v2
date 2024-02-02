# Configures an Nginx server to server static contents

$html = @("EOF")
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

$config_content = @("EOF")
server {
    listen 80 default_server;
    loaction /hbnb_static/ {
        alias /data/web_static/current/;
	index index.html;
    }
	
    location / {
	root /data/web_static/current/;
	index index.html;
	try_files \$uri \$uri/ =404;
    }
    listen [::]:80;
}
EOF

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

file { '/data/' :
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/':
  ensure =>  directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/':
  ensure =>  directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure =>  directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/':
  ensure =>  directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/current':
  ensure =>  link,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  target => '/data/web_static/releases/test/',
}

file { '/data/web_static/releases/test/index.html' :
  ensure  =>  file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => $html,
}

file { '/etc/nginx/sites-available/default' :
  ensure  => present,
  content => $config_content,
}
