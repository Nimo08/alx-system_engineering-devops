# Automate the task of creating a custom HTTP header response, but with Puppet
exec { 'command':
  command  => 'apt-get update; apt-get install -y nginx;
  sed -i "51i add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}

