# Automate the task of creating a custom HTTP header response, but with Puppet
exec { 'command':
  command  => 'apt-get -y update; apt-get -y install nginx;
  sed -i "51i add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}

