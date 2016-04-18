The random module contains a perfectly good solution for the task
random.sample(seq,k) wil return a random sample of size k from the sequence seq
it is optimized and changes behaviour according to the sizes of input sequence and sample size.
In case requested sample size exceeds the size of a given sequence, the script will alert user and
return the sequence shuffled. random.shuffle() works in-place with no additional memory