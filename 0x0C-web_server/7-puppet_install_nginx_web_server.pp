# Install and configure an Nginx server using Puppet
class { 'nginx':
  listen_port => 80,
}
file { '/etc/nginx/sites-available/redirect_me':
  ensure => file,
}
nginx::resource::server { 'default':
  ensure   => present,
  location => [
    {
      location => '/',
      content  => 'Hello World!',
    },
    {
      location => '^/redirect_me$',
      rewrite  => 'https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    },
  ],
  require  => File['/etc/nginx/sites-available/redirect_me'],
}
