# install flask from pip3
package { 'flask':
  ensure          => 'installed',
  provider        => 'pip3',
  install_options => ['--prefix=/usr'],
}
