# This Puppet script installs a package
package { 'flask':
  ensure => '2.1.0',
  source => 'pip3',
}
