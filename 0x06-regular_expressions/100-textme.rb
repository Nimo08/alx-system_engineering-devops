#!/usr/bin/env ruby
log = ARGV[0]
match = log.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
res = match.join(',')
puts res
