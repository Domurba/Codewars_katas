#2021-08-19 12:56:04.516000+00:00
"""You are given a table `numbers` with just one column, `number`. It holds some numbers that are already ordered.

You need to write a query that makes them un-ordered, as in, every possible ordering should appear equally often."""

select * from numbers
order by random()