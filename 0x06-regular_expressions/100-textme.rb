#!/usr/bin/env ruby
log = ARGV[0]

sender_match = log.match(/\[from:(.*?)\]/)
receiver_match = log.match(/\[to:(.*?)\]/)
flags_match = log.match(/\[flags:(.*?)\]/)

res = "#{sender_match[1]}, #{receiver_match[1]}, #{flags_match[1]}"
puts res
