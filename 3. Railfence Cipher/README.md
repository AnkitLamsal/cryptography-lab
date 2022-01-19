# Rail Fence Cipher

Rail Fence Cipher is the classical transposition(permutation) cipher
It hides the message by rearranging the letter order without altering the actual letters used.

We write the message letters out diagonally over a number of rows and then read off cipher row by row.

Here is the example of Rail Fence Cipher


Key:	 	4 	3	2	1	5	6	7
Plain Text:	a	t	t	a	c	k	p
		o	s	t	p	o	n	e
		d	u	n	t	i	l	t
		w	o	a	m	x	y	z

Cipher Text: APTMTTNATSUOAODWCOIXKNLYPETZ

Rail Fence is more secure than other subsitution based cipher techniques. As it will be harder to have cryptanalysis of Permutation based cipher techniques.

