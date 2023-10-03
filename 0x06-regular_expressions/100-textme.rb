#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*\b)\] \[to:(.*\b)\] \[flags:(.*\b)\]/).join
