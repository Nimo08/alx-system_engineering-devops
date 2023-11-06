# Automate the task of creating a custom HTTP header response, but with Puppet

$server_hostname = $facts['networking']['fqdn']

package { 'nginx':
  ensure => 'installed',
}

file_line { 'add custom http header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'location / {',
  line   => "add_header X-Served-By ${server_hostname};",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
