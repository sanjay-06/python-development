n=0
command=$l
while ! $command && [ $n -le 5 ]; do
  sleep $n
  ((n+=1))
  echo "Retry #$n"
done;
