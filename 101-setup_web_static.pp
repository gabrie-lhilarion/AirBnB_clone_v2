# Puppet manifest to setup web servers to deploy web_static

# Update package repositories
package { 'apt-transport-https':
  ensure => installed,
}
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => ['/usr/bin', '/usr/sbin'],
}

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
               <head>
               </head>
               <body>
                 Holberton School
               </body>
             </html>',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Set ownership recursively
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file_line { 'hbnb_static_location':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => '    location /hbnb_static {',
  match   => '^[\s]*location \/ {',
  after   => 'last',
  notify  => Service['nginx'],
}

file_line { 'hbnb_static_alias':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => '        alias /data/web_static/current;',
  match   => '^[\s]*location \/hbnb_static {',
  after   => 'last',
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
