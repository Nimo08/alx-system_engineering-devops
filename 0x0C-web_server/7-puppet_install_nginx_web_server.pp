# Install and configure an Nginx server using Puppet
include nginx
file { '/etc/nginx/sites-available/redirect_me':
  ensure => file,
}
nginx::resource::server { 'default':
  ensure             => present,
  spdy               => 'off',
  http2              => 'off',
  proxy_read_timeout => '60s',
  proxy_send_timeout => '60s',
  proxy_set_header   => [],
  proxy_hide_header  => [],
  proxy_pass_header  => [],
  owner              => 'www-data',
  group              => 'www-data',
  mode               => '0644',
}
nginx::resource::location { 'index.html':
  ensure   => present,
  location => '/',
  content  => 'Hello World!',
}
nginx::resource::location { 'redirect_me':
  location => '^/redirect_me$',
  rewrite  => 'https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require  => File['/etc/nginx/sites-available/redirect_me'],
}
