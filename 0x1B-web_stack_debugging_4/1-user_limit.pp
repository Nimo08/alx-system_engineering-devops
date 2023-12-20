# Fix stack to get failed requests to 0
# Change the OS configuration to login with the holberton user

exec {'replace_u-limit':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before  => Exec['restart_nginx'],
}

exec {'restart_nginx':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}

if $ulimit_value != '15' {
  Exec['replace_u-limit'] -> Exec['restart_nginx']
}
