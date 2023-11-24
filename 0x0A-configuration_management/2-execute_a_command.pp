#kills a process named killmenow

exec {'process_killer':
  command => 'pkill killmenow',
  path    => ['/usr/bin'],
}
