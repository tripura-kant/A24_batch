#Demo

i=1; for f in *; do [ -f "$f" ] && mv "$f" "${i}_$f" && ((i++)); done

https://github.com/codeanddebugedu/leetcode-solutions