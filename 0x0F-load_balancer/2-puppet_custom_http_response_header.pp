# thisalso automates the  creation of a custom http header response, but uses puppet
exec { 'update':
  command => 'sudo apt-get update',
  provider => shell,
}
package { 'nginx':
  ensure => exec['update],
}
file_line {'header line':
  ensure => 'present',
  path => '/etc/nginx/sites-available/default',
  after => 'listen 80 default_server;',
  line => "  location / {
  add_header X-Served-By ${hostname};",
  match => '^\tlocation / {',
  require => Package['nginx'],

}
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
