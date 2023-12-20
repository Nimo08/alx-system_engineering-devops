# Fix stack to get failed requests to 0

exec {'replace_u-limit':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before  => Exec['restart_nginx'],
}

exec {'restart_nginx':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}
