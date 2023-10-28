# make changes to our configuration file
augeas { 'ssh_config':
  context => '/files/home/*/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
    'set IdentityFile ~/.ssh/school',
  ],
}
