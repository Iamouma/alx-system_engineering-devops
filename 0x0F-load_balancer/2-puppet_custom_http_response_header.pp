# This updates package information
exec { 'apt-update':
  command => '/usr/bin/apt-get -y update',
  path    => ['/usr/bin', '/bin'],
}

# This Installs Nginx package
package { 'nginx':
  ensure => installed,
}

# This creates a basic HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# This configures Nginx to add the custom HTTP header
file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

# This ensures Nginx is running
service { 'nginx':
  ensure => running,
}
