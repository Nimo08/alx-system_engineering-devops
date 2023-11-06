# Automate the task of creating a custom HTTP header response, but with Puppet

package { 'nginx':
  ensure => 'installed',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'location / {',
  line   => 'add_header X-Served-By $server_hostname;',
}

service { 'nginx':
  ensure  => 'running',
  require => Package[nginx],
}
