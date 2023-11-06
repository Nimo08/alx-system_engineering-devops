# Automate the task of creating a custom HTTP header response, but with Puppet

exec { 'add custom http header':
  command => "echo 'add_header X-Served-By \{"$server_hostname\}";' >> /etc/nginx/sites-available/default",
  require => exec { 'install nginx package' },
  notify  => Service['nginx'],
}
