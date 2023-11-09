# Automates Bash script that sets up your web servers for the deployment of web_static

package { 'nginx':
  ensure => 'present',
}

file { '/data/':
  ensure => 'directory',
}

file { '/data/web_static/':
  ensure => 'directory',
}

file { '/data/web_static/releases/':
  ensure => 'directory',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

exec { 'nginx_conf':
  environment => ['data=\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'],
  command     => 'sed -i "56i $data" /etc/nginx/sites-available/default',
  path        => '/usr/bin:/usr/sbin:/bin:/usr/local/bin'
}
-> service { 'nginx':
  ensure => running,
}
