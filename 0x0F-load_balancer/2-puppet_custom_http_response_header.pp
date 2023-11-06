# Automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add custom http header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'location / {',
  line   => 'add_header X-Served-By "405012-web-01";',
}

service { 'nginx':
  ensure  => 'running',
  require => Package[nginx],
}
