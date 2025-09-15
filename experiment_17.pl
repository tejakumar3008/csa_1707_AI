% sum_from_1_to_n(N, Sum).
% Finds the sum of integers from 1 to N.

% Base case: sum of numbers from 1 to 1 is 1
sum_from_1_to_n(1, 1).

% Recursive case
sum_from_1_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_from_1_to_n(N1, PartialSum),
    Sum is PartialSum + N.
